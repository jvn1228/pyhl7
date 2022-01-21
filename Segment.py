from pyhl7.Component import Component

class Segment:
    def __init__(self, name, components):
        self.name = name
        self.components = []
        for c in components:
            self.components.append(Component(c))

    def get(self, c_idx : int, sc_idx : int = None) -> Component:
        if sc_idx != None:
            return self.components[c_idx].get(sc_idx)
        return self.components[c_idx]

    def __str__(self):
        return "|".join([self.name] + [str(c) for c in self.components])
