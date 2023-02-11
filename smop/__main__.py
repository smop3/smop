# SMOP -- Simple Matlab/Octave to Python compiler
# Copyright 2011-2016 Victor Leikehman
import glob
import sys
import os
import traceback
from os.path import basename, splitext

from smop import options
from smop import parse
from smop import resolve
from smop import backend
from smop import version

from textwrap import dedent


def print_header(fp):
    if options.no_header:
        return
    # print("# Running Python %s" % sys.version, file=fp)
    # context = locals()
    # context.update(options=options, version=version)
    template = f"""# -*- encoding: {options.encoding} -*-
# Generated with SMOP {version.__version__}
try:
    from smop.libsmop import *
except ImportError:
    raise ImportError('File compiled with `smop3`, please install `smop3` to run it.') from None
# {options.filename}

# simulate matlab workspace
workspace_ = locals()
"""
    print(template, file=fp)


def main():
    if "M" in options.debug:
        import pdb

        pdb.set_trace()
    # implement glob pattern
    if options.glob_pattern:
        options.filelist += glob.glob(options.glob_pattern)
    if not options.filelist:
        options.parser.print_help()
        return
    if options.output == "-":
        fp = sys.stdout
    elif options.output:
        fp = open(options.output, "w")
    else:
        fp = None
    if fp:
        print_header(fp)

    nerrors = 0
    for i, options.filename in enumerate(options.filelist):
        try:
            if options.verbose:
                print(i, options.filename)
            if not options.filename.endswith(".m"):
                print("\tIgnored: '%s' (unexpected file type)" % options.filename)
                continue
            if basename(options.filename) in options.xfiles:
                if options.verbose:
                    print("\tExcluded: '%s'" % options.filename)
                continue
            buf = open(options.filename, encoding=options.encoding).read()
            buf = buf.replace("\r\n", "\n")
            # FIXME buf = buf.decode("ascii", errors="ignore")
            stmt_list = parse.parse(buf if buf[-1] == "\n" else buf + "\n")

            if not stmt_list:
                continue
            if not options.no_resolve:
                G = resolve.resolve(stmt_list)
            if not options.no_backend:
                s = backend.backend(stmt_list)
            if not options.output:
                f = splitext(basename(options.filename))[0] + ".py"
                output_dir = "."
                if options.output_directory:
                    output_dir = options.output_directory
                f = output_dir + "/" + f
                if options.verbose:
                    print("output: ", f)
                with open(f, "w", encoding=options.encoding) as fp:
                    print_header(fp)
                    fp.write(s)
            else:
                fp.write(s)
        except KeyboardInterrupt:
            break
        except:
            nerrors += 1
            traceback.print_exc(file=sys.stdout)
            if options.strict:
                break
        finally:
            pass
    if nerrors:
        print("Errors:", nerrors)


if __name__ == "__main__":
    print("Running main")
    main()
