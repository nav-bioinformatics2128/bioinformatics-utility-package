from dataclasses import dataclass


@dataclass
class SequenceInfo:
    sequence_id: str
    length: int
    gc_percent: float
