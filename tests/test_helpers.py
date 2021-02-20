from audiolipsum.exceptions import ExternalLibraryError
from audiolipsum.helpers import lame
from mock import patch
import pytest


class MockResult(object):
    stdout = ''


def run_subprocess(cmd, shell, capture_output, text):
    assert cmd == 'which lame'
    assert shell
    assert capture_output
    assert text
    return MockResult()


@patch('subprocess.run', run_subprocess)
def test_lame():
    with pytest.raises(ExternalLibraryError):
        lame('source.wav', 'dest.mp3')
