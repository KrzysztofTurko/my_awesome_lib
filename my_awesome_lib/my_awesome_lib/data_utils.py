def convert_to_int(data):
    """
    Konwertuje listę ciągów znaków na listę liczb całkowitych.
    
    :param data: Lista ciągów znaków.
    :return: Lista liczb całkowitych.
    :raises ValueError: Jeśli konwersja nie jest możliwa.
    """
    return [int(item) for item in data]