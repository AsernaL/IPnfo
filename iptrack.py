import requests
import json
from pip._vendor.colorama import Fore

baner = ('''
  _   _  _                  _       _   
 | | | || |                | |     | |  
 | | | || |_ _ __   ___ ___| | ___ | |_ 
 | | |__   _| '_ \ / __/ _ \ |/ _ \| __|
 | |____| | | | | | (_|  __/ | (_) | |_ 
 |______|_| |_| |_|\___\___|_|\___/ \__|
 ''')                                       
                                        
print(Fore.LIGHTBLUE_EX+baner)

print(Fore.BLUE+'İnstagram = @KnightL4ncelot')
print(Fore.CYAN+'KnihtsOfShadow #Anonymous')

ip_address = input(Fore.CYAN+'Ip/Network Gateway---->')

response = requests.get(f'http://ip-api.com/json/{ip_address}').content

data = json.loads(response)

print(Fore.WHITE+f"""
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

print(Fore.BLUE+"""
Ty For Using K.O.S ip Tracker
This tool made by L4ncelot """)



print(Fore.WHITE+'KnightsOfShadow')
