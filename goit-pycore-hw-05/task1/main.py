def caching_fibonacci():
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    fib = caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

if __name__ == "__main__":
    main()