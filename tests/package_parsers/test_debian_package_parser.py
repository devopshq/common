import pytest

from dohq_common.exceptions import PackageInvalidVersion
from dohq_common.package_parsers.debian_package_name_parser import DebianPackageNameParser


@pytest.mark.parametrize(
    "test_case",
    [
        ['package-name-long_2.5.9.314_all.deb', 'package-name-long', '2.5.9.314', 'all'],
        ['package-name_2.5.317_all.deb', 'package-name', '2.5.317', 'all'],
    ]
)
def test_parse_from_package_name_success(test_case):
    p = DebianPackageNameParser.parse_from_package_name(test_case[0])
    assert p.package == test_case[1]
    assert p.version == test_case[2]
    assert p.arch == test_case[3]
    assert p.fullname == test_case[0]

@pytest.mark.parametrize(
    "test_case",
    [
        'package-name-long_2.5.9.314.deb',
    ]
)
def test_parse_from_package_name_success(test_case):
    with pytest.raises(PackageInvalidVersion) as exc_info:
        package = DebianPackageNameParser.parse_from_package_name(test_case)
