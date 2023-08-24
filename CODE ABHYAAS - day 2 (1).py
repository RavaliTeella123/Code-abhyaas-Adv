#!/usr/bin/env python
# coding: utf-8

# In[3]:


1.#find the second largest and second smallest element in the array
def analyze_list(list1):
    length=len(list1)
    list1.sort()
    print("Largest number ",list1[length-1])
    print("Smallest number ",list1[0])
    print("second largest ",list1[length-2])
    print("second smallest ",list1[1])
list1=[1,3,56,60,3,0,8]
yet=analyze_list(list1)


# In[8]:


2.# Remove duplicate values
def remove_duplicates(arr):
    # Convert the array to a set to remove duplicates
    unique_set = set(arr)
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list
# Original array with duplicates
original_array = [3, 6, 2, 8, 6, 3, 9, 2, 1]
# Call the function to remove duplicates
array = remove_duplicates(original_array)
print("Original Array:", original_array)
print("Array with Duplicates Removed:", array)


# In[12]:


#3.Right rotate the array by one position 
test_list=[1,2,3,4,5]
print("The Original List is ",str(test_list))
test_list=test_list[-1:] + test_list[:-1]
print("The list after rotate is ",str(test_list))


# In[13]:


# Work Given:
# Check whether given array is sorted or not 
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Test cases
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 3, 2, 1]
arr3 = [1, 3, 2, 4, 5]

print("Is arr1 sorted?", is_sorted(arr1))
print("Is arr2 sorted?", is_sorted(arr2))
print("Is arr3 sorted?", is_sorted(arr3))


# In[ ]:




