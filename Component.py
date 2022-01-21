class Subcomponent:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def __call__(self):
        return self.value

    def __str__(self):
        return self.value

class Component:
    def __init__(self, subcomponent_string : str):
        subcomponents = subcomponent_string.split('^')
        self.subcomponents = []
        for sc in subcomponents:
            self.subcomponents.append(Subcomponent(sc))

    def get(self, index : int):
        return self.subcomponents[index]()

    def __str__(self):
        return "^".join([str(sc) for sc in self.subcomponents])
