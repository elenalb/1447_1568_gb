# форматирование строк

name = "Lena"

# %
print("Hello, %s!" % name)
# %d - digit
# %f - float
print("%-10s %-10s %-10s" % ('param1', 'param2', 'param3'))

# format()
print("Hello, {}".format(name))
print("{:>20} {:>20} {:>20}".format('param1', 'param2', 'param3'))
print("{:.3f}".format(4.324342432424))

# f-string
print(f"Hello, {name}")
print(f"{'param1':>20} {'param2':>20}")
print(f"{2.342432434:.4f}")
