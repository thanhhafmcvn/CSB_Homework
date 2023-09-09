arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
plus_two_arr = []
multiply_two_arr = []
shift_two_arr = arr[2:] + arr[:2]
for i in arr:
    plus_two_arr.append(i+2)
    multiply_two_arr.append(i*2)
    # shift_two_arr.insert(arr.index(i)-2,i)

print(plus_two_arr)
print(multiply_two_arr)
print(shift_two_arr)