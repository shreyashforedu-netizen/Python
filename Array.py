
import numpy as np
arr0=np.array(42)
print("0-D Array:\n",arr0)
arr1=np.array([1,2,3])
print("1-D Array:\n",arr1)
arr2=np.array([[1,2,3],[4,5,6]])
print("2-D Array:\n",arr2)

print(f"Multiplication:",np.multiply(arr0,arr1))
print(f"Addition:", np.add(arr0,arr2))
print(f"Subtract:", np.subtract(arr1,arr2))