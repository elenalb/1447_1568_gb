# print в файл

with open("print_to_file.txt", "w") as f:
    print("Test print to file!", file=f)
