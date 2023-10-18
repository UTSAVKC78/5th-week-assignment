input_string = input("enter a string: ")

num_counting = 0
upp_counting = 0
low_counting = 0
other_counting = 0

for char in input_string:
    if char.isnumeric():
        num_counting += 1
    elif char.isupper():
        upp_counting += 1
    elif char.islower():
        low_counting += 1
    else:
        other_counting += 1

print("numbers:", num_counting)
print("uppercase letters:", upp_counting)
print("lowercase letters:", low_counting)
print("other characters:", other_counting)
