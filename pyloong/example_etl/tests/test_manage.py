"""Test manage"""
import pytest

from example_etl.exceptions import PluginNotFoundError
from example_etl.extractor.file import FileExtractor
from example_etl.manage import Manage, get_extension


def test_get_extension():
    """Test get extension"""
    plugin = get_extension('example_etl.extractor', 'file')
    assert plugin is FileExtractor


def test_get_extension_error():
    """Test get extension error"""
    with pytest.raises(PluginNotFoundError):
        get_extension('example_etl.extractor', 'xxx')


def test_manage_run(mocker):
    """Test manage run"""
    mocker.patch('example_etl.manage.get_extension')
    process_mock = mocker.patch.object(Manage, 'transform')
    manage = Manage()

    manage.run()
    assert process_mock.called_once()


def test_manage_transform(mocker):
    """Test manage transform"""
    magic_mock = mocker.MagicMock()
    manage = Manage()
    manage.transformer = magic_mock
    magic_mock.extract.return_value = [1, 2]
    manage.transform(magic_mock, magic_mock)

    assert magic_mock.extract.called_once()
    assert magic_mock.load.call_count == 2
    assert magic_mock.transform.call_count == 2
