"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

class Solution:
    def number_to_thai(self, number: int) -> str:
            if number > 10000000:
                 print("number is over 10000000")
                 return
            if number < 0 :
                 print("number can not less than 0")
                 return
            number_text = str(number)
            number_array = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
            digit_array = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน", "สิบล้าน"]
            text_result = ""
            number_len = len(number_text)
            for i in range(number_len):
                tmp = int(number_text[i])
                if tmp != 0:
                    if (i == (number_len - 1)) and (tmp == 1):
                        text_result += "เอ็ด"
                    elif (i == (number_len - 2)) and (tmp == 2):
                        text_result += "ยี่"
                    elif (i == (number_len - 2)) and (tmp == 1):
                        text_result += ""
                    elif number_len < 8:
                        text_result += number_array[tmp]
                    text_result += digit_array[number_len - i - 1]
            print(text_result)  
            return text_result

    # Example usage
Solution().number_to_thai(112)
