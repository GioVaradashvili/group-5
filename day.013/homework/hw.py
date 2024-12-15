full_name = "gio varadashvili"

Consonant_count = 0 

for i in range(0, len(full_name)):
    char = (full_name[i])
    if char == "v" or char == "r" or char == "d" or char == "a":
        Consonant_count += 1

print(Consonant_count)