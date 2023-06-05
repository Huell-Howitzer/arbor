# file_system_objects.py

import os


class FileSystemObject:
    """A generic class representing a filesystem object."""

    def __init__(self, name):
        """Initialize the filesystem object with a name."""
        self.name = name

    def create(self, path):
        """Create the filesystem object at the given path."""
        full_path = os.path.join(path, self.name)
        self._create(full_path)
        return full_path


class Directory(FileSystemObject):
    """A class representing a directory, which is a filesystem object that can contain other filesystem objects."""

    def __init__(self, name):
        """Initialize the directory with a name and an empty list of children."""
        super().__init__(name)
        self.children = []

    def _create(self, path):
        """Create the directory at the given path."""
        os.makedirs(path, exist_ok=True)

    def add_child(self, child):
        """Add a child filesystem object to the directory."""
        self.children.append(child)

    def create(self, path):
        """Create the directory and all of its children at the given path."""
        full_path = super().create(path)
        for child in self.children:
            child.create(full_path)


class File(FileSystemObject):
    """A class representing a file, which is a filesystem object that cannot contain other filesystem objects."""

    def _create(self, path):
        """Create the file at the given path."""
        open(path, 'w').close()
