import math

def compute_population(t):
   #вычислить численность населения для года t по формуле


#ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые


# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list


# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"