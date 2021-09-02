import random


def random_list(my_list, k):
    if my_list and k <= len(my_list):
        return [my_list.pop(random.randint(0,len(my_list)-1)) for _ in range(k)]
    return []


def random_list_with_prob(my_list, my_prob, k):
    """Для решения 2й задачи использован метод рулетки,
    используемый в генетических алгоритмах.

    В основе идеи метода лежит представление популяции
    в виде колеса рулетки, где для каждой особи имеется
    сектор, размер которого пропорционален значению её
    показателя приспособленности.

    """

    if my_list and 0 < k <= len(my_list):
        my_prob = [x*10 for x in my_prob]
        result=[]
        for _ in range(k):
            sum_prob = sum(my_prob)
            random_count = random.randint(0, sum_prob-1)
            for i,_ in enumerate(my_list):
                random_count -= my_prob[i]
                if random_count<0:
                    result.append(my_list.pop(i))
                    del my_prob[i]
                    break
        return result
    return []


def main() -> None:
    input_list = [1, 3, 4, 0, 9]
    k = 3
    prob = [.7, .4, .5, .9, .1]
    print(random_list(input_list[:], k))
    print(random_list_with_prob(input_list[:], prob[:], k))


if __name__ == "__main__":
    main()