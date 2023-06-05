import os
import unittest
from src.directory_builder.file_system_objects import Directory, File


class TestFile(unittest.TestCase):
    def setUp(self):
        self.file = File('test.txt')

    def tearDown(self):
        os.remove('test.txt')

    def test_create(self):
        self.file.create('')
        self.assertTrue(os.path.isfile('test.txt'))


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.directory = Directory('test_dir/')

    def tearDown(self):
        os.rmdir('test_dir')

    def test_create(self):
        self.directory.create('')
        self.assertTrue(os.path.isdir('test_dir'))

    def test_add_child(self):
        self.directory.add_child(File('child.txt'))
        self.assertEqual(len(self.directory.children), 1)


if __name__ == '__main__':
    unittest.main()
