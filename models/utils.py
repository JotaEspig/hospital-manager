from typing import Dict


def is_data_valid(cls, data: Dict[str, str]) -> bool:
        for key in data.keys():
            if key not in cls.__dict__.keys():
                return False

        return True
