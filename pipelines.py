import json


class JsonExportPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        with open("entries.json", "w") as f:
            json.dump(self.items, f, indent=4)
