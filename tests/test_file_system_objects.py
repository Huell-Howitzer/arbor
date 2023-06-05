"""
Tests for the arbor.file_system_objects module.

This test module includes test cases for the File and Directory classes in
the arbor.file_system_objects module. The File tests check the creation and deletion
of File objects. The Directory tests verify the creation of Directory objects, as well
as the addition of child files.

Classes:
    TestFile: Test case for the File class.
    TestDirectory: Test case for the Directory class.
"""

import unittest

from arbor.file_system_objects import Directory
from arbor.file_system_objects import File

TEST_FILE_NAME = "test.txt"
TEST_DIRECTORY_NAME = "test_dir/"
CHILD_FILE_NAME = "child.txt"


class TestFile(unittest.TestCase):
    """
    The `TestFile` class is a subclass of unittest.TestCase that specifically tests
    the functionality of the `File` class found in the `arbor.file_system_objects` module.

    The `File` class represents a file object in a file system, and this test class
    evaluates whether the `File` class correctly creates a file and whether it can delete it.

    .. automethod:: setUp
    .. automethod:: tearDown
    .. automethod:: test_create
    .. automethod:: test_delete
    """

    def setUp(self):
        """
        The `setUp` method is automatically called by the testing framework for each individual test.
        ...
        """
        self.file = File(TEST_FILE_NAME)

    ...


class TestDirectory(unittest.TestCase):
    """
    The `TestDirectory` class is a subclass of unittest.TestCase that specifically tests
    the functionality of the `Directory` class found in the `arbor.file_system_objects` module.

    The `Directory` class represents a directory in a file system, and this test class
    checks whether the `Directory` class correctly creates a directory and whether it can add child files.

    .. automethod:: setUp
    .. automethod:: tearDown
    .. automethod:: test_create
    .. automethod:: test_add_child
    """

    def setUp(self):
        """
        The `setUp` method is used to set up any state that is shared across multiple tests. In this case,
        ...
        """
        self.directory = Directory(TEST_DIRECTORY_NAME)

    ...


if __name__ == "__main__":
    unittest.main()
