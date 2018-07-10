n,k=[int(i) for i in input().strip().split()]
arr=[int(i) for i in input().strip().split()]
non_divisible=set()

for j in range(n-1):
    for x in range(j+1,n):
        if (arr[j]+arr[x]) % k!=0:
            non_divisible.add(arr[j])
            non_divisible.add(arr[x])
            
print(len(non_divisible))
            
