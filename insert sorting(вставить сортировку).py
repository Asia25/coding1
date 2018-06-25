# Constant for switching debug and release mode
DEBUG_MODE = True

# Constant strings for debugging
DEBUG_MSG_INPUT_LIST = ["Input list: ", "Исходный список: "]
DEBUG_MSG_OUTPUT_LIST = ["Output list: ", "Отсортированный список: "]

# Language selection
LANG_EN_CODE = 0
LANG_RU_CODE = 1


def insert_sorting(lst, language = LANG_EN_CODE):
    """Function for sorting list by insert
    lst - input list for sorting
    language    - language of debug messages, by default English is chosen"""
    if DEBUG_MODE: print(DEBUG_MSG_INPUT_LIST[language], lst)
    for first_index in range(1, len(lst)):
        value = lst[first_index]
        second_index = first_index - 1
        while second_index >= 0 and lst[second_index] > value:
            lst[second_index + 1] = lst[second_index]
            second_index = second_index - 1
        lst[second_index + 1] = value
    if DEBUG_MODE: print(DEBUG_MSG_OUTPUT_LIST[language], lst)
    return lst


print(insert_sorting([10, 23, 45, 3, 2, 45], 0))