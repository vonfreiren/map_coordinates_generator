import json

from geopy.geocoders import Nominatim


def retrieve_coordinates(city, country, zip):
    address = None
    if zip is not None and zip != '':
        location = f'{zip}, {country}'

        address = geolocator.geocode(location)

    if address is None:
        location = f'{city}, {country}'
        address = geolocator.geocode(location)

    latitude = address.latitude
    longitude = address.longitude

    return latitude, longitude

geolocator = Nominatim(user_agent="http")

list_companies = []

with open('Finance.Company_Info.json') as file:
    # Load the JSON data
    data = json.load(file)
    for company in data:
        try:
            city = company['city']
            country = company['country']
            zip = company['zip']

            latitude, longitude = retrieve_coordinates(city, country, zip)

            company['latitude'] = latitude
            company['longitude'] = longitude
            company['name'] = company['shortName'] if 'shortName' in company else company['longName']
            list_companies.append(company)
        except:
            print("error " + company['ticker'])

    with open('Finance.Company_Info_New.json', 'w') as outfile:
        json.dump(list_companies, outfile)







# Use the format "zipcode, country" for better accuracy




