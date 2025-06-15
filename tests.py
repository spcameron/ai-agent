# tests.py

import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_root(self):
        result = get_files_info("calculator", ".")
        print(result)
        
if __name__ == "__main__":
    unittest.main()