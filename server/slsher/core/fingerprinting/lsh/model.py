import dataclasses

from slsher.core.fingerprinting.model import Fingerprinter, Fingerprint


@dataclasses.dataclass
class LshFingerprintComparison:
    lhs: Fingerprint
    rhs: Fingerprint
    value: int | float


class LshFingerprinter(Fingerprinter):

    @staticmethod
    def compare_fingerprint(
            *fingerprints: list[Fingerprint]
    ) -> list[LshFingerprintComparison]:
        ...
