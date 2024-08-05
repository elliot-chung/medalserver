from json import load as json_load

def load_data():
    with open('athletes.json') as f:
        athletes = json_load(f)

    country_dict = {}
    count_dict = {}
    for athlete in athletes:
        country_code = athlete['organisation']['code']
        country_desc = athlete['organisation']['description']
        if country_code not in country_dict:
            country_dict[country_code] = country_desc
        count_dict[country_code] = count_dict.get(country_code, 0) + 1

    return country_dict, count_dict


if __name__ == "__main__":
    country_dict, count_dict = load_data()
    print(len(country_dict))
    print(len(count_dict))
    print(country_dict.values())

