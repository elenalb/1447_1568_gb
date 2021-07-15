# менеджер контекста

# f = open("test_file.txt")
# for line in f:
#     print(line)
# f.close()

with open("test_file.txt") as f:
    for line in f:
        print(line)
