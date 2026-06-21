from functools import reduce
r=[1,2,4,7,9]
res=reduce(map(lambda x,y:x if x>y else y,r))
print(res)