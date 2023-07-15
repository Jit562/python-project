import phonenumbers

from phonenumbers import timezone, geocoder, carrier

number = input("enter number:  +91   ")

num = phonenumbers.parse(number)

time = timezone.time_zones_for_number(num)

car = carrier.name_for_number(num,"en")

ged = geocoder.description_for_number(num,"en")

print(num)
print(time)
print(car)
print(ged)

