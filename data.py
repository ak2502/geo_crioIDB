import json  
import pandas as pd  
from pandas.io.json import json_normalize  
import requests
from tabulate import tabulate

data = [{"title":"Dharamraj","id":"here:pds:place:356te7ug-aab7da0959a549568e2d5367360ac2f8","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Dharamraj, Hare Krishna Road, Powai, Mumbai 400076, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Powai","street":"Hare Krishna Road","postalCode":"400076"},"position":{"lat":19.12548,"lng":72.91935},"access":[{"lat":19.12545,"lng":72.91935}],"distance":1086,"categories":[{"id":"700-7200-0324","name":"Послуги з оренди житла","primary":True}]},{"title":"Pajasa Apartments","id":"here:pds:place:356te7ug-2d6f7d8713484a3c822ff16d259a3672","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Pajasa Apartments, Central Avenue, Hiranandani, Powai, Mumbai 400076, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Powai","subdistrict":"Hiranandani","street":"Central Avenue","postalCode":"400076"},"position":{"lat":19.12339,"lng":72.91274},"access":[{"lat":19.12339,"lng":72.91274}],"distance":1115,"categories":[{"id":"700-7200-0324","name":"Послуги з оренди житла","primary":True}],"contacts":[{"phone":[{"value":"+912269999891"}],"www":[{"value":"https://www.pajasaapartments.co.in"}]}]},{"title":"Scorpio House","id":"here:pds:place:356te7ug-3fc1a164b55c7471dfef61d914495aa7","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Scorpio House, Central Avenue, Hiranandani, Powai, Mumbai 400076, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Powai","subdistrict":"Hiranandani","street":"Central Avenue","postalCode":"400076"},"position":{"lat":19.11933,"lng":72.91227},"access":[{"lat":19.11933,"lng":72.91227}],"distance":1568,"categories":[{"id":"700-7200-0324","name":"Послуги з оренди житла","primary":True}]},{"title":"Oritel Service Apartments","id":"here:pds:place:356te7ud-fff70785b3144b2eb60a36923532bd01","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Oritel Service Apartments, 36-2, Chandivali, Powai, Mumbai 400072, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Powai","subdistrict":"Chandivali","postalCode":"400072","houseNumber":"36-2"},"position":{"lat":19.11098,"lng":72.89882},"access":[{"lat":19.111,"lng":72.89867}],"distance":2920,"categories":[{"id":"500-5000-0000","name":"Готель або мотель","primary":True},{"id":"500-5000-0053","name":"Готелі"},{"id":"500-5100-0000","name":"Житло"},{"id":"700-7200-0324","name":"Послуги з оренди житла"}],"references":[{"supplier":{"id":"tripadvisor"},"id":"1135613"}],"contacts":[{"phone":[{"value":"+912228475656"},{"value":"+917208080719","categories":[{"id":"500-5100-0000"}]},{"value":"+919820977731","categories":[{"id":"500-5000-0000"}]}],"mobile":[{"value":"+917208080719","categories":[{"id":"500-5100-0000"}]}],"www":[{"value":"http://www.oritel.biz","categories":[{"id":"500-5000-0000"},{"id":"500-5000-0053"},{"id":"700-7200-0324"}]},{"value":"https://www.business.site","categories":[{"id":"500-5100-0000"}]}]}],"openingHours":[{"categories":[{"id":"500-5000-0000"}],"text":["Mon-Sun: 00:00 - 24:00"],"isOpen":True,"structured":[{"start":"T000000","duration":"PT24H00M","recurrence":"FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA,SU"}]}]},{"title":"Silverline Apartment","id":"here:pds:place:356te7uf-0a7baeff179d49fd860e8d3902946ac3","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Silverline Apartment, Marol, Andheri East, Mumbai 400059, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Andheri East","subdistrict":"Marol","postalCode":"400059"},"position":{"lat":19.12057,"lng":72.88556},"access":[{"lat":19.12066,"lng":72.88535}],"distance":3245,"categories":[{"id":"900-9300-0221","name":"Житловий будинок","primary":True},{"id":"700-7200-0324","name":"Послуги з оренди житла"}]},{"title":"Andheri East Service Apartments","id":"here:pds:place:356te7uf-0d5db6077151dcd23696918063140033","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Andheri East Service Apartments, Marol, Andheri East, Mumbai 400059, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Andheri East","subdistrict":"Marol","postalCode":"400059"},"position":{"lat":19.11746,"lng":72.88374},"access":[{"lat":19.11746,"lng":72.88374}],"distance":3576,"categories":[{"id":"700-7200-0324","name":"Послуги з оренди житла","primary":True}],"contacts":[{"phone":[{"value":"+919820049408"}],"www":[{"value":"http://www.servicedapartmentsmumbai.com/?s&search=1&post_type=estate&location=marol-andheri-east&term"}]}]},{"title":"Aghadi Nagar Chs","id":"here:pds:place:356te7v5-ea19989e14a440f9b8386569ef29849e","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Aghadi Nagar Chs, Bhandup West, Mumbai 400078, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Bhandup West","postalCode":"400078"},"position":{"lat":19.16275,"lng":72.93285},"access":[{"lat":19.16289,"lng":72.93285}],"distance":3856,"categories":[{"id":"700-7200-0324","name":"Послуги з оренди житла","primary":True}],"contacts":[{"mobile":[{"value":"+919324060902"}]}]},{"title":"Eden Guest House","id":"here:pds:place:356jx7ps-5ebe0762091400064d11e6140c9dfde8","ontologyId":"here:cm:ontology:apartment_rental_flat_rental","resultType":"place","address":{"label":"Eden Guest House, 703 Marol Maroshi Road, Marol, Andheri East, Mumbai 400059, India","countryCode":"IND","countryName":"India","stateCode":"MH","state":"Maharashtra","county":"Mumbai Suburban","city":"Mumbai","district":"Andheri East","subdistrict":"Marol","street":"Marol Maroshi Road","postalCode":"400059","houseNumber":"703"},"position":{"lat":19.11748,"lng":72.88025},"access":[{"lat":19.11749,"lng":72.88007}],"distance":3897,"categories":[{"id":"500-5100-0057","name":"Гостьовий будинок","primary":True},{"id":"500-5000-0000","name":"Готель або мотель"},{"id":"500-5000-0053","name":"Готелі"},{"id":"500-5100-0059","name":"Туристична база"},{"id":"700-7200-0324","name":"Послуги з оренди житла"}],"references":[{"supplier":{"id":"core"},"id":"1115429174"},{"supplier":{"id":"core"},"id":"1200967164"},{"supplier":{"id":"core"},"id":"1204946123"}],"contacts":[{"phone":[{"value":"+912229201900"},{"value":"+912238550971","categories":[{"id":"500-5000-0000"},{"id":"500-5100-0059"}]},{"value":"+918004916126","categories":[{"id":"500-5000-0000"}]},{"value":"+919820886610","categories":[{"id":"500-5000-0000"}]}],"mobile":[{"value":"+919820886610","categories":[{"id":"500-5000-0053"},{"id":"500-5100-0057"}]}],"fax":[{"value":"\"\"","categories":[{"id":"500-5000-0000"},{"id":"500-5100-0059"}]}],"www":[{"value":"http://edenguesthouse.co.in"},{"value":"http://www.hoteleden.co.in","categories":[{"id":"500-5000-0000"}]}],"email":[{"value":"abdulla@edenguesthouse.co.in","categories":[{"id":"500-5000-0000"}]}]}]}]

