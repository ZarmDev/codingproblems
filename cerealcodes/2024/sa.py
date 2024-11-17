arr_l = int(input().strip())
arr = input().strip().split()

highest_num = 0
index_to_delete = None
for i in range(arr_l):
    arr[i] = int(arr[i])
    if arr[i] > highest_num:
        highest_num = arr[i]
        index_to_delete = i

del arr[index_to_delete]

other_num_sum = 0

for i in arr:
    other_num_sum += i

arr.sort(reverse=True)

check = False

## FIRST CHECK

if highest_num == other_num_sum:
    print("YES")
else:
    check = True

## SECOND CHECK

if check:
    check_2 = False
    while highest_num > 0:
        # Subtract the greatest number until it reaches zero
        # print(arr, other_num_sum, highest_num)
        if other_num_sum - arr[0] < highest_num:
            del arr[0]
            continue
        other_num_sum -= arr[0]
        del arr[0]

        if other_num_sum == highest_num:
            print("YES")
            check_2 = True
            break

    if (not check_2):
        print("NO")