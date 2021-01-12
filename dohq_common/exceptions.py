# -*- coding: utf-8 -*-

class DohqCommonException(Exception):
    """A base class for dohq-common"""


class DepsTxtLockInvalidLine(DohqCommonException):
    pass

class PackageInvalidVersion(DohqCommonException):
    pass
