# bytes / bytearray

print(b'text')
print(type(b'text'))
my_bytes = 'текст'.encode('utf-8')
print(my_bytes.decode())
print(bytes('текст', encoding='utf-8'))

my_var = bytearray(b"some text")
print(my_var)
print(my_var[1])
