#!/usr/bin/env python
# coding: utf-8

# In[7]:


arr = [1,1,1,1,1,2,2,5,8,7,5,0]

# empty set is to store element frequencies
element_frequency = {}

# Count the frequencies of each element
for number in arr:
    if number in element_frequency:
        element_frequency[number] += 1
    else:
        element_frequency[number] = 1

# print the frequency of each element
print(" Number | Frequency")
for number , frequency in element_frequency.items():
    print(f"    {number}   |    {frequency}")


# In[4]:


#2.program to print maximun frequent element
class Solution:
   def solve(self, nums):
      max=0
      length=len(nums)
      for i in range(0,length-1):
         count=1
         for j in range(i+1,length):
            if(nums[i]==nums[j]):
               count+=1
               if(max<count):
                  max=count
      return max
ob = Solution()
nums = [1,5,8,5,6,3,2,45,7,5,8,7,1,4,6,8,9,10,8,8]
print(ob.solve(nums))


# In[11]:


#3.program to print minimum frequent element
def leastFrequent(arr, n):
    Hash={}
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
    min_count = n + 1
    res = 0
    for i in Hash:
        if (min_count >= Hash[i]):
            res = i
            min_count = Hash[i]
           
    return res
arr = [1,8,8,8,0,2,9]
print(leastFrequent(arr, len(arr)))


# In[ ]:




