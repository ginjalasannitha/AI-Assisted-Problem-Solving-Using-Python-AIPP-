# recursive fibonacci with explanation

def fibonacci(n):
    """returns nth fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Fibonacci({n}) =", fibonacci(n))
