.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/python-3.10-blue.svg
   :target: https://www.python.org/downloads/release/python-3100/

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT

.. image:: https://codecov.io/gh/huell-howitzer/arbor/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/huell-howitzer/arbor


===================
Arbor - Tree Maker
===================

Arbor is a powerful and flexible Python package that facilitates the creation
of directory trees and file structures from a plain text file. It simplifies
the management of complex directory structures, providing a clear and
intuitive way to create, manipulate, and visualize them.

Features
========

- **File Structure Definition**: Define your file and directory structures through simple plain text files.

- **Directory Tree Creation**: Generate physical directory trees and file structures based on your definitions.

- **Easy Integration**: Arbor can be easily integrated into larger Python projects.

- **Extensible**: Open source and written in Python, Arbor can be modified to suit your needs.

Installation
============

To install Arbor, you can simply use pip:

.. code-block:: shell

    pip install arbor

You can also clone the repository and install manually:

.. code-block:: shell

    git clone https://github.com/huell-howitzer/arbor.git
    cd arbor
    python setup.py install

Quickstart
==========

Here's how you can start using Arbor:

.. code-block:: python

    from arbor import DirectoryTree

    # Define your tree in a plain text file
    with open("my_tree.txt", "w") as f:
        f.write("...")  # replace with your tree definition

    # Create the tree
    tree = DirectoryTree.from_file("my_tree.txt")
    tree.create()

This will create a directory tree as per the definition in "my_tree.txt".

For more examples and usage, please refer to the official documentation.

Contributing
============

We welcome contributions from the open source community! To get started:

1. Fork the Arbor repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and open a pull request.

For more details, please see our contributing guidelines.

License
=======

Arbor is released under the MIT License. See the `LICENSE`_ file for more details.

.. _LICENSE: https://github.com/huell-howitzer/arbor/blob/main/LICENSE

Documentation
=============

Detailed documentation is available in our `Sphinx docs`_.

.. _Sphinx docs: https://huell-howitzer.github.io/arbor/

Support
=======

If you are having issues or have questions, you can:

- Report issues on the GitHub `issue tracker`_.

.. _issue tracker: https://github.com/huell-howitzer/arbor/issues

