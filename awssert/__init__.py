import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("awssert").version
except pkg_resources.DistributionNotFound:
    pass

from awssert.hooks import *
