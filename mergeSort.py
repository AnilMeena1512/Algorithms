def mergeSort(array):
    if len(array)>1:
        r=len(array)//2
        p=array[:r]
        q=array[r:]
        mergeSort(p)
        mergeSort(q)
        i=j=k=0
        
        while i <len(p) and j<len(q):
            if p[i]<q[j]:
                array[k]=p[i]
                i+=1
            else:
                array[k]=q[j]
                j+=1
            k+=1
        #when we run out from the element in either p and q
        #pick the remaining element
        
        while i<len(p):
            array[k]=p[i]
            i+=1
            k+=1
        while j<len(q):
            array[k]=q[j]
            j+=1
            k+=1
            
            
            
array = [6, 5, 12, 10, 9, 1]

mergeSort(array)

print("Sorted array is: ")
print(array)
