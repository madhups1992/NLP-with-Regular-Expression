import sqlite3
import pytest

import project0
from project0 import project0

@pytest.mark.dependency(depends=['test_fetchincidents'])
def test_extractincidents():
    
    assert len(project0.extractincidents("/tmp/Project0/Arrest1.pdf")) >3
