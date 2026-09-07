class Solution:
    def hasDuplicate(self, numbers: List[int]) -> bool:
        hashset=set()
        for i in numbers:
            if i in hashset:
                return True
            hashset.add(i)
        return False        