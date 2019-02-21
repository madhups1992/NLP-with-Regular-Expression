import sqlite3
import pytest
import project0
from project0 import project0

def test_createdb():
    
    incidents = project0.extractincidents("/tmp/Project0/Arrest1.pdf")
    len_inc = len(incidents)
    # Create Dataase
    db = project0.createdb()
	
    # Insert Data
    assert len(db) >0
