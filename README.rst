optic
=====

Refresh yourself on what those elusive options do, hassle free!

Example
-------

View the descriptions of -xcf and --format in the given order:

    optic tar xcf update

Output:

    -x, --extract, --get
    -extract files from an archive

    -c, --create
    create a new archive

    -f, --file ARCHIVE
    use archive file or device ARCHIVE

    -u, --update
    only append files newer than copy in archive

Notes
-----

For the sake of my sanity, I will refer to the optional arguments for this
program as flags, and the positional arguments as options.

Installing
==========

optic is installed using pip for Python 3. By default your local pip tool may be 
linked to Python 2. To be safe run the following command:

    sudo pip3 install optic

If the pip3 command is not found install the package with:

    sudo apt-get install python3-pip

Note that the above command will only work on Debian-based systems.

Contributing
============

This project is still in the beginning stages. Contributions are very welcome.

License
=======

This software is licensed under GPLv3. See the `LICENSE` file for more information.
