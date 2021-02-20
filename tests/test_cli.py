from click.testing import CliRunner
from audiolipsum.cli import main
from mock import patch
from tempfile import mkstemp, gettempdir
import os


def test_outdir_notfound():
    runner = CliRunner()
    result = runner.invoke(main, ['--outdir', 'testout'])
    assert result.exit_code
    assert 'Path does not exist' in result.output


def generate_mp3s(*args, **kwargs):
    handle, filename = mkstemp('.mp3')
    os.close(handle)
    yield open(filename, 'rb')


@patch('audiolipsum.generate_mp3s', generate_mp3s)
def test_clean():
    temp = gettempdir()
    runner = CliRunner()
    result = runner.invoke(main, ['1', '--outdir', temp])
    assert not result.exit_code
