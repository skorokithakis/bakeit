BakeIt
------

BakeIt is a command line utility (and Python library) to
`Pastery <https://www.pastery.net>`__, the best pastebin in the world.
BakeIt aims to be simple to use and unobtrusive.

Installation
============

To install, use ``pip``:

::

    pip install bakeit

You are done!

Usage
=====

Using BakeIt is similarly easy. First, create a file with your Pastery
API key in ``~/.config/bakeit.cfg``, like so:

::

    [pastery]
    api_key = eisha8ahqui7Aesh0fasyu8HFsdo

Then, just pass the file you want to upload to the ``bakeit`` command:

::

    $ bakeit <file to upload>
    Paste URL: https://www.pastery.net/oniasd/

You can also pipe stuff to it:

::

    $ cat myfile | grep hello | bakeit
    Paste URL: https://www.pastery.net/oniasd/

Usage as a Python library
=========================

BakeIt provides the ``PasteryUploader`` class:

:sub:`[STRIKEOUT:.python >>> from bakeit import PasteryUploader >>> pu =
PasteryUploader("your API key") >>> pu.upload("this is the text to
upload") "https://www.pastery.net/oniasd/"]`

``PasteryUploader`` accepts the following arguments:

-  ``body`` - The body of the paste.
-  ``title`` (optional) - The title to give the paste.
-  ``language`` (optional) - The language the paste is in. Pastery will
   attempt to autodetect this if omitted.
-  ``duration`` (optional) - The number of minutes to keep this paste
   for.
-  ``max_views`` (optional) - The number of views to keep this paste
   for.

Happy pasting!
