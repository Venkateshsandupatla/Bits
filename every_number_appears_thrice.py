def thrice(arr):
    arr = sorted(arr)
    b = []
    for i in range(2,len(arr)):
        count = 0
        if arr[i-2] == arr[i-1] == arr[i]:
            count+=1
            b.append(arr[i])
    arr = set(arr)
    b = set(b)
    print(arr-b)

        

aa = [2,2,3,2,7,7,8,7,8,8]
#thrice(aa)

# 
def th(arr):
    b = sum(aa)
    print(b)
    print(b%3)

th(aa)