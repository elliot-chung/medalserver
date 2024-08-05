import medal_fetch
import athletes
from operator import itemgetter
from typing import List, Tuple

data_type = List[Tuple[str, float, float, float, float, int]]

def medals_per_100_athletes() -> data_type:
    epsilon = 0.00001
    output = []
    try:
        medal_data = medal_fetch.fetch_data()
    except Exception as e:
        print(e)
        return ["ERROR FETCHING DATA"]
    country_dict, count_dict = athletes.load_data()

    
    # 'AIN' team is missing from the medal data
    # AIN is the country for Belarus and Russia since both country's athletes have been banned from the Olympics due to doping (and the Russian war on Ukraine)
    # The latter reason seems to be the reason why microsoft is not reporting the medal data for AIN
    for medal_result in medal_data:
        bronze_count = medal_result['medalsWon']['Bronze']
        silver_count = medal_result['medalsWon']['Silver']
        gold_count = medal_result['medalsWon']['Gold']
        total_count = medal_result['medalsWon']['Total']

        bronze_count = bronze_count if bronze_count > 0 else epsilon
        silver_count = silver_count if silver_count > 0 else epsilon
        gold_count = gold_count if gold_count > 0 else epsilon
        total_count = total_count if total_count > 0 else epsilon
        
        country_key = medal_result['team']['shortName']['rawName']
        athlete_count = count_dict.get(country_key, 1)
        country_name = country_dict.get(country_key, 'Unknown')

        bronze_per_athlete = bronze_count / athlete_count
        silver_per_athlete = silver_count / athlete_count
        gold_per_athlete = gold_count / athlete_count
        total_per_athlete = total_count / athlete_count

        bronze_per_100 = bronze_per_athlete * 100
        silver_per_100 = silver_per_athlete * 100
        gold_per_100 = gold_per_athlete * 100
        total_per_100 = total_per_athlete * 100

        item = (country_name, bronze_per_100, bronze_count, silver_per_100, silver_count, gold_per_100, gold_count, total_per_100, total_count, athlete_count)
        output.append(item)
    return output



if __name__ == "__main__":
    data = medals_per_100_athletes()
    data = sorted(data, key=itemgetter(4), reverse=True)
    output = [f"{name}: {bronze:.2f}, {silver:.2f}, {gold:.2f}, {total:.2f} ({athletes})" for name, bronze, silver, gold, total, athletes in data]
    print("\n".join(output))

    