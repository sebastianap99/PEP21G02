# def factorial(number):
#     n = int(number)
#     for i in range(1, n):
#         n = n * i
#     return n
#
#
# print(factorial(4))
#
#
# def factorial_rec(n):
#     if (n <= 1):
#         return 1
#     else:
#         return n * factorial_rec(n - 1)
#
#
# for i in range(10):
#     print(factorial_rec(i))

# def flatten(test_list):
#     if isinstance(test_list, list):
#         if len(test_list) == 0:
#             return []
#         first, rest = test_list[0], test_list[1:]
#         return flatten(first) + flatten(rest)
#     else:
#         return [test_list]

# def flatten_list(data: list):
#         fin_list = []
#         for i in data:
#             if type(i) == int:
#                 fin_list.append(i)
#                 continue
#             print(i)
#             fin_list.extend(flatten_list(i))
#         return fin_list

test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]


def not_shown(test_data,nr_holes=10):
    result=set()
    for game_result in test_data:
        result=result.union(set(game_result))


not_shown(test_data)

def pinball_game(test_data, nr_holes = 10):
    result = set()

    for game_result in test_data:
        result = result.union(set(game_result))
    holes_set = set(range(1, nr_holes + 1))
    print(holes_set)
    result = holes_set.difference(result)
    print(result)

pinball_game(test_data)
