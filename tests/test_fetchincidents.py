import pytest
import argparse

import project0
from project0 import project0

def test_fetchincidents():
    url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf"
    assert project0.fetchincidents(url) is not None


    



