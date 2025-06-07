from pathlib import Path

from munch import Munch

from ds2mermaid import version

import pytest


def test_nothing(capfd):
    print('yup, that just happened')
    out, err = capfd.readouterr()
    assert 'yup' in out
