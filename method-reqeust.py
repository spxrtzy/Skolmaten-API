TokenID = 'ihb7r118spntm233uo8c'
VersionsID = 'ras27m4w8yjj2'
import json
import os
import requests


with open('urlinfo.json') as f:
    data = json.load(f)
    f.close()

province = data['province']
district = data['district']
school = data['school']

base_url= f'https://skolmaten.se'
connector = f'/api/3/menu/?school={school}&client={TokenID}'



print("[REQ] SENT REQUEST TO", base_url + connector)


send_req = requests.get(base_url + connector)

print(f'[ANS] REQUEST SENT RESPONCE: {send_req}')
print(f'[ANS] REQUEST SENT ANSWER: \n\n{send_req.content} \n')


# Write out

with open('final.json', 'wb') as f:
    f.write(send_req.content)
    f.close()