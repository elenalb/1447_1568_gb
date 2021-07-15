import os

# os.remove("text_for_x.txt")

# os.rename("new_text_file", "renamed_file")

print(os.listdir())

print(os.path.basename(r"C:\Users\elena.babenko\PycharmProjects\1447_1568_gb\lesson5\test_file.txt"))
print(os.path.dirname(r"C:\Users\elena.babenko\PycharmProjects\1447_1568_gb\lesson5\test_file.txt"))

os.path.exists("renamed_file")
print(os.path.join("file_dir", "filename"))