d=json_normalize(data)

d2=d[['title','address.label','distance','access','position.lat','position.lng','address.postalCode','contacts','id']]

d.to_csv('apartment.csv')
d2.to_csv('cleaned_apartment.csv')

df_final=d2[['position.lat','position.lng']]

CafeList=[]
DepList=[]
GymList=[]
latitudes = list(d2['position.lat'])
longitudes = list( d2['position.lng'])
for lat, lng in zip(latitudes, longitudes):    
    radius = '1000' #Set the radius to 500 metres
    latitude=lat
    longitude=lng
    
    search_query = 'cafe' #Search for any cafes
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    CafeList.append(venues['title'].count())
	
    search_query = 'gym' #Search for any gyms
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    GymList.append(venues['title'].count())

    search_query = 'department-store' #search for supermarkets
    url = 'https://discover.search.hereapi.com/v1/discover?in=circle:{},{};r={}&q={}&apiKey=uJHMEjeagmFGldXp661-pDMf4R-PxvWIu7I68UjYC5Q'.format(latitude, longitude, radius, search_query)
    results = requests.get(url).json()
    venues=json_normalize(results['items'])
    DepList.append(venues['title'].count())

df_final['Cafes'] = CafeList
df_final['Department Stores'] = DepList
df_final['Gyms'] = GymList

print(tabulate(df_final,headers='keys',tablefmt='github'))
