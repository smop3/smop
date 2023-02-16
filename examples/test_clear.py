# -*- encoding: utf-8 -*-
# Generated with SMOP 0.42-beta Improved by 杨波@塔尔旺科技 2023
try:
    from smop.lib import *
except ImportError:
    raise ImportError('File compiled with `smop3`, please install `smop3` to run it.') from None
# examples\test_clear.m

# simulate matlab workspace
workspace_ = locals()


clear('id_sw','sw_tmp')
id_sw=matlabarray()
sw_tmp=matlabarray()