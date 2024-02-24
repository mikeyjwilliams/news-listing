from typing import List

class Algos:
    def __init__(self, *args,):
        self._array_data = []
        self.target = None
        
        
    def binary_search(self, sorted_array: List[int], target: int) -> int:
        '''
        Returns the index of the target in the array, or -1 if the target is not in the array.
        :param array: The array to search.
        :param target: The target to search for.
        :return: The index of the target in the array, or -1 if the target is not in the array.
        '''
        left = 0
        right = len(sorted_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_array[mid] == target:
                return mid
            elif sorted_array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1