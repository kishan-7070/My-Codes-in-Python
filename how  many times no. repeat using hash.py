arr=[1,2,3,1,2,3,4,2,4,2]
hashmap={}
for num in arr:
    if num in hashmap:
        hashmap[num]+=1
    else:
        hashmap[num]=1
print(hashmap)