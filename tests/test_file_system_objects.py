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

import os
import unittest

from arbor.file_system_objects import Directory
from arbor.file_system_objects import File
from arbor.file_system_objects import FileSystemObject

TEST_FILE_NAME = "test.txt"
TEST_DIRECTORY_NAME = "test_dir"
CHILD_FILE_NAME = "child.txt"


class TestFile(unittest.TestCase):
    """
    The `TestFile` class is a subclass of unittest.TestCase that specifically tests
    the functionality of the `File` class found in the `arbor.file_system_objects` module.

    The `File` class represents a file object in a file system, and this test class
    evaluates whether the `File` class correctly creates a file.
    """

    def setUp(self):
        """
        The `setUp` method is automatically called by the testing framework for each individual test.
        It creates an instance of `File` for testing.
        """
        self.file = File(TEST_FILE_NAME)

    def tearDown(self):
        """
        The `tearDown` method is automatically called by the testing framework after each test.
        It removes the test file if it was created.
        """
        if os.path.exists(TEST_FILE_NAME):
            os.remove(TEST_FILE_NAME)

    def test_create(self):
        """
        Test that the `create` method correctly creates a file.
        """
        self.file.create(".")
        self.assertTrue(os.path.exists(TEST_FILE_NAME))

    def test_delete(self):
        """
        Test that the `delete` method correctly deletes a file.
        """
        self.file.create(".")
        self.file.delete(".")
        self.assertFalse(os.path.exists(TEST_FILE_NAME))


class TestDirectory(unittest.TestCase):
    """
    The `TestDirectory` class is a subclass of unittest.TestCase that specifically tests
    the functionality of the `Directory` class found in the `arbor.file_system_objects` module.

    The `Directory` class represents a directory in a file system, and this test class
    checks whether the `Directory` class correctly creates a directory and whether it can add child files.
    """

    def setUp(self):
        """
        The `setUp` method is used to set up any state that is shared across multiple tests.
        It creates an instance of `Directory` for testing.
        """
        self.directory = Directory(TEST_DIRECTORY_NAME)

    def tearDown(self):
        """
        The `tearDown` method is automatically called by the testing framework after each test.
        It removes the test directory and its content if they were created.
        """
        if os.path.exists(os.path.join(TEST_DIRECTORY_NAME, CHILD_FILE_NAME)):
            os.remove(os.path.join(TEST_DIRECTORY_NAME, CHILD_FILE_NAME))

        if os.path.exists(TEST_DIRECTORY_NAME):
            os.rmdir(TEST_DIRECTORY_NAME)

    def test_create(self):
        """
        Test that the `create` method correctly creates a directory.
        """
        self.directory.create(".")
        self.assertTrue(os.path.exists(TEST_DIRECTORY_NAME))

    def test_add_child(self):
        """
        Test that the `add` method correctly adds a child file to the directory.
        """
        child_file = File(CHILD_FILE_NAME)
        self.directory.add(child_file)
        self.assertIn(child_file, self.directory.children)


class File(FileSystemObject):
    """
    Represents a file, which is a type of filesystem object.

    .. automethod:: arbor.file_system_objects.File._create
    """

    def _create(self, path):
        """
        Create the file at the given path.

        :param path: The path where the file should be created.
        :return: None
        """
        with open(path, "a") as f:
            f.close()

    def create(self, directory_path):
        """
        Create the file.

        :param directory_path: The directory where the file should be created.
        :return: None
        """
        full_path = os.path.join(directory_path, self.name)
        self._create(full_path)

    def delete(self, directory_path):
        """
        Delete the file.

        :param directory_path: The directory where the file should be deleted from.
        :return: None
        """
        full_path = os.path.join(directory_path, self.name)
        if os.path.exists(full_path):
            os.remove(full_path)


if __name__ == "__main__":
    unittest.main()
