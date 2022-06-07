# OlxAutoSearch

## How to run
You need to have python3 installed to run this script. Refer to [python website](https://www.python.org/downloads/).

#### Install google-chrome
Ubuntu
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
Windows:

Go to https://www.google.com/chrome/ and install Chrome

#### Clone repo
```bash
git clone https://git.kobiela.click/wiktor.kobiela/OlxAutoSearch.git
cd OlxAutoSearch
```
#### Create and activate venv
```bash
mkdir venv
python3 -m venv venv/
source venv/bin/activate
```
#### Install requirements
```bash
python3 -m pip install -r requirements.txt
```
#### Run the script
```bash
python3 olx.py -h
usage: python3 olx.py -i "item_to_search" -c "city_to_search" -v max_value [-w "webhook_url" ] [-h]

Description

required arguments:
  -i "item_to_search"     Provide item name, that should be searched
  -c "city_to_search_in"  Provide city name, where item should be searched
  -v <value>              Provide max value of searched item

optional arguments:
  -w "webhook_url"        Provide discord webhook url - default notifications are off.

helpful arguments:
  -h                      Show this help message and exit

© 2022, wiktor.kobiela
```
#### Example usage: 
Search IKEA MICKE in Gdańsk city for less than 300 and send notification about new items.
```bash
python3 olx.py -i "IKEA MICKE" -c "Gdańsk" -v 300 -w "https://discord.com/api/webhooks/privatewebhook"
```