
'''
Реалізуйте функцію caching_fibonacci,
яка створює та використовує кеш для зберігання і
повторного використання вже обчислених значень чисел Фібоначчі.
'''

# ФУНКЦІЯ caching_fibonacci
#     Створити порожній словник cache

#     ФУНКЦІЯ fibonacci(n)
#         Якщо n <= 0, повернути 0
#         Якщо n == 1, повернути 1
#         Якщо n у cache, повернути cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]

#     Повернути функцію fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci

def caching_fibonacci(n):
    cache = []

    def fibonacci(n):
        pass


        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
