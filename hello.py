def summer_69(arr):
    print(arr)

    sum = 0
    flag = True

    for i in arr:
        if i == 6 or i == 9:
            flag = not flag
            # print(flag)
        if flag and i != 9:
            sum += i
        # print(i)

    print(f"Sum = {sum}")
# Check
summer_69([1, 3, 5])

# Check
summer_69([4, 5, 6, 7, 8, 9])

# Check
summer_69([2, 1, 6, 9, 11])