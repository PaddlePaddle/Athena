class NameGenerator:
    def __init__(self):
        self.key2name = {}
        self.prefix2counter = {}

    def Generate(self, key, prefix):
        if key in self.key2name:
            return self.key2name[key]
        if prefix not in self.prefix2counter:
            self.prefix2counter[prefix] = -1
        self.prefix2counter[prefix] += 1
        name = f"{prefix}_{self.prefix2counter[prefix]}"
        self.key2name[key] = name
        return name
