import pathlib, sys

cwd = pathlib.Path.cwd()
sys.path.append(str( cwd.parent ))

from src import app
import start

def test_get_weather():
    assert app.get_weather() == 'Good'


def test_sum():
    assert start.sum(1,2) == 3