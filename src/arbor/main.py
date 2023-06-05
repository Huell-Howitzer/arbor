import sys
from .directory_tree import DirectoryTree


def main():
    # Command line arguments are available through the sys.argv list
    # sys.argv[0] is the script name itself
    # sys.argv[1] will be the command line argument you pass.

    if len(sys.argv) != 2:
        print("Usage: arbor <file>")
        sys.exit(1)

    filename = sys.argv[1]

    tree = DirectoryTree.from_file(filename)
    tree.create()


if __name__ == "__main__":
    main()
