def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


print(is_prime(3))


def primes(limit):
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    return result


print(primes(10))


def enc_dec(text, key):
    result = ''
    for letter in text:
        number = ord(letter)
        # print(chr(number ^ key))
        result += chr(number ^ key)
    return result

output = enc_dec("Hello World", 20500)
print(output)
output_dec = enc_dec(output, 20500)
print(output_dec)


def add_numbers():
    x=0
    number_list=[]
    while(x<=100):
        y=int(input("Adauga numar: "))
        if y>=0:
            x+=y
            number_list.append(y)

        if x==100:
            print("Numerele care insumate dau 100 sunt: ",number_list)
            break
    print("Suma numerelor introduse: ",x)

add_numbers()


# def add_numbers():
# #     sum = 0
# #     num_list = []
# #     while sum <= 100:
# #         if sum==100:
# #             break
# #         n = int(input("Enter numbers: "))
# #         if n >= 0:
# #             sum = sum + n
# #             num_list.append(n)
# #     else:
# #         return sum
# #     return num_list
# #
# # print(add_numbers())
