import json

def saveConfig(data):
    configJson = json.dumps(data)
    with open('config.json', 'w') as f:
        f.write(configJson)
        f.close()


def readConfig():
    with open('config.json', 'r') as f:
        jsonData = json.load(f)
        return jsonData