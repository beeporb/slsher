import abc
import dataclasses
import enum
import pathlib
import typing


class FingerprintFamily(enum.Enum):
    CONVENTIONAL = enum.auto()
    LSH = enum.auto()
    PERCEPTUAL = enum.auto()


@dataclasses.dataclass
class Fingerprint:
    fingerprint_type: FingerprintFamily
    fingerprint_source: str
    fingerprint: typing.Any


class Fingerprinter(abc.ABC):

    @abc.abstractmethod
    def generate_fingerprint(self, data: bytes) -> Fingerprint:
        ...
