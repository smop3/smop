# -*- encoding: utf8 -*-

import numpy as np
from .libsmop import matlabarray


def diff(X, n=1, dim=1):
    """实现 matlab 的 diff(X) 函数，如果 X 是矩阵，会沿行求差分而不是沿列。

    用法:
    Y = diff(X)
    Y = diff(X,n)
    Y = diff(X,n,dim)

    参数：
    X - matlabarray 数组或矩阵
    n - int，可选，求导次数
    dim - int, 正整数标量，沿 dim 指定的维计算，和 matlab 中一样从 1 开始，1表示行维度，2表示列维度。

    返回: matlabarray 结果对象

    >>> a = matlabarray([[1,3,6], [2,4,7]])
    >>> d = diff(a,1)
    >>> print(d)
    [[1 1 1]]

    >>> a = matlabarray([[1,3,6], [2,4,7]])
    >>> d = diff(a, 1, dim=2)
    >>> print(d)
    [[2 3]
     [2 3]]

    matlab
    =======
    diff 差分和近似导数

    语法:
    Y = diff(X)
    Y = diff(X,n)
    Y = diff(X,n,dim)

    Y = diff(X) 计算沿大小不等于 1 的第一个数组维度的 X 相邻元素之间的差分：

    如果 X 是长度为 m 的向量，则 Y = diff(X) 返回长度为 m-1 的向量。Y 的元素是 X 相邻元素之间的差分。
        Y = [X(2)-X(1) X(3)-X(2) ... X(m)-X(m-1)]

    如果 X 是不为空的非向量 p×m 矩阵，则 Y = diff(X) 返回大小为 (p-1)×m 的矩阵，其元素是 X 的行之间的差分。
        Y = [X(2,:)-X(1,:); X(3,:)-X(2,:); ... X(p,:)-X(p-1,:)]

    如果 X 是 0×0 的空矩阵，则 Y = diff(X) 返回 0×0 的空矩阵。

    matlab 版本：在 R2006a 之前推出

    python 实现
    ===========
    用 numpy.diff() 实现。

    注意：matlab 中默认是沿‘row’求差分，而 numpy 是沿最后一个维度求差分，所以需要修正这一点。

    """
    # 要先转换成 nunpy.ndarray，不能用 matlabarray 做运算，否则 numpy.diff 的 index 要求从0开始，而 matlabarray 的 index 从 1 开始
    X = np.asarray(X)
    return matlabarray(np.diff(X, n, dim-1))


if __name__ == '__main__':
    """Test"""
    import doctest
    doctest.testmod()
