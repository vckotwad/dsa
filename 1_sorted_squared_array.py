
'''
Question:-
You are given an array of Integers in which 
each subsequent value is not less than the previous value.
Write a function that takes
this array as an input and returns a new array with the squares of each number sorted in ascending order

'''


def sorted_squared(array):
    
    
    if len(array)==0:
        return []
        
    if len(array)==1:
        return [array[0]*array[0]]
        
    if array[0]>=0:
        new_array=[]
        for i in array:
            new_array.append(i*i)
        return new_array
        
    n=len(array)
    new_array=[0]*n
    i=0
    j=n-1
    for k in reversed(range(n)):
        if array[i]**2>array[j]**2:
            new_array[k]=array[i]**2
            i+=1 
        else:
            new_array[k]=array[j]**2
            j-=1 
    return new_array