def list_to_dict(keys, values):
    """
    Konwertuje dwie listy (klucze i wartości) na słownik.
    
    :param keys: Lista kluczy.
    :param values: Lista wartości.
    :return: Słownik utworzony z kluczy i wartości.
    :raises ValueError: Jeśli listy mają różną długość.
    """
    if len(keys) != len(values):
        raise ValueError("Listy kluczy i wartości muszą mieć tę samą długość.")
    return dict(zip(keys, values))

def filter_data(data, condition):
    """
    Filtruje listę danych na podstawie warunku.
    
    :param data: Lista danych do przefiltrowania.
    :param condition: Funkcja warunku filtrowania.
    :return: Przefiltrowana lista.
    """
    return [item for item in data if condition(item)]