# Платформа myte задание Factory5

### Задание:

1. Есть список input_list (python list) целых чисел длинной N. Необходимо выбрать k случайных элементов без повторений по индексу. Алгоритм решения должен быть оптимальным по сложности и по ресурсам, определить сложность в нотации O(N,k)  

Переводить список в другие структуры данных нельзя. Для получения единичного случайного числа можно использовать метод random.randint(A, B). Иные методы из random и в целом сторонние библиотеки использовать нельзя  

PS. Пожелание: не забудьте рассмотреть случай k —> N  

Пример:  

`input_list = [1, 3, 4, 3, 3, 9]`  

`k = 3`  

варианты ответа: [3, 4, 3] или [4, 1, 9] или [3, 1, 4] неправильные вариант ответа: [4, 4, 3] - 4 не должен быть более одного раза, потому что во входном списке встречается только единожды  

2. Дополнительно: Решить предыдущую задачу с условием того, что для каждого элемента входного списка есть соответствующая вероятность его выпадения. Вероятности представлены отдельным список той же длины. Пример списка вероятностей `prob = [.7, .4, .5, .9, .1]`, элементы лежать в диапазоне [0, 1], значения кратны 0.1  

### Решение:

1. Функция `random_list` возвращает требуемый список. Имеет линейную сложность O(k). Если на вход подается пустой список, k = 0 или больше длины списка, то на выход получим пустой список.  

2. Функция `random_list_with_prob` реализует отбор методом рулетки.
