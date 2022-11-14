class PIF:
    def __init__(self):
        self.identifiers = []

    def add(self, code, st_pos):
        self.identifiers.append((code, st_pos))

    def __str__(self):
        return str(self.identifiers)