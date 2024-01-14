def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    lower_index = 0
    higher_index = len(word) - 1

    while lower_index < higher_index:
        if word[lower_index] != word[higher_index]:
            return False
        lower_index += 1
        higher_index -= 1
    return True
