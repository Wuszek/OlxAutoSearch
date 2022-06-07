import os
import re

import catch as catch
import requests


def create_elements_list(items_list: list, elem_to_cut, attribute):
    new_list = []
    for el in items_list:
        string = el.get_attribute(f"{attribute}")
        cut = re.sub(f"{elem_to_cut}", "", str(string))
        new_list.append(cut)
    return new_list


def create_dictionary(given_dictionary: dict, given_city, max_value):
    for key, value in list(given_dictionary.items()):
        int_price_value = re.search(r'(.*?)zł', value[0]).group(1)
        if int(int_price_value.replace(" ", "")) > int(max_value):  # max value entered
            del given_dictionary[key]
        elif f"{given_city}, ".lower() not in value[1].lower():  # city entered
            del given_dictionary[key]
    if not given_dictionary:
        exit("There are no items meeting given requirements.")
    return given_dictionary


def create_database_file():
    if os.path.isfile('data'):
        print("INFO : Database exists.")
    else:
        file = open("data", 'w')
        file.close()
        print("INFO : Created database file.")


def create_database(given_dictionary: dict):
    create_database_file()
    with open("data", 'r+') as file:
        file.seek(0)
        lines = [line.rstrip() for line in file.readlines()]
        print(f"INFO : Database content: {lines}")
        for k, v in list(given_dictionary.items()):
            if v[2] in lines:
                print(f"INFO : {v[2]} already in database.")
                del given_dictionary[k]
            else:
                print(f"INFO : {v[2]} is new!")
                lines.append(v[2])
        if given_dictionary != {}:
            print(f"INFO : New items to send notification: {given_dictionary}")
        else:
            print(f"INFO : No new items (all items from olx already in database).")
        print(f"INFO : Updated database: {lines}")
        while "" in lines:
            lines.remove("")
        file.seek(0)
        file.truncate()
        file.write("\n".join(lines))
    file.close()
    return given_dictionary


def send_notification(new_items: dict, webhook):
    command_list = ""
    for k, v in list(new_items.items()):
        command_list = command_list + f"{k}, {v[0]}, {v[2]}\n"

    payload = {'username': 'OlxBot', "content": ''.join(command_list), "avatar_url": "https://bit.ly/38Uy6Tz"}
    try:
        requests.post(webhook, data=payload)
        print("INFO : Discord message sent successfully.")
    except Exception as e:
        print(f"ERROR : There was an error during sending notification: {e}.")

