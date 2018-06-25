import SortBySelection



# Signature

OUTPUT_LIST = ["Output list: ", "Отсортированный список: "]

LANGUAGE_OF_OUTPUT = ['Element not found', 'Элемент не найден']

INDEX_ELEMENT = ['Index of element', 'Индекс элемента']



# Language selection

LANG_EN_CODE = 0

LANG_RU_CODE = 1





def binary_search(input_list, required_element, language = LANG_EN_CODE):

    """Function for binary search

    required_element - the index of this element we get in the answer

    language    - language of answers, by default English is chosen"""

    element = required_element

    lst = SortBySelection.sort_by_selection(input_list)

    print(OUTPUT_LIST[language], lst)

    left_border_list = 0

    right_border_list = len(lst)

    while left_border_list < right_border_list - 1:

        middle_list = (left_border_list + right_border_list) // 2

        if lst[middle_list] > element:

            right_border_list = middle_list

        else:

            left_border_list = middle_list

    if lst[left_border_list] == element:

        return INDEX_ELEMENT[language], left_border_list

    elif lst[right_border_list] != element:

        return LANGUAGE_OF_OUTPUT[language]

    else:

        return INDEX_ELEMENT[language], right_border_list