import csv
import requests

access_token = 'my_token'
query = 'keyword'
center = '27.9506,-82.4572'
distance = 10000

url = f'https://graph.facebook.com/pages/search?q={query}&center={center}&distance={distance}&fields=id,name,location,link&access_token={access_token}'
response = requests.get(url)
response_json = response.json()

if 'error' in response_json:
    print(response_json['error'])
else:
    pages = response_json['data']
    
# Extract the name and email of each page
results = []
for page in pages:
    # Get the page's ID
    page_id = page['id']

    # Get the page's name
    page_name = page['name']

    # Get the page's email (if available)
    try:
        page_email = graph.get_object(id=page_id, fields='emails')['emails'][0]['email']
    except:
        page_email = ''

    # Add the results to the list
    results.append([page_name, page_email])

# Write the results to a CSV file
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email'])
    for result in results:
        writer.writerow(result)