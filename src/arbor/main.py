"""
This module is the entry point for the Arbor application. It uses the Arbor module to generate a directory structure
from a text file. The text file should be passed as a command line argument.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html
"""

import sys
import argparse
from rich.console import Console
from arbor.directory_tree import DirectoryTree

console = Console()


def main():
    """
    The main function of the Arbor application. It processes command line arguments, creates a DirectoryTree from a file,
    and then creates the corresponding directory structure.

    .. automethod:: arbor.main.main
    """
    parser = argparse.ArgumentParser(
        description="Generate a directory structure from a text file."
    )
    parser.add_argument(
        "file", type=str, help="The text file containing the directory structure"
    )
    args = parser.parse_args()

    try:
        tree = DirectoryTree.from_file(args.file)
        tree.create()
        console.print(
            f"[green]Successfully created the directory structure from {args.file}![/green]"
        )
    except Exception as e:
        console.print(
            f"[red]An error occurred while creating the directory structure: {str(e)}[/red]"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
