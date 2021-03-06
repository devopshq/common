from wcmatch import fnmatch


class PackageMatch:
    def __init__(self, line):
        placeholders = line.split()

        placeholders_count = len(placeholders)

        if placeholders_count not in [2, 3]:
            raise line

        self.package_name = placeholders[0]
        self.version_pattern = placeholders[1]

        if self.version_pattern[-1] == '-':
            self.version_pattern = f"{self.version_pattern[:-1]}|!*-*"

        if placeholders_count == 3:
            self.contracts = [c for c in placeholders[2].strip().split(';')]
        else:
            self.contracts = []

    def is_package_fullname_match_version_pattern(self, package):
        return package.package == self.package_name and \
            fnmatch.fnmatch(package.fullversion,
                            self.version_pattern,
                            flags=fnmatch.NEGATE | fnmatch.SPLIT)

    def is_package_contracts_match(self, package):
        return all(package.has_contract(c) for c in self.contracts)

    def is_package_match(self, package):
        return self.is_package_fullname_match_version_pattern(package) and self.is_package_contracts_match(package)


class DepsTxtSimpleParser:
    def __init__(self, deps_txt_iter):

        self.package_matches = []

        for i, line in enumerate(deps_txt_iter):
            line = line.strip()

            if not line or line.startswith(('#', '[',)):
                continue

            self.package_matches.append(PackageMatch(line))

    def is_package_fullname_match_version_pattern(self, package):
        return any(match.is_package_fullname_match_version_pattern(package) for match in self.package_matches)


class DepsTxtSimpleReader(DepsTxtSimpleParser):
    def __init__(self, path):
        with open(path, newline='', encoding='utf-8-sig') as f:
            super().__init__(f)
