import pkg_resources

__version__ = pkg_resources.get_distribution("awssert").version

from awssert.hooks import *
