import requests.api
import json
from pip._vendor.colorama import Fore

print(Fore.MAGENTA+'      ▄▄▄        ██████ ▓█████  ██▀███   ███▄    █  ▄▄▄       ██▓     ')
print(Fore.MAGENTA+'     ▒████▄    ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒ ██ ▀█   █ ▒████▄    ▓██▒     ')
print(Fore.MAGENTA+'     ▒██  ▀█▄  ░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██  ▀█▄  ▒██░     ')
print(Fore.MAGENTA+'     ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░     ')
print(Fore.MAGENTA+'      ▓█   ▓██▒▒██████▒▒░▒████▒░██▓ ▒██▒▒██░   ▓██░ ▓█   ▓██▒░██████▒ ')
print(Fore.MAGENTA+'      ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░ ')
print(Fore.MAGENTA+'       ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░ ')
print(Fore.MAGENTA+'       ░   ▒   ░  ░  ░     ░     ░░   ░    ░   ░ ░   ░   ▒     ░ ░    ')
print(Fore.MAGENTA+'           ░  ░      ░     ░  ░   ░              ░       ░  ░    ░  ░ ')
print(Fore.MAGENTA+'                                                                      ')
print(Fore.MAGENTA+'      ▄▄▄▄   ▓█████  ██▀███   ██ ▄█▀▓█████   ██████  █     █░▒███████▒')
print(Fore.MAGENTA+'     ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒ ██▄█▒ ▓█   ▀ ▒██    ▒ ▓█░ █ ░█░▒ ▒ ▒ ▄▀░')
print(Fore.MAGENTA+'     ▒██▒ ▄██▒███   ▓██ ░▄█ ▒▓███▄░ ▒███   ░ ▓██▄   ▒█░ █ ░█ ░ ▒ ▄▀▒░   ')
print(Fore.MAGENTA+'     ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▓██ █▄ ▒▓█  ▄   ▒   ██▒░█░ █ ░█   ▄▀▒   ░')
print(Fore.MAGENTA+'     ░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██▒ █▄░▒████▒▒██████▒▒░░██▒██▓ ▒███████▒')
print(Fore.MAGENTA+'     ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░▒▒ ▓░▒░▒')
print(Fore.MAGENTA+'     ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒ ▒░ ░ ░  ░░ ░▒  ░ ░  ▒ ░ ░  ░░▒ ▒ ░ ▒')
print(Fore.MAGENTA+'      ░    ░    ░     ░░   ░ ░ ░░ ░    ░   ░  ░  ░    ░   ░  ░ ░ ░ ░ ░')
print(Fore.MAGENTA+'      ░         ░  ░   ░     ░  ░      ░  ░      ░      ░      ░ ░    ')
print(Fore.MAGENTA+'           ░                                                 ░        ')

print(Fore.YELLOW+'İnstagram = @Berkeswz')
print(Fore.YELLOW+'Team = Black Cyber Team')

ip_address = input(Fore.MAGENTA+'Ip/Network Gateway---->')

response = requests.get(f'http://ip-api.com/json/{ip_address}').content

data = json.loads(response)

print(f"""
IP = {data['query']}
Country = {data['country']}
City = {data['city']}
ZIP = {data['zip']}
ISP = {data['isp']}
Lon = {data['lon']}
Lat = {data['lat']}
Location = {data['lat']},{data['lon']}
Countrycode = {data['countryCode']}
Region = {data['region']} 
Timezone = {data['timezone']}
As = {data['as']}
""")

print(Fore.MAGENTA+"""
Ty For Using AsernaL ? ip Tracker
This tool made by Berkeswz """)

print('Follow on instagram')

print(Fore.YELLOW+""" 
@berkeswz
@qwenzyreal
""")

print(Fore.RED+'////Black Cyber Team////')