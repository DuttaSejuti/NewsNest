import json
import os

class JsonExportPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        file_path = os.path.join('data', 'entries.json')
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)
