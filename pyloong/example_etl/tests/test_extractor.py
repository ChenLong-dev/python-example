"""Test extractor"""
import pytest, os

from example_etl.extractor.base import BaseExtractor
from example_etl.extractor.file import FileExtractor


def test_base_source(mocker):
    """Test base extractor"""
    close_mock = mocker.patch.object(BaseExtractor, 'close')
    with pytest.raises(NotImplementedError):
        with BaseExtractor(mocker.MagicMock()) as base:
            base.extract()
    assert close_mock.called_once()


def test_file_source(mocker, foo_file):
    """Test file extractor"""
    extractor = FileExtractor(mocker.MagicMock())
    extractor.settings.FILE_EXTRACTOR_PATH = foo_file
    data = list(extractor.extract())
    os.remove(extractor.settings.FILE_EXTRACTOR_PATH)
    assert data == ['foo']
