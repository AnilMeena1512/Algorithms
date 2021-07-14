def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
        
    return(-1)
            
arr=[2,3,5,6,7]
x=7
result=linear_search(arr,x)
if result==-1:
    print("The element is not found")
else:
    print("The element is found at index:",result)

    
