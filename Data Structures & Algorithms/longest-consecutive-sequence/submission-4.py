class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newnum=set(nums)
        longest=0

        for num in newnum:
            if (num-1) not in newnum:    
                length=1
                while(num+length)in newnum:
                    length+=1
                longest=max(length,longest)

        return longest

        