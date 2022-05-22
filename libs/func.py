import re


def create_elements_list(items_list: list, elem_to_cut, attribute):
    new_list = []
    for el in items_list:
        string = el.get_attribute(f"{attribute}")
        cut = re.sub(f"{elem_to_cut}", "", str(string))
        new_list.append(cut)
    # print(new_list)
    return new_list


def create_dictionary(given_dictionary: dict, given_city, max_value):
    for key, value in list(given_dictionary.items()):
        int_price_value = re.search(r'(.*?)zł', value[0]).group(1)
        if int(int_price_value.replace(" ", "")) > int(max_value):  # max value entered
            # print(value[0][:-3])
            del given_dictionary[key]
        elif f"{given_city}, ".lower() not in value[1].lower():  # city entered
            # print(value[1])
            del given_dictionary[key]
    if not given_dictionary:
        exit("There are no items meeting given requirements.")
    return given_dictionary

