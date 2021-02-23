"""This module hierarchy provides utility classes for adding and
removing helper bones (for example IK targets, grip rotation handles etc)
to the hip/legs/feet section of a makehuman rig."""

from mpfb.services.logservice import LogService

_LOG = LogService.get_logger("leghelpers.init")
_LOG.trace("initializing leghelpers module")
