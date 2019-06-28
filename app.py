from results import Results
import requests
import json
from database import Database

Database.initialise(database="election", user="postgres", password="postgresql", host="localhost")

# r = requests.get('https://tiny.cc/hnecdata')
# print(r.status_code)

# with open('results.json','r') as f:
#     data=json.load(f)
#     for p in data:
#         r = Results(str(p['Center Number']),p['Center Name'],p['Valid Votes'],p['id'])
#         # print(p['Center Number'])
#         # print(p['Center Name'])
#         # print(p['Valid Votes'])
#         r.save_to_db()
#         print(r)
r = Results.load_from_db('31001')