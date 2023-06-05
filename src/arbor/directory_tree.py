# src/arbor/directory_tree.py

import os
from .file_system_objects import Directory, File


class DirectoryTree:
    def __init__(self):
        self.root = Directory("")

    @classmethod
    def from_file(cls, filename):
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
                dir = Directory(name)
                parents[depth].add(dir)
                if depth + 1 < len(parents):
                    parents[depth + 1] = dir
                else:
                    parents.append(dir)
            else:  # This line represents a file
                file = File(name)
                parents[depth].add(file)

        return tree

    def create(self, path="."):
        self.root.create(path)
