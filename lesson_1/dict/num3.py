'''
Дан список стран и городов каждой страны.
Затем даны названия городов.
Russia: Moscow Petersburg Novgorod Kaluga
Ukraine: Kiev Donetsk Odessa

Для каждого города укажите, в какой стране он находится.
Odessa
Moscow
Novgorod
San Francisco
'''
def find_city(city_dict, city):
    for country, city_in_country in city_dict.items():
        if (city in city_in_country):
            return country
    return ("Not found")
def num3():
    city_dict = {"Russia": ["Moscow", "Petersburg", "Novgorod", "Kaluga"],
                 "Ukraine": ["Kiev", "Donetsk", "Odessa"]}
    print(find_city(city_dict, "Odessa"))
    print(find_city(city_dict, "Moscow"))
    print(find_city(city_dict, "Novgorod"))
    print(find_city(city_dict, "San Francisco"))

if __name__ == "__main__":
    num3()


