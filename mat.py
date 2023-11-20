#написать функцию, которая создает массив из всех четных элементов между 50 и 90.
def create_even_array():
    even_array = []
    for num in range(50, 91):
        if num % 2 == 0:
            even_array.append(num)
    return even_array

result = create_even_array()
print(result)
