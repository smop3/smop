import os
from setuptools import setup

from smop.version import __version__ as __VERSION__

# try:
#    __VERSION__ = os.popen("git describe --tags").read().strip()
# except OSError as e:
#    __VERSION__ = ""
#
# open("smop/version.py","w").write("__version__='%s'" % __VERSION__)

setup(
    author="Victor Leikehman",
    author_email="victorlei@gmail.com",
    description="Matlab to Python converter. Community maintained fork for Python 3.",
    license="MIT",
    keywords="convert translate matlab octave python",
    url="https://github.com/victorlei/smop",
    download_url="https://github.com/victorlei/smop",
    name="smop3",
    version=__VERSION__,
    entry_points={
        "console_scripts": [
            "smop = smop.__main__:main",
        ],
    },
    packages=["smop"],
    install_requires=[
        "ply",
        "numpy",
        "scipy",
        "networkx>=2.0.0",
    ],
    extras_require={"test": ["pytest"]},
)
