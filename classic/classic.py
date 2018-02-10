# https://proglib.io/p/greatest-python-one-liners/


max_xy = lambda x,y: x if x > y else y
print(max_xy(-2,-1))

# Map
n = [1,2,3,4]
print((map(lambda x:x**2 + 2, n)))

# Reduce
n = [1,2,3,4]
print(reduce (lambda x,y: x*y, n))

#Filter
n = [1,2,3,4]
print (list(filter(lambda x: x > 2, n)))

# Quick Sort
n = [-3,5,8,3,-7,0,3,6,-1]
qsort = lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])
print(qsort(n))

# Distination between 2 points
# zip - http://ninjaside.info/blog/ru/funkcii-map-i-zip-i-lambda-python/ + nice design
dist = lambda w,v : (sum((wi - vi)**2 for wi,vi in zip(w,v)))**.5
print(dist([0,0], [3,3]))

# Pi
pi = 4*sum((-1.0)**(n%2) / (2*n + 1) for n in range(2010))
print(pi)

# gen unbreak array
print map(lambda x:x+1,range(0,20))

# simple digits
print filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0, map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))

# fibonnachi
print map(lambda x,f=lambda x,f:(x<=1) or (f(x-1,f)+f(x-2,f)): f(x,f), range(20))

# all cross product
cross_product = [(a, b) for a in ['a', 'b', 'c'] for b in [1, 2, 3]]
print (cross_product)

# gen strings from 2 string
def string_parcer(string, numbers): return ', '.join(map(lambda s,n:s+str(n), [string for i in numbers], numbers))
print(string_parcer("string", "012345"))

### linean alg

# mult vector on digit
def scale(A, x): return [ai*x for ai in A]
print(scale([3,4,5], 2))

# summ 2 vectors
A = [1, 2, 3]
B = [5, 8, 10]
def add(A, B): return [ai+bi for (ai, bi) in zip(A, B)]
print(add(A,B))

# invert (Tx) matrix
a=[[1,2,3],[4,5,6],[7,8,9]]
inverted_a = [list(i) for i in zip(*a)]
print(a[0])
print(a[1])
print(a[2])
print(inverted_a[0])
print(inverted_a[1])
print(inverted_a[2])

### another

# random element
import random; a = random.choice(['alpha', 'beta', 'gamma', 'delta'])
print(a)

# 
M = ['a', 'b', 'c', 'c', '1', '100', 'a10']
M.append('Beta')
print(M)