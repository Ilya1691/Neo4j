import json


class SearchItem:
    def __init__(self, id, url, rating, name, price, type, brand, model, characteristics):
        self.id = id
        self.url = url
        self.rating = rating
        self.name = name
        self.price = price
        self.type = type
        self.brand = brand
        self.model = model
        self.characteristics = characteristics

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
