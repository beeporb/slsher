import dataclasses

from slsher.core.fingerprinting.model import Fingerprinter, Fingerprint


@dataclasses.dataclass
class ConventionalFingerprintComparison:
    compared_fingerprints: tuple[Fingerprint, Fingerprint]
    conventional_match: bool


class ConventionalFingerprinter(Fingerprinter):

    @staticmethod
    def compare_fingerprint(
            *fingerprints: list[Fingerprint]
    ) -> ConventionalFingerprintComparison:
        ...
