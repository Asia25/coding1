# Constant for switching debug and release mode

DEBUG_MODE = True



# Constant strings for debugging

DEBUG_MSG_INPUT_LIST = ["Input list: ", "Исходный список: "]

DEBUG_MSG_OUTPUT_LIST = ["Output list: ", "Отсортированный список: "]



# Language selection

LANG_EN_CODE = 0

LANG_RU_CODE = 1





def bubble_sort(list1, language=LANG_EN_CODE):

    """Function for sorting list by bubble

    list1 - input list for sorting

    language    - language of debug messages, by default English is chosen"""

    index = 1

    if DEBUG_MODE:

        print(DEBUG_MSG_INPUT_LIST[language], list1)

    while index < len(list1):

        for first_index in range(len(list1) - index):

            if list1[first_index] > list1[first_index + 1]:

                list1[first_index], list1[first_index + 1] = list1[first_index + 1], list1[first_index]

        index += 1

    if DEBUG_MODE:

        print(DEBUG_MSG_OUTPUT_LIST[language], list1)

    return list1





print(bubble_sort([10, 6, 8, 9, 76]))

