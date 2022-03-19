'''
Here we we apply the merge sort algorithm but restiting that to the length of its half insted of (M+N).
1. We need to calculate the median and median will be the middle element if total element is odd and average sum of two middle element if it is even. 
   So, for that we will first identity that index and pass into Merge Sort Function.
2. Merge Sort function will run till that index only and after execution our emement will be at the last index or last two index.
'''

def MergeSort(nums1,nums2,l):
    res = []
    m = i = j = 0
    while(m<=l):
        m +=1
        if (i>=len(nums1)):
            res.append(nums2[j])
            j += 1
        elif (j>=len(nums2)):
            res.append(nums1[i])
            i += 1
        elif (nums1[i]<=nums2[j]):
            res.append(nums1[i])
            i += 1
        elif (nums1[i]>nums2[j]):
            res.append(nums2[j])
            j += 1
    return res
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        indexx1 = indexx2 = 0
        if ( ( len1 + len2) % 2 == 0):
            indexx1 = (len1 + len2)//2
            indexx2 = indexx1 -1
            res = MergeSort(nums1,nums2,indexx1)
            median = (res[indexx1] + res[indexx2]) /2
        else:
            indexx1 = (len1 + len2)//2
            res = MergeSort(nums1,nums2,indexx1)
            median = res[(len1 + len2)//2]
        return (median)
      
      '''
      Time Cpmplexity: O((M+N)/2)==O(M+N)
      Space Cpmplexity: O((M+N)/2)==O(M+N)
      '''
        
