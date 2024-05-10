import os
from utils.json_utils import load_data, save_data, generate_file_path


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
    original_file = generate_file_path("entries.json")
    original_data = load_data(original_file)

    filtered_comments_entries = filter_and_sort_entries_by_comments(original_data)
    comments_output_file = generate_file_path("filtered_comments_entries.json")
    save_data(filtered_comments_entries, comments_output_file)

    filtered_points_entries = filter_and_sort_entries_by_points(original_data)
    points_output_file = generate_file_path("filtered_points_entries.json")
    save_data(filtered_points_entries, points_output_file)


if __name__ == "__main__":
    main()
