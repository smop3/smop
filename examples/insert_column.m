load("abc.mat");
% 说明
function R=foo()
    % 注释
    b=[];
    b(1, :) = [4,5,6];
    a=foo(b)
    R=b(1,:);
end
