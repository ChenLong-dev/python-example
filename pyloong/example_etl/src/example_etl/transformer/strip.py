"""Transform data and remove blank of data star and end."""
import logging

from example_etl.transformer.base import BaseTransformer

logger = logging.getLogger(__name__)


# pylint: disable=too-few-public-methods

class StripTransformer(BaseTransformer):
    """
    Transform data and remove blank of data star and end.
    """
    def transform(self, data: str) -> str:
        """Remove blank of data star and end."""
        logger.debug('Strip data: "%s"', data)
        return data.strip()
