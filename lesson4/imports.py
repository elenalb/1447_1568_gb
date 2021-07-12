# импортирование в python - все import по стандарту должны стоять в начале файла!

# импорт из стандартных библиотек

import time as t
import random

print(t.time())
print(random.random())

from time import time as t
from random import random

print(t())
print(random())

# импорт из собственных модулей

import my_module

my_module.show_message()
print(my_module.simple_calc(2))

from my_module import show_message, simple_calc

show_message()
print(simple_calc(4))
