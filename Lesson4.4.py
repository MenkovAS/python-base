'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.'''

from itertools import permutations
from itertools import repeat
from itertools import combinations
base_list = [1, 2, 2, 3, 4, 1, 2]
list = [el for el in base_list if base_list.count(el)==1]
print(list)