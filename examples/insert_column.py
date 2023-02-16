# -*- encoding: utf-8 -*-
# Generated with SMOP 0.42-beta Improved by 杨波@塔尔旺科技 2023
try:
    from smop.lib import *
except ImportError:
    raise ImportError('File compiled with `smop3`, please install `smop3` to run it.') from None
# examples\insert_column.m

# simulate matlab workspace
workspace_ = locals()


workspace_.update(load('abc.mat'))
# 说明
@function
def foo(*args,**kwargs):
    varargin = foo.varargin
    nargin = foo.nargin

    # 注释
    b=matlabarray()
    b[1,:]=concat([4,5,6])
    a=foo(b)
    R=b[1,:]
    return R
    
if __name__ == '__main__':
    pass
    