# Signature
LANGUAGE_OF_OUTPUT = ['Element not found', 'Элемент не найден']
INDEX_ELEMENT = ['Index of element', 'Индекс элемента']

# Language selection
LANG_EN_CODE = 0
LANG_RU_CODE = 1


def linear_search(lst, required_element, language = LANG_EN_CODE):
    """Function for linear search
    input_element - the index of this element we get in the answer
    language    - language of answers, by default English is chosen"""
    index_element = 0
    right_border_of_the_list = len(lst) - 1
    while lst[index_element] != required_element and right_border_of_the_list > index_element:
        index_element += 1
    if lst[index_element] == required_element:
        return INDEX_ELEMENT[language], index_element
    else:
        return LANGUAGE_OF_OUTPUT[language]