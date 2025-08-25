# flake8: noqa

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("bakeit")
except PackageNotFoundError:
    # Package is not installed.
    __version__ = "0.0.0+unknown"

from bakeit.uploader import PasteryUploader
