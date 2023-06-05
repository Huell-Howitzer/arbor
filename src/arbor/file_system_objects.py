# file_system_objects.py

"""
This module provides classes representing generic filesystem objects, directories, and files.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html
"""

import os
from arbor.directory_tree import DirectoryTree


class FileSystemObject:
    """
    Represents a generic filesystem object.

    Attributes:
        name: The name of the filesystem object.
    """

    def __init__(self, name):
        """
        Initialize a FileSystemObject with a name.

        :param name: The name of the filesystem object.
        :return: None
        """
        self.name = name

    def create(self, path):
        """
        Create the filesystem object at the given path.

        :param path: The path where the filesystem object should be created.
        :return: The full path where the filesystem object was created.

        .. automethod:: arbor.file_system_objects.FileSystemObject.create
        """
        full_path = os.path.join(path, self.name)
        self._create(full_path)
        return full_path


class Directory(FileSystemObject):
    """
    Represents a directory, which is a filesystem object that can contain other filesystem objects.

    Attributes:
        children: A list of filesystem objects contained in the directory.
    """

    def __init__(self, name):
        """
        Initialize a Directory with a name and an empty list of children.

        :param name: The name of the directory.
        :return: None
        """
        super().__init__(name)
        self.children = []

    def _create(self, path):
        """
        Create the directory at the given path.

        :param path: The path where the directory should be created.
        :return: None
        """
        os.makedirs(path, exist_ok=True)

    def add_child(self, child):
        """
        Add a child filesystem object to the directory.

        :param child: A FileSystemObject to add as a child.
        :return: None
        """
        self.children.append(child)

    def create(self, path):
        """
        Create the directory and all of its children at the given path.

        :param path: The path where the directory should be created.
        :return: None

        .. automethod:: arbor.file_system_objects.Directory.create
        """
        full_path = super().create(path)
        for child in self.children:
            child.create(full_path)

    def add(self, _file):
        """
        Add a filesystem object to the directory.

        :param _file: A FileSystemObject to add.
        :return: None

        .. automethod:: arbor.file_system_objects.Directory.add
        """
        self.children.append(_file)


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
        open(path, "a").close()
