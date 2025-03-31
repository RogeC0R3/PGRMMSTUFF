def bubble(list_A):
    indexing_length = len(list_A) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_A[i] > list_A[i+1]:
                sorted = False
                list_A[i], list_A[i+1] = list_A[i+1], list_A[i]
                return list_A 
print(bubble(1,32))                   
                
