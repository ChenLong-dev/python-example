"""
File extractor

extract data from file.
"""
import logging
from typing import Iterable

from example_etl.constants import DEFAULT_ENCODING
from example_etl.extractor.base import BaseExtractor

logger = logging.getLogger(__name__)


class FileExtractor(BaseExtractor):
    """File extractor"""

    def extract(self) -> Iterable[str]:
        """Open and read file"""
        extractor_path = self.settings.FILE_EXTRACTOR_PATH
        logger.info('Extract data from %s', extractor_path)
        with open(extractor_path, 'r', encoding=DEFAULT_ENCODING) as file:
            for i in file:
                yield i
