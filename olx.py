import argparse
import sys
import time
from libs.setup import set_up
from libs.search import search_by_id, search_by_css, search_by_xpath, search_all_by_class_name, search_all_by_xpath
from libs.elements import *
from libs.func import create_elements_list


class OlxSearch:

    def __init__(self):
        self.driver = set_up(WEBSITE)

    def initiate_search(self, item_to_search, city_to_search):
        search_by_id(self.driver, COOKIES_BUTTON_ID).click()
        search_by_xpath(self.driver, SEARCH_BAR_ITEM_XPATH).send_keys(item_to_search)
        search_by_css(self.driver, SEARCH_BAR_CITY_CSS).send_keys(city_to_search)
        time.sleep(2)
        search_by_css(self.driver, SEARCH_BUTTON_CSS).click()

    def get_all_items(self):
        item_title = search_all_by_class_name(self.driver, ITEMS_NAME_CLASS_NAME)
        title_list = create_elements_list(item_title, "")

        item_price = search_all_by_xpath(self.driver, ITEM_PRICE_XPATH)
        price_list = create_elements_list(item_price, "do negocjacji")

        item_location = search_all_by_xpath(self.driver, ITEM_LOCATION_XPATH)
        location_list = create_elements_list(item_location, " - .*$")
        return title_list, price_list, location_list

    @staticmethod
    def getOpt(argv):
        parser = argparse.ArgumentParser \
            (usage="python3 olx.py -i '<itme_to_search>' -c '<city_to_search>' [-h]",
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
        helpful.add_argument('-h', action='help', help='Show this help message and exit')
        args = parser.parse_args()
        return args.item, args.city


sss = OlxSearch()
item, city = sss.getOpt(sys.argv[1:])

sss.initiate_search(item_to_search=item, city_to_search=city)
sss.get_all_items()
