def quick_sort(sequence):
    length=len(sequence)
    
    if length<=1:
        return(sequence)
    else:
        pivot=sequence.pop()
    
    lower_items=[]
    greater_items=[]
        
    for item in sequence:
        if item<pivot:
            lower_items.append(item)
        else:
            greater_items.append(item)
    return(quick_sort(lower_items)+[pivot]+quick_sort(greater_items))
print(quick_sort([2,3,4,1,2,5,9]))
