user_input = str(input("Write a sentence: "))
splited_string = user_input.split(" ")
unique = len({word for word in splited_string})
print(f"Number of unique words: {unique}")
