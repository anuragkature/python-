import numpy as np
x=[4,2,6,8,10]
arr =np.array(x)
arr
y=[[1,2,3],[3,2,1][4,5,6]]
arr=np.array(y)
arr
arr=np.zeros((4,4))
arr=np.ones((4,4))
arr
arr=np.random.random([3,2])
arr
arr=np.arange(1,30,3)
arr
arr=np.linspace(0,20,5)
arr
a=np.array([100,200,300])
b=np.array([[20,25,30],[40,50,60]])
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)

print("mean of array 'a' elements: ", np.mean(a))
print("standard deviation of array 'a' elements: ", np.std(a))
print("variance of array 'a'elements : ", np.var(a))
print("sum of array 'b'elemments : ", np.sum(b))
print("product of array  'b'elements :", np.prod(b))
a= np.aran("Arrayof Given interval",a)
arr = np. arange(1,40,4).reshaoe(5,2)
print("Trannspose of Array",arr .transpose())
arr1 = np.array([[1,2,3,4],[2,3,7,11]])
arr2 = np.array([[1,3,5,7][2,4,6,8]])
a= np.concatenate((arr1,arr2))
print("concatenate of Two Array",a)