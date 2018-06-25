# Constant for switching debug and release mode

DEBUG_MODE = False



# Language selection

LANG_EN_CODE = 0

LANG_RU_CODE = 1



# Constant strings for debugging

DEBUG_MSG_INPUT_LIST = ["Input list: ", "Исходный список: "]

DEBUG_MSG_OUTPUT_LIST = ["Output list: ", "Отсортированный список: "]





def sort_by_selection(sorted_list, language = LANG_EN_CODE):

    """Function for sorting list by selection

    sorted_list - input list for sorting

    language    - language of debug messages, by default English is chosen"""

    if DEBUG_MODE: print(DEBUG_MSG_INPUT_LIST[language], sorted_list)

    lst = sorted_list

    comparing_element_index = 0

    while comparing_element_index < len(lst) - 1:

        start_frame_index = comparing_element_index

        for i in range(comparing_element_index + 1, len(lst)):

            if lst[i] < lst[start_frame_index]:

                start_frame_index = i

        buffer_element = lst[comparing_element_index]

        lst[comparing_element_index] = lst[start_frame_index]

        lst[start_frame_index] = buffer_element

        comparing_element_index += 1

    if DEBUG_MODE: print(DEBUG_MSG_OUTPUT_LIST[language], lst)

    return lst