"""
this is the fetch request written in javascript

fetch("https://api.msn.com/sports/leaguemedalstandings?apikey=kO1dI4ptCTTylLkPL1ZTHYP8JhLKb8mRDoA5yotmNJ&version=1.0&cm=en-us&tzoffset=-7&user=m-0343F8C1AC8362723E9DEC70AD7863AD&activityId=DDA83F3A-70B7-4505-87B0-BA70D7CE0AD0&ocid=sports-league-medals&it=edgeid&scn=APP_ANON&leagueid=SummerOlympics_SummerOlympics&count=50", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-ms-gec": "0253CF44C48B4E2AFD5E78F1FFD27FC4E96B28CE79E8FEB89709F2A9D66C6C98",
    "sec-ms-gec-version": "1-127.0.2651.74",
    "x-client-data": "eyIxIjoiMCIsIjEwIjoiXCJYM0E0STRtRjk3a0RhbVdLenhDeTJBV2Q1bjVtVFd6V3RTK29LaXhocHNBPVwiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiItMjI4OTM1MzcwMzM2MTUxOTc3MCIsIjUiOiJcImFaYWU2dUpKbzBsenQwc2JPSkxIOTNoWkV6ejFHQXRjZkpwL2NHNnNqVmc9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjYwMTI5NTQyMTQ1IiwiOSI6ImRlc2t0b3AifQ==",
    "x-edge-shopping-flag": "1"
  },
  "referrer": "https://www.msn.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
})
"""

# the following is the python code to fetch the data
from urllib.parse import urlencode
from urllib3 import request
from json import loads as json_loads

def fetch_data(retries=3):
  endpoint = "https://api.msn.com/sports/leaguemedalstandings"
  
  params = {
    'apikey': 'kO1dI4ptCTTylLkPL1ZTHYP8JhLKb8mRDoA5yotmNJ',
    'version': '1.0',
    'cm': 'en-us',
    'tzoffset': '-7',
    'user': 'm-0343F8C1AC8362723E9DEC70AD7863AD',
    'activityId': 'DDA83F3A-70B7-4505-87B0-BA70D7CE0AD0',
    'ocid': 'sports-league-medals',
    'it': 'edgeid',
    'scn': 'APP_ANON',
    'leagueid': 'SummerOlympics_SummerOlympics',
    'count': '1000'
  }

  params = urlencode(params)
  url = endpoint + "?" + params

  headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'priority': 'u=1, i',
      'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'sec-ms-gec': '0253CF44C48B4E2AFD5E78F1FFD27FC4E96B28CE79E8FEB89709F2A9D66C6C98',
      'sec-ms-gec-version': '1-127.0.2651.74',
      'x-client-data': 'eyIxIjoiMCIsIjEwIjoiXCJYM0E0STRtRjk3a0RhbVdLenhDeTJBV2Q1bjVtVFd6V3RTK29LaXhocHNBPVwiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiItMjI4OTM1MzcwMzM2MTUxOTc3MCIsIjUiOiJcImFaYWU2dUpKbzBsenQwc2JPSkxIOTNoWkV6ejFHQXRjZkpwL2NHNnNqVmc9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjYwMTI5NTQyMTQ1IiwiOSI6ImRlc2t0b3AifQ==',
      'x-edge-shopping-flag': '1'
  }


  while retries > 0:
    try:
      retries -= 1
      resp = request("GET", url, headers=headers)
      data = json_loads(resp.data)
    except Exception as e:
      print(e)
      continue
    else:
      break
  if retries == 0: raise Exception("Failed to fetch data")
  data = data['value'][0]['medalStandings']
  return data

if __name__ == "__main__":
  data = fetch_data()
  print(data[0])


