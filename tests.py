# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    @unittest.skip("Skipping GFI tests")
    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        print(result)
        print("")

        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)
        print("")

        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)
        print("")

        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)
        print("")
        
    
    def test_get_file_content(self):
        # result = get_file_content("calculator", "lorem.txt")
        # print("Result for lorem.txt:")
        # print(result)
        # print("")
        
        result = get_file_content("calculator", "main.py")
        print("Result for main.py:")
        print(result)
        print("")

        result = get_file_content("calculator", "pkg/calculator.py")
        print("Result for pkg/calculator.py:")
        print(result)
        print("")

        result = get_file_content("calculator", "/bin/cat")
        print("Result for /bin/cat:")
        print(result)
        print("")

        
if __name__ == "__main__":
    unittest.main()