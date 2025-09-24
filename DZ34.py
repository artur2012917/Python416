import csv

data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3570',
    'vendor': 'Cisco'
},
{
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
},
{
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
},
{
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open("dict_writer.csv", "w", encoding='utf-8') as f:
    writer = csv.DictWriter(f, delimiter=",", lineterminator='\n', fieldnames=data[0].keys())
    writer.writeheader()
    for d in data:
        writer.writerow(d)

