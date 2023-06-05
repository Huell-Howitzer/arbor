"""
This module provides the DirectoryTree class, which represents a directory tree and provides methods for creating
directory trees from strings or files.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html
"""

import os
from arbor.file_system_objects import Directory, File


class DirectoryTree:
    """
    Represents a directory tree.

    Attributes:
        root: A Directory object representing the root of the directory tree.

    Methods:
        from_file(filename): Class method to create a directory tree from a file.
        create(path): Creates the directory tree at the given path.
    """

    def __init__(self):
        """
        Initialize a new DirectoryTree object with an empty root directory.

        :return: None
        """
        self.root = Directory("")

    @classmethod
    def from_file(cls, filename):
        """
        Create a directory tree from a file.

        The file should contain a string representation of a directory tree. Each line represents a directory or
        file. The depth of the directory or file is determined by the number of "|" and "├" characters in the line.
        A "/" in the line indicates that the line represents a directory, and a lack of "/" indicates a file.

        :param filename: The name of the file containing the string representation of the directory tree.
        :return: A DirectoryTree object representing the directory tree.

        .. automethod:: arbor.directory_tree.DirectoryTree.from_file
        """
        tree = cls()

        with open(filename, "r") as f:
            lines = f.readlines()

        parents = [tree.root]
        for line in lines:
            depth = line.count("|") + line.count("├") + line.count("└")
            name = (
                line.replace("|", "")
                .replace("├", "")
                .replace("└", "")
                .replace("─", "")
                .replace("/", "")
                .strip()
            )

            if "/" in line:  # This line represents a directory
                _dir = Directory(name)
                parents[depth].add(_dir)
                if depth + 1 < len(parents):
                    parents[depth + 1] = _dir
                else:
                    parents.append(_dir)
            else:  # This line represents a file
                _file = File(name)
                parents[depth].add(_file)

        return tree

    def create(self, path="."):
        """
        Create the directory tree at the given path.

        The root directory of the directory tree will be created at the given path, and all subdirectories and files
        will be created within the root directory according to the structure of the directory tree.

        :param path: The path where the root directory of the directory tree should be created.
        :return: None

        .. automethod:: arbor.directory_tree.DirectoryTree.create
        """
        self.root.create(path)
