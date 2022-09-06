# create a random address generator
from random import choice, randint
import datetime


# Names
def random_name_male():
    """ Opens a processed file with male names and returns a name at random."""
    with open('rand_male_names', 'rt') as mn:
        male_names_list = mn.read().splitlines()
        male_name = choice(male_names_list)
        return male_name


def random_name_female():
    """ Opens a processed file with female names and returns a name at random."""
    with open('rand_female_names', 'rt') as fn:
        female_names_list = fn.read().splitlines()
        female_name = choice(female_names_list)
        return female_name


def random_name_lastname():
    """ Opens a processed file with lastnames and returns a name at random."""
    with open('lastnames_1.txt', 'rt') as ln:
        lastnames_list = ln.read().splitlines()
        last_name = choice(lastnames_list)
        return last_name


def random_name():
    """ Returns a male of female name at random 50/50."""
    x = randint(1, 2)
    if x == 1:
        return random_name_male()
    else:
        return random_name_female()


# Address
def random_address():
    """ Opens a processed file with addresses and returns one at random
    with a street number at random."""
    with open('address.txt', 'rt') as a:
        address_list = a.read().splitlines()

    number = randint(1, 149)
    street = choice(address_list)
    address = street + " " + str(number)
    return address


# City
def random_city():
    """ Returns a random city from a list."""
    city_list = ['Rotterdam', 'Amsterdam', 'Den Haag', 'Groningen', 'Maastricht', 'Utrecht']
    city = choice(city_list)
    return city


# Postal codes
def random_postal_code():
    """ Creates a postal code at random and return the result."""
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_code = [x for x in alfabet]
    first_part = randint(1000, 9999)
    second_part = choice(letter_code) + choice(letter_code)
    postal_code = str(first_part) + ' ' + second_part
    return postal_code


# Phone numbers
def random_phone_number():
    """ Creates a random phone number and returns it."""
    first_part = '06-'
    second_part = ''
    for i in range(8):
        digit = str(randint(0, 9))
        second_part = second_part + digit
    phone_number = first_part + second_part
    return phone_number


# OOP date
class Date:
    def __init__(self, start_year: int, end_year: int):
        self.start_year = start_year
        self.end_year = end_year

    def generate(self):
        """ Generates a random date. Returns it in the chosen format."""
        year = randint(self.start_year, self.end_year)
        month = randint(1, 12)
        day = randint(1, 31)
        birthdate = datetime.date(year, month, day)
        return birthdate.strftime("%d-%m-%Y")

    def random_date(self):
        """ Returns a valid random date. Checks for value errors (leap day,
         correct days in the month) and returns a set date."""
        try:
            return generate_date(self.start_year, self.end_year)
        except ValueError:
            dt = datetime.date(self.start_year, 8, 1)
            return dt.strftime("%d-%m-%Y")


# Date
def generate_date(start_year, end_year):
    """ Generates a random date. Returns it in the chosen format."""
    year = randint(start_year, end_year)
    month = randint(1, 12)
    day = randint(1, 31)
    birthdate = datetime.date(year, month, day)
    return birthdate.strftime("%d-%m-%Y")


def random_date(start_year, end_year):
    """ Returns a valid random date. Checks for value errors (leap day,
     correct days in the month) and returns a set date."""
    try:
        return generate_date(start_year, end_year)
    except ValueError:
        dt = datetime.date(start_year, 8, 1)
        return dt.strftime("%d-%m-%Y")


# Processing
def reduce_names_to_75():
    """ Process a file and reduce the names to a maximum of 75."""
    # change male and female string doc
    with open('female.txt', 'rt') as m:
        content = m.readlines()
        print(len(content))
        print(content)

        for i in range(25):
            x = randint(0, len(content))
            content.pop(x)

        print(len(content))
        print(content)

    # random_male_names
    for items in content:
        with open('rand_female_names', 'at') as rm:
            rm.write(items)


def lastnames_cleanup():
    """ Processes the raw lastnames document and return a txt file with 100 lastnames"""
    # lastname file cleanup
    with open('lastnames.txt', 'rt') as ln:
        content = ln.read().splitlines()
        print(len(content))

        process_content = []
        for lines in content:
            char = lines[0]
            if char.isdigit():
                # print(lines)
                process_content.append(lines.split())

        # print(process_content)
        lastnames = []
        for items in process_content:
            if items[1] == 'De' or items[1] == 'Van':
                x = items[1].strip('/') + ' ' + items[2].strip('/')
                lastnames.append(x + '\n')
            else:
                y = items[1].strip('/')
                lastnames.append(y + '\n')

        print(len(lastnames))
        print(lastnames)

        for items in lastnames:
            print(items)
            with open('lastnames_1.txt', 'at') as rm:
                rm.write(items)


if __name__ == '__main__':
    # print examples
    # for r in range(11):
    #     print(random_name(), random_name_lastname())
    #     print(random_date(2009, 2010))  # 12-13 year olds
    #     print(random_address())
    #     print(random_city())
    #     print(random_postal_code())
    #     print(random_phone_number())
    #     print()
    #     pass

    A1 = Date(2009, 2010)
    B3 = Date(2007, 2008)
    birthdate = B3.random_date()

    print(A1.random_date())
    print(birthdate)

