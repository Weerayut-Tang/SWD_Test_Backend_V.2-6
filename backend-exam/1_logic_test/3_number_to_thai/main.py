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
        if number < 0:
            return "number can not less than 0"

        if number > 10_000_000:
            return "number out of range"

        if number == 0:
            return "ศูนย์"

        units = ["", "หนึ่ง", "สอง", "สาม", "สี่",
                 "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

        def convert_less_than_thousand(n):
            if n == 0:
                return ""

            result = ""

            hundred = n // 100
            n %= 100
            ten = n // 10
            unit = n % 10

            if hundred > 0:
                result += units[hundred] + "ร้อย"

            if ten == 1:
                result += "สิบ"
            elif ten == 2:
                result += "ยี่สิบ"
            elif ten > 2:
                result += units[ten] + "สิบ"

            if unit > 0:
                if unit == 1 and (ten > 0 or hundred > 0):
                    result += "เอ็ด"
                else:
                    result += units[unit]

            return result

        million = number // 1_000_000
        remainder = number % 1_000_000

        result = ""

        if million > 0:
            result += convert_less_than_thousand(million) + "ล้าน"

        if remainder > 0:
            result += convert_less_than_thousand(remainder)

        return result

