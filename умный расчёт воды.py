def smart_water_calculation(time_in_the_shower):

    number_of_water_bottles_per_minute = 12

    if time_in_the_shower < 0:

        return 'Enter positive number!!!'

    else:

        number_of_bottles = time_in_the_shower * number_of_water_bottles_per_minute

        return number_of_bottles





print(smart_water_calculation(30))