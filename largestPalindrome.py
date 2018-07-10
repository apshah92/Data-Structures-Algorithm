n,k=[int(i) for i in input().strip().split()]
n=n-1
original=input().strip()
reverse=original[::-1]
xorString=''
for o,r in zip(original,reverse):
    xorString+= '0' if o==r else '1'
largestnum=reverselargenum=original
difference=int(xorString.count('1')/2)
print(xorString)
if difference==k:
    largestnum=largestnum.split()
    reverselargenum=reverselargenum.split()
    for i in range(difference):
        if xorString[i]=='1':
            largestnum[i]=largestnum[n-i]
            reverselargenum[n-i]=reverselargenum[i]
    if int(''.join(largestnum))>=int(''.join(reverselargenum)):
        print((''.join(largestnum)))  
    
elif difference<k:
    largestnum=largestnum.split()
    reverselargenum=reverselargenum.split()
    for i in range(k-difference):
        if xorString[i]=='1':
            largestnum[i]=largestnum[n-i]='9'            
    reverselargenum= largestnum      
    for i in range(difference-1):
        if xorString[i]=='1':
            largestnum[i]=largestnum[n-i]
            reverselargenum[n-i]=reverselargenum[i]
    if int(''.join(largestnum))>=int(''.join(reverselargenum)):
        print((''.join(largestnum)))  

    
else:
    print('-1')
        
        
        
    
    
    

        
    
    
    
