# словари
my_dict = dict(key_1="val_1", key_2="val_2")
print(my_dict)
new_dict = {1: 'one', 2: 'two'}
print(new_dict)

print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
print(new_dict.get(1))
print(new_dict.get(3))
print(new_dict[1])
print(my_dict.popitem())
print(my_dict.pop('key_1'))
new_dict.update({3: 'three', 4: 'four'})
new_dict.update({5: 'five'})
print(new_dict)

new_dict_1 = {1: ['one', 'один', 'ein', 'uno']}
value = new_dict_1.get(1)
print(value)
