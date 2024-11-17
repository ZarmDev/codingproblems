# Get all multiples of given input
o = 0
num = int(input().strip())
digit_start = '1'
for i in range(num - 1):
    digit_start += '0'

digit_start = int(digit_start)

while (not digit_start % num == 0):
    digit_start += 1

originalnum = num
num = digit_start
# print(digit_start, 'huh')
while (o < 10):
    # get the next multiple
    num = num + originalnum
    # if current number contains the neccessary digits
    digits_to_check = [0,1,2,5,6,8,9]
    num_str = str(num)
    not_contains_digits = all((not str(digit) in num_str) for digit in digits_to_check)

    if not_contains_digits:
        continue

    # if you reverse it and replace...
    reversed_and_replaced = list(num_str)
    reversed_and_replaced.reverse()
    reversed_and_replaced = ''.join(reversed_and_replaced).replace('6', 'x').replace('9', '6').replace('x', '9')
    # print(num_str, reversed_and_replaced)
    # reversed_and_replaced = list(num_str.replace('6', 'x').replace('9', '6').replace('x', '9'))
    # print(num, reversed_and_replaced)
    # reversed_and_replaced.reverse()
    # reversed_and_replaced = ''.join(reversed_and_replaced)
    
    if reversed_and_replaced == num_str:
        print(num_str)
        break

    o += 1