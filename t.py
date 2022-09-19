nums = [0,1,0,3,12]
i=0
s=0
while i!=len(nums)-1:
    if nums[i]==0:
        del nums[i]
        s+=1
    else:
        i+=1
for j in range(s):
    nums.append(0)
print(nums,"7")
