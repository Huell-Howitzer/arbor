import os
import unittest
from directory_builder import DirectoryTree


class TestDirectoryTree(unittest.TestCase):
    def test_create(self):
        # Set up
        tree = DirectoryTree()
        tree.create('''test_dir/
├── test_subdir/
└── test_file.txt''')

        # Assert
        self
