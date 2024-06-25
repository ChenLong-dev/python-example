"""Test config"""
import tempfile,os

import pytest
from click.testing import CliRunner


@pytest.fixture()
def clicker():
    """clicker fixture"""
    yield CliRunner()

@pytest.fixture()
def foo_file():
    """foo file"""
    if os.name == 'nt':
        # 当这个临时文件处于打开状态，在unix平台，该名字可以用于再次打开临时文件，但是在windows不能。所以，如果要在windows打开该临时文件，需要将文件关闭，然后再打开，操作完文件后，再调用os.remove删除临时文件。   
        file = tempfile.NamedTemporaryFile(mode='w',delete=False) #注意，delete设置为False，就不会关闭文件后自动清理了
        file.close()
        # #再次打开之前一定要先关闭
        # #最后写的这行代码用于清理这个临时文件
        open(file.name,'w').write('foo')
        file.close()
        return file.name
    else:
        with tempfile.NamedTemporaryFile(mode='w') as file:
            file.write('foo')
            file.flush()
            return file.name
        
    
