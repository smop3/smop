a = []
a(:, 1) = [1,2,3]

function R=foo()
    b=[];
    b(1, :) = [4,5,6];
    R=b;
end
