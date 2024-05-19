"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self,numbers: list) -> int | str:
        if not any(numbers):
            print("list can not blank")
            return
        
        max_index = len(numbers) -1
        print(numbers[max_index])


Solution().find_max_index([2,3,5,6])
