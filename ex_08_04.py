fname = input("Enter the file name: ")
try:
    with open(fname, "r") as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.extend(line.split())
        
    print(words)
    print(len(words))

    new_list = []

    for word in words:
        if word not in new_list:
            new_list.append(word)

    print(sorted(new_list))
    print(len(new_list))

except:
    print("File cannot be opened:", fname)
    exit()