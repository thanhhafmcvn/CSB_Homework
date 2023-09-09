classmate = []

while len(classmate) < 5:
    name = input("Enter a name: ")
    classmate.append(name)
    if len(classmate) == 5:
        break
for i in classmate:
    print(f"Xin chào, {i}")
