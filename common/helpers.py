from typing import Dict


class CustomDict:
    def __init__(self, value: Dict):
        self.value = value

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)

        for key, value in instance.value.items():
            setattr(instance, key, value)

        return instance
