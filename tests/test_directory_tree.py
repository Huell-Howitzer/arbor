"""
This module contains unit tests for the DirectoryTree class in the arbor.directory_tree module.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html
"""

import os
import unittest
from arbor.directory_tree import DirectoryTree

TREE_STRUCTURE = """test_dir/
├── test_subdir/
└── test_file.txt"""

# Define a constant for the filename
OUTPUT_FILENAME = "tree.txt"


class TestDirectoryTree(unittest.TestCase):
    """A suite of test cases for the DirectoryTree class"""

    def setUp(self):
        """
        The method will run before each test. It creates a DirectoryTree instance.

        :return: None
        """
        self.tree = DirectoryTree()

    def tearDown(self):
        """
        This method will run after each test. It cleans up the files and directories created by the tests.

        :return: None
        """
        if os.path.exists("test_dir"):
            os.rmdir("test_dir")
        if os.path.isfile(OUTPUT_FILENAME):
            os.remove(OUTPUT_FILENAME)

    def test_create(self):
        """
        This test ensures that the DirectoryTree correctly parses a string into a directory structure. It also
        ensures that the tree structure is correctly written to a file.

        :return: None

        .. automethod:: arbor.directory_tree.DirectoryTree.create
        """
        self.tree.create(TREE_STRUCTURE)

        # Write the tree structure to a file
        with open(OUTPUT_FILENAME, "w") as f:
            f.write(str(self.tree))

        # Assert
        self.assertTrue(os.path.exists("test_dir"))
        self.assertTrue(os.path.exists("test_dir/test_subdir"))
        self.assertTrue(os.path.isfile("test_dir/test_file.txt"))
        self.assertTrue(os.path.isfile(OUTPUT_FILENAME))


if __name__ == "__main__":
    unittest.main()
