import requests
import json
import csv

headers = {
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"144e7b-i6YQnBoCxwlWsLRQd4H2brMbueA"',
    'origin': 'https://martechtribedata-vendor-eu.ey.r.appspot.com',
    'referer': 'https://martechtribedata-vendor-eu.ey.r.appspot.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'Cache-Control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

first_response = requests.get('https://martechtribedata-server-eu.ey.r.appspot.com/firstsubcat', headers=headers)
second_response = requests.get('https://martechtribedata-server-eu.ey.r.appspot.com/secondsubcat', headers=headers)
first_response_json = json.loads(first_response.text)
second_response_json = json.loads(second_response.text)

with open('companies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Vendor Name', 'Employees', 'Revenue Range', 'URL'])
    
    for response_data in first_response_json:
        writer.writerow([
                response_data["vendor_name"],
                response_data["employees"],
                response_data["revenue_range"],
                response_data["url"]
            ])
        print(response_data["vendor_name"],response_data["employees"], response_data["revenue_range"], response_data["url"])
    
    for response_data in second_response_json:
        writer.writerow([
                response_data["vendor_name"],
                response_data["employees"],
                response_data["revenue_range"],
                response_data["url"]
            ])
        print(response_data["vendor_name"],response_data["employees"], response_data["revenue_range"], response_data["url"])

