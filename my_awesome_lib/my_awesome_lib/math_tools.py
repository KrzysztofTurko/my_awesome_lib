def calculate_average(numbers):
    """
    Oblicza średnią z listy liczb.
    
    :param numbers: Lista liczb.
    :return: Średnia z listy liczb.
    :raises ValueError: Jeśli lista jest pusta.
    """
    if not numbers:
        raise ValueError("Lista liczb nie może być pusta.")
    return sum(numbers) / len(numbers)

def factorial(n):
    """
    Oblicza silnię liczby n.
    
    :param n: Liczba całkowita.
    :return: Silnia liczby n.
    :raises ValueError: Jeśli n jest ujemne.
    """
    if n < 0:
        raise ValueError("Silnia jest zdefiniowana tylko dla liczb nieujemnych.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result