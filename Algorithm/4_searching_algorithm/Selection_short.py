
def Sort(selection_sort):
    
    for i in range (6):
        min_index = i
        for j in range(i, 7):
            if selection_sort[j] < selection_sort[min_index]:
                min_index=j
        
        # swapping index value into temp
        temp = selection_sort[i]
        #swapping minimum value into .. running index position    
        selection_sort[i] = selection_sort[min_index]
        # finaly swapping running index value swapping into minimum index position
        selection_sort[min_index] = temp
        
        
        
        print (selection_sort)
        


selection_sort:int= [4, 12, 45, 80, 2, 20, 56]
Sort(selection_sort)

print("Ascending Order by selection sort is: :" ,selection_sort)
    
