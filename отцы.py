def fathers_sorted_and_search():
    fathers = {'Harold Abelson': 'Logo', 'Kenneth Eugene Iverson': 'APL', 'Andrei Alexandrescu': 'C++',
               'Alfred Vaino Aho': 'AWK', 'Guido Van Rossum': 'Python', 'Jeremy Ashkenas': 'CoffeeScript',
               'Walter Bright': 'D', 'John George Kemeny': 'Basic', 'Peter Naur': 'Algol', 'Don Syme': 'F#',
               'Rasmus Lerdorf': 'php', 'Larry Wall': 'perl', 'Brian Kernighan': 'awk', 'James Gosling': 'java',
               'Simon Cozens': 'parrot'}
    choice = input('Sorted or Search?')
    if choice == 'Sorted':
        sorted_fathers = sorted(fathers.keys())
        for index in sorted_fathers:
            print(index, ":", fathers[index])
    elif choice == 'Search':
        search_father = input("Who you looking for? Enter a name:")
        for name, value in fathers.items():
            if name == search_father:
                print(search_father, 'Develop', fathers[name])
                break
            else:
                print("Could not find this man")
    else:
        print('Try again')


print(fathers_sorted_and_search())