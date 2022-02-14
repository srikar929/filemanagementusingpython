"""
This module is of testing the Functions in the server
module and the test is done with the unittest module.
"""
import unittest
import Functions

class TestFunctions(unittest.TestCase):
    """
    In this class the testcase was taken to test the server code
    (Functions) commands, which gives from server to client.
    There are four functions in the sense of four different testcases
    Ofcourse the methods was passed the test without any fail.
    """
    def test1_all_functions(self):
        """
        In this 1st test case the userid is srikar90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = Functions.Functions("srikar90")

        createfol = opera.creating_the_folder("birds")
        self.assertEqual(createfol, True)

        writefil = opera.writing_the_file("birds", "eagle", 'Eagle is good  bird')
        self.assertEqual(writefil, True)

        readfil = opera.reading_the_file("birds", "eagle")
        self.assertEqual(readfil, 'E a g l e   i s   g o o d     b i r d')

        change = opera.change_the_folder_path("birds")
        self.assertEqual(change, True)

    def test2_all_functions(self):
        """
        In this 2nd test case the userid is mikhel90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = Functions.Functions("mikhel90")

        createfol = opera.creating_the_folder("friends")
        self.assertEqual(createfol, True)

        writefil = opera.writing_the_file("friends", "tommy", "tommy is good friend")
        self.assertEqual(writefil, True)

        readfil = opera.reading_the_file("friends", "tommy")
        self.assertEqual(readfil, "t o m m y   i s   g o o d   f r i e n d")

        change = opera.change_the_folder_path("friends")
        self.assertEqual(change, True)

    def test3_all_functions(self):
        """
        In this 3rd test case the userid is aravind90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = Functions.Functions("aravind90")

        createfol = opera.creating_the_folder("donkey")
        self.assertEqual(createfol, True)

        writefil = opera.writing_the_file("donkey", "puty", "puty is good donkey")
        self.assertEqual(writefil, True)

        readfil = opera.reading_the_file("donkey", "puty")
        self.assertEqual(readfil, "p u t y   i s   g o o d   d o n k e y")

        change = opera.change_the_folder_path("donkey")
        self.assertEqual(change, True)

    def test4_all_functions(self):
        """
        In this 4th test case the userid is keerthi90 and  folder is created,
        a file is writtten and the a file read is done.
        """
        opera = Functions.Functions("keerthi90")

        createfol = opera.creating_the_folder("nope")
        self.assertEqual(createfol, True)

        writefil = opera.writing_the_file("nope", "girl", "I am good girl")
        self.assertEqual(writefil, True)

        readfil = opera.reading_the_file("nope", "girl")
        self.assertEqual(readfil, "I   a m   g o o d   g i r l")

        change = opera.change_the_folder_path("nope")
        self.assertEqual(change, True)

if __name__ == "__main__":
    unittest.main()
