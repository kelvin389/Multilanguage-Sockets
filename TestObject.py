from dataclasses import dataclass

@dataclass
class TestObject:
    field1: int
    field2: str

    def __init__(self, f1: int, f2: str):
        self.field1 = f1
        self.field2 = f2
    
    def __str__(self):
        return(f"field1: {self.field1}, field2: {self.field2}")