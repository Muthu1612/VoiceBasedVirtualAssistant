import json


msg="bbbbbbbc"
ans="bbbbbbbbbxxxxxx"
rand="bbbbbbbbbxxxxxxa"
temp_dict=            {"tag": int,
        "patterns": [msg],
        "responses": [ans],
        "context": [""]
        }


data_file = open('intents.json').read()
intents2 = json.loads(data_file)
temp_dict=            {"tag": [rand],
"patterns": [msg],
"responses": [ans],
"context": [""]
}
intents2['intents'].append(temp_dict)
with open('intents.json', 'w') as json_file:
    json.dump(intents2, json_file)