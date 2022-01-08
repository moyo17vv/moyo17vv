import phonenumbers
from geopy.geocoders import Nominatim
from phonenumbers import carrier, geocoder

def numchecker(phone):
   info = []
   numero = phonenumbers.parse(phone)
   info.append(geocoder.description_for_number(numero, "es"))
   info.append(carrier.name_for_number(numero, "es"))
   return info

phone = input("Digite un numero de telefono:")
print (numchecker(phone))
