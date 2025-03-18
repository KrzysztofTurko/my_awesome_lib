def reverse_text(text):
    """
    Odwraca podany tekst.
    
    :param text: Tekst do odwrócenia.
    :return: Odwrócony tekst.
    """
    return text[::-1]

def remove_duplicates(words):
    """
    Usuwa duplikaty z listy słów.
    
    :param words: Lista słów.
    :return: Lista słów bez duplikatów.
    """
    return list(set(words))