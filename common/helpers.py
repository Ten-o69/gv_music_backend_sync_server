from typing import Dict, Any


class CustomDict:
    """
    A custom dictionary-like object that assigns dictionary keys as attributes.

    This class takes a dictionary on initialization and dynamically sets
    each key-value pair in the dictionary as an attribute of the instance.

    Example:
        >>> data = {"name": "Alice", "age": 30}
        >>> obj = CustomDict(data)
        >>> obj.name
        'Alice'
        >>> obj.age
        30

    Attributes:
        value (Dict[Any, Any]): The dictionary passed during initialization.
    """

    def __init__(self, value: Dict[Any, Any]):
        """
        Initialize a CustomDict instance with a given dictionary.

        Args:
            value (Dict[Any, Any]): A dictionary to be stored and converted to attributes.
        """
        self.value = value

    def __new__(cls, *args, **kwargs):
        """
        Create and initialize a new instance of CustomDict.

        After creating the instance and initializing it, each key-value pair in the
        dictionary is assigned as an attribute on the instance.

        Returns:
            CustomDict: A fully initialized CustomDict object with attributes set.
        """
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)

        for key, value in instance.value.items():
            setattr(instance, key, value)

        return instance
