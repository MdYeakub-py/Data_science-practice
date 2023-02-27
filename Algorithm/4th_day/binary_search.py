position = 0
def Sort(binary_search, search_value):
    low = 0
    high = len(binary_search)-1
    found = 0
    while low <= high :
        mid = (low + high)//2
        if search_value == binary_search[mid]:
            globals() ['position'] = mid
            return True
        elif search_value > binary_search[mid]:
            low = mid + 1
        else :
            high = mid - 1
            
         


binary_search:int= [4, 12, 45, 80, 2, 20, 56]
binary_search.sort()
search_value = int(input("Enter Search value :"))

if Sort(binary_search, search_value):
    print("Value is found at position number :", position+1)
else:
    print("Value not found")
    
