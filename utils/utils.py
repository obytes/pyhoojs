def write_to_file(file_name, json_data):
    import json
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile)


def load_users_from_csv(file_name='input.csv'):
    import csv
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return reader
