import argparse
import sys
import time
from libs.setup import set_up
from libs.search import search_by_id, search_by_css, search_by_xpath, search_all_by_xpath
from libs.elements import *
from libs.func import create_elements_list, create_dictionary, create_database


class OlxSearch:

    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = set_up(WEBSITE)

    def initiate_search(self, item_to_search, city_to_search):
        search_by_id(self.driver, COOKIES_BUTTON_ID).click()
        search_by_xpath(self.driver, SEARCH_BAR_ITEM_XPATH).send_keys(item_to_search)
        search_by_css(self.driver, SEARCH_BAR_CITY_CSS).send_keys(city_to_search)
        time.sleep(2)
        search_by_css(self.driver, SEARCH_BUTTON_CSS).click()

    def get_all_items(self):
        item_title = search_all_by_xpath(self.driver, ITEM_NAME_XPATH)
        title_list = create_elements_list(item_title, "", "textContent")

        item_price = search_all_by_xpath(self.driver, ITEM_PRICE_XPATH)
        price_list = create_elements_list(item_price, "do negocjacji", "textContent")

        item_location = search_all_by_xpath(self.driver, ITEM_LOCATION_XPATH)
        location_list = create_elements_list(item_location, " - .*$", "textContent")

        item_link = search_all_by_xpath(self.driver, ITEM_URL_XPATH)
        urls_list = create_elements_list(item_link, "", "href")
        return title_list, price_list, location_list, urls_list

    def create_dict(self, tlist: list, plist: list, llist: list, ulist: list, given_city, max_value):
        new_dict = {k: v for k, *v in zip(tlist, plist, llist, ulist)}
        # print(new_dict)
        items_dict = create_dictionary(new_dict, given_city, max_value)
        print(f"INFO : There are {len(items_dict)} items matching given requirements:")
        for k, v in items_dict.items(): print(f"{k}: {v}")
        # print(items_dict)
        self.driver.quit()
        return items_dict

    @staticmethod
    def write_to_file(dictionary: dict):
        create_database(dictionary)

    @staticmethod
    def getOpt(argv):
        parser = argparse.ArgumentParser \
            (usage="python3 olx.py -i '<itme_to_search>' -c '<city_to_search>' -v <max_value> [-h]",
             description="Description",
             epilog="© 2022, wiktor.kobiela", prog="OlxAutoSearch",
             add_help=False,
             formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=120, width=250))
        required = parser.add_argument_group('required arguments')
        helpful = parser.add_argument_group('helpful arguments')
        required.add_argument('-i', action='store', dest="item", required=True, metavar="<item_to_search>",
                              help='Provide item name, that should be searched')
        required.add_argument('-c', action='store', dest="city", required=True, metavar="<city_to_search_in>",
                              help='Provide city name, where item should be searched')
        required.add_argument('-v', action='store', dest="value", required=True, metavar="<value>",
                              help='Provide max value of searched item')
        helpful.add_argument('-h', action='help', help='Show this help message and exit')
        args = parser.parse_args()
        return args.item, args.city, args.value


sss = OlxSearch()
item, city, value = sss.getOpt(sys.argv[1:])
sss.start()
sss.initiate_search(item_to_search=item, city_to_search=city)
t_list, p_list, l_list, u_list = sss.get_all_items()
d = sss.create_dict(t_list, p_list, l_list, u_list, city, value)
sss.write_to_file(dictionary=d)