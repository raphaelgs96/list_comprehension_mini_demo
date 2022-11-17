def base_func(max_range: int) -> list:
    # CASO 1
    # Iterar sobre uma lista e adicionar cada elemento em uma nova lista

    list_result = []

    for num in range(1, max_range + 1):
        list_result.append(num)

    return list_result

    # return [num for num in range(1, max_range + 1)]


    # CASO 2
    # Iterar sobre uma lista e adicionar cada elemento multiplicado por 2 em uma nova lista

    # list_result = []

    # for num in range(1, max_range + 1):
    #     list_result.append(num * 2)

    # return list_result

    # return [num * 2 for num in range(1, max_range + 1)]


    # CASO 3
    # Iterar sobre uma lista e adicionar cada elemento em uma nova lista caso ele seja par

    # list_result = []

    # for num in range(1, max_range + 1):
    #     if num % 2 == 0:
    #         list_result.append(num)
    
    # return list_result

    # return [num for num in range(1, max_range + 1) if num % 2 == 0]


    # CASO 4
    # Iterar sobre uma lista e adicionar a string 'par' caso o elemento seja par ou 'impar' caso ele seja impar

    # list_result = []

    # for num in range(1, max_range + 1):
    #     if num % 2 == 0:
    #         list_result.append('par')
    #     else:
    #         list_result.append('impar')

    # return list_result

    # return ['par' if num % 2 == 0 else 'impar' for num in range(1, max_range + 1)]


print(base_func(10))
