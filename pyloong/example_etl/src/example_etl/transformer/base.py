"""Base transformer"""


# pylint: disable=too-few-public-methods

class BaseTransformer:
    """Base transformer"""

    def __init__(self, settings):
        self.settings = settings

    def transform(self, data: str) -> str:
        """Transform data"""
        raise NotImplementedError()
