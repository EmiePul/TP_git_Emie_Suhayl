import json
def save_to_json(data,filename):
	with open(filename, 'w') as file:
		json.dump(data,file)

def load_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
