# числа
# int()

print(abs(-10))

print(bin(4))  # двоичный формат - 0100
print(bin(6))  # 0110
# 0100
# 0110
# 0100
print(4 & 6)  # побитовое И
print(4 | 6)  # побитовое ИЛИ
print(4 ^ 6)  # побитовое исключающее ИЛИ

print(oct(4))  # восьмеричный формат
print(hex(4))  # шестнадцатеричный формат

# float() - числа с плавающей точкой - дроби
print(type(4.6))

# complex()
# a + i*b
# i * i = -1 ; в python мнимая единица - j
n_1 = complex(5, 6)
print(n_1)
n_2 = complex(1, 2)
print(n_1 + n_2)
