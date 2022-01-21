from pyhl7.Segment import Segment
from pyhl7.Component import Component

class Hl7Message:
    def __init__(self):
        self.head = []

    def add_segment(self, segment):
        components = segment.split('|')
        if len(components):
            seg_name = components[0]
            self.head.append(Segment(seg_name, components[1:]))

    def get(self, seg_name, idx : int = 0) -> Segment:
        if idx == 0:
            for seg in self.head:
                if seg.name == seg_name:
                    return seg
        else:
            current_idx = 0
            for seg in self.head:
                if seg.name == seg_name:
                    if current_idx == idx:
                        return seg
                else:
                    current_idx += 1
        return None

    def __str__(self):
        return "\n".join([str(seg) for seg in self.head])

class Hl7Message231(Hl7Message):
    def __init__(self):
        super().__init__()
        self.version = "2.3.1"

def parse_file(f : str) -> Hl7Message:
    """
    Parse a file containing a HL7 message.
    """
    msg = Hl7Message231()
    with open(f, 'r') as f:
        for segment in f.readlines():
            # to do: validate component name
            msg.add_segment(segment.strip())
    return msg
