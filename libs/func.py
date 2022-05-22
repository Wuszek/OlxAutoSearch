import re


def create_elements_list(items_list: list, elem_to_cut):
    new_list = []
    for el in items_list:
        string = el.get_attribute("textContent")
        cut = re.sub(f"{elem_to_cut}", "", string)
        new_list.append(cut)
    print(new_list)
    return new_list
