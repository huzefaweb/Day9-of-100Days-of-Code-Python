# Dictionary in lists
travel_log = [{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
}, {
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
}]

def add_new_country(country, visits, cities):
  new_dictionary = {}
  new_dictionary["country"] = country
  new_dictionary["visits"] = visits
  new_dictionary["cities"] = cities
  travel_log.insert(1, new_dictionary)

add_new_country("Russia",2,["moscow","saintpetersburg"])
print(travel_log)
