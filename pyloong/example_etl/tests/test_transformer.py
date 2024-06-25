"""Test transformer"""
import pytest

from example_etl.transformer.base import BaseTransformer
from example_etl.transformer.strip import StripTransformer


def test_base_process(mocker):
    """Test base transformer"""
    process = BaseTransformer(mocker.MagicMock())
    with pytest.raises(NotImplementedError):
        process.transform('foo')


@pytest.mark.parametrize(
    'data, expect_value',
    [
        ('xx ', 'xx'),
        (' xx ', 'xx'),
        ('xx', 'xx'),
    ]
)
def test_strip_process(mocker, data, expect_value):
    """Test strip transformer"""
    processor = StripTransformer(mocker.MagicMock())
    res = processor.transform(data)
    assert res == expect_value