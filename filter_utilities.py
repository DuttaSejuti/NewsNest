import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def filter_and_sort_entries_by_comments(entries):
    filtered_entries = []

    for entry in entries:
        if len(entry["title"].split()) > 5:
            filtered_entries.append(entry)

    filtered_entries.sort(key=lambda x: x["total_comments"], reverse=True)
    return filtered_entries


def filter_and_sort_entries_by_points(entries):
    filtered_entries = []

    for entry in entries:
        if len(entry["title"].split()) <= 5:
            filtered_entries.append(entry)

    filtered_entries.sort(key=lambda x: x["points"], reverse=True)
    return filtered_entries


def main():
    original_data = load_data("entries.json")

    filtered_comments_entries = filter_and_sort_entries_by_comments(original_data)
    print(
        f"### There are {len(filtered_comments_entries)} entries with more than 5 words ###"
    )
    save_data(filtered_comments_entries, "filtered_comments_entries.json")

    filtered_points_entries = filter_and_sort_entries_by_points(original_data)
    print(
        f"### There are {len(filtered_points_entries)} entries with less or equal 5 words ###"
    )
    save_data(filtered_points_entries, "filtered_points_entries.json")


if __name__ == "__main__":
    main()
