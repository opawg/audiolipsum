from audiolipsum import generate_mp3s
from mutagen.mp3 import MP3


def test_generate_mp3s():
    files = 0

    for f in generate_mp3s(2, duration=1, multiprocessing=False):
        mp3 = MP3(f.name)
        duration = mp3.info.length
        files += 1
        assert duration == 1

    assert files == 2
