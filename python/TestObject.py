from dataclasses import dataclass

@dataclass
class TestObject:
    field1: int
    field2: str
    
    def __str__(self):
        return(f"field1: {self.field1}, field2: {self.field2}")
