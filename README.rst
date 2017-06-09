*****
optic
*****

Refresh yourself on what those elusive options do, hassle free!

Example
#######

View the descriptions of -xcf and --update in the given order:
::

    optic tar xcf update

Output:
::

    -x, --extract, --get
    -extract files from an archive

    -c, --create
    create a new archive

    -f, --file ARCHIVE
    use archive file or device ARCHIVE

    -u, --update
    only append files newer than copy in archive

**********
Installing
**********

optic is installed using pip for Python 3. By default your local pip tool may be 
linked to Python 2. To be safe run the following command:
::

    sudo pip3 install optic

If the pip3 command is not found install the package with:
::

    sudo apt-get install python3-pip

Note that the above command will only work on Debian-based systems.

************
Contributing
************

Contributions are very welcome! Right now the project needs more definitions pages. And I mean a lot more. Follow the format of the existing definitions pages for your favorite command(s), submit a pull request, and your hard work will be added to the project. Cheers!

*******
License
*******

This software is licensed under GPLv3. See the `LICENSE` file for more information.
