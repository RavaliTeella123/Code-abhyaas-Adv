#!/usr/bin/env python
# coding: utf-8

# In[23]:


#1.Linear Search
def search(list1,key):
    for i in range(len(list1)):
        if key==list1[i]:
            print("key element is found at index",i)
            break
    else:
        print("key element is not found")
list1=[34,23,5,6,7,1,23,8]
print(list1)
key=int(input("enter the number: "))
search(list1,key)


# In[39]:


#2.Binary search
def binary_search(list1,key):
    low=0
    high=((len(list1)-1))
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if(key==list1[mid]):
            found=True
        elif (key>=list1[mid]):
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("key is found")
    else:
              print("key is not found")
list1=[2,3,1,4,2,3]
list1.sort()
print(list1)
key=int(input("enter the number"))
binary_search(list1,key)


# In[2]:


# 3. union of 2 arrays
def Union(list1,list2):
    final_list = list(set().union(list1,list2))
    return final_list
 
# Driver Code
list1 = [23, 15, 2, 14, 14, 16, 20 ,52]
list2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(list1,list2))


# In[ ]:




