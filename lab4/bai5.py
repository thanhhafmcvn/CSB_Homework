step = 0
end_number = 1000
while step <= 10:
    if sum([int(i) for i in str(end_number)]) == 9:
        print(end_number, end=" ",)
        step += 1
    end_number += 1
    if step == 10:
        break
