import json
from datetime import datetime

from nugget import Nugget

#passaggio a dizionario al posto della lista

def convert_to_list_str(nuggets: list[Nugget]):
    nuggets_str = []
    for nugget in nuggets:
        nuggets_str.append({
            'ID': nugget.id,
            "Q": nugget.question,
            "A": nugget.answer,
            "Link": nugget.link,
            "L": nugget.last_execution.isoformat(),
        })
    return nuggets_str


def load_nuggets_from_json()->list[Nugget]:
    with open("data.json", "r") as file:
        culture_nuggets=json.load(file)

    nuggets=[]

    for nugget in culture_nuggets:
        id=nugget["ID"]
        question=nugget["Q"]
        answer=nugget["A"]
        link=nugget["Link"]
        last_execution_str=nugget["L"]
        last_execution=datetime.fromisoformat(last_execution_str)
        nuggets.append(Nugget(id,question,answer,link,last_execution))

    return nuggets


def save_nugget_to_json(culture_nuggets: list[Nugget]):
    nuggets_str=convert_to_list_str(culture_nuggets)
    with open("data.json", "w") as file:
        json.dump(nuggets_str, file)

