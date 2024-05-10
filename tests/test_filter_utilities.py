import unittest
from filter_utilities import filter_and_sort_entries_by_comments, filter_and_sort_entries_by_points

class TestFilterUtilities(unittest.TestCase):
    def setUp(self):
        self.original_data = [
            {"order": 1, "title": "Popover API", "total_comments": 10, "points": 20},
            {"order": 2, "title": "Life-like particle system", "total_comments": 5, "points": 30},
            {"order": 3, "title": "Logicola 3 'NEW' look", "total_comments": 8, "points": 15},
            {"order": 4, "title": "SWPC issues first G4 geomagnetic storm watch since 2005", "total_comments": 12, "points": 25},
            {"order": 5, "title": "Apple apologizes for iPad 'Crush' ad that 'missed the mark'", "total_comments": 12,
             "points": 25},
        ]
        self.empty_data = []

    def test_filter_and_sort_entries_by_comments(self):
        filtered_entries = filter_and_sort_entries_by_comments(self.original_data)
        self.assertEqual(len(filtered_entries), 2)
        self.assertEqual(filtered_entries[0]["title"], "SWPC issues first G4 geomagnetic storm watch since 2005")
        self.assertEqual(filtered_entries[1]["title"], "Apple apologizes for iPad 'Crush' ad that 'missed the mark'")

        sorted_entries = sorted(filtered_entries, key=lambda x: x["total_comments"], reverse=True)
        self.assertEqual(filtered_entries, sorted_entries)

    def test_filter_and_sort_entries_by_points(self):
        filtered_entries = filter_and_sort_entries_by_points(self.original_data)
        self.assertEqual(len(filtered_entries), 3)
        self.assertEqual(filtered_entries[0]["title"], "Life-like particle system")
        self.assertEqual(filtered_entries[1]["title"], "Popover API")

        sorted_entries = sorted(filtered_entries, key=lambda x: x["points"], reverse=True)
        self.assertEqual(filtered_entries, sorted_entries)

    def test_filter_and_sort_entries_empty_file(self):
        filtered_entries = filter_and_sort_entries_by_comments(self.empty_data)
        self.assertEqual(len(filtered_entries), 0)

        filtered_entries = filter_and_sort_entries_by_points(self.empty_data)
        self.assertEqual(len(filtered_entries), 0)

if __name__ == "__main__":
    unittest.main()
