'''
An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic, or false otherwise.
'''


def monotonic_array(array):
    
    n=len(array)
    if n==0: return True
    
    first=array[0]
    last=array[n-1]
    
    if first>last:
        #MD or False
        for k in range(n-1):
            if array[k]<array[k+1]:return False
    elif first==last:
        #Mnontonic or False
        for k in range(n-1):
            if array[k]!=array[k+1]:return False
    else:
        #MI or false
        for k in range(n-1):
            if array[k] > array[k+1]:return False
    
    return True

array=[1,2,3,4,5]
print(monotonic_array(array))