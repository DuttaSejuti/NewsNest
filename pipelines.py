from utils.json_utils import save_data, generate_file_path

class JsonExportPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        file_path = generate_file_path(filename='entries.json')
        save_data(self.items, file_path)
