def binary_search(list,target):
    start=0
    end=len(list)-1
    while start<=end:
        mid=(start+end)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1

list=[1,2,3,4,5,6,7,8,9]
target=5
result=binary_search(list,target)
if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
     