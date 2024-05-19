"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    
    def find_tailing_zeroes(self, number: int) -> int | str:

        if number < 0:
            print("number can not be negative")
            return

        fact_number = 1
        for i in range(1, number+1):
            fact_number = fact_number * i

        str_number = str(fact_number)
        str_number = str_number[::-1]
        i = 0 
        for text in str_number:
            if text != "0":
                break
            if text == "0":
                i += 1
        result = "result is " + str(i)
        print(result)
        return i



Solution().find_tailing_zeroes(7)
