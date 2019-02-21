import sqlite3
import pytest
import project0
from project0 import project0

def test_populatedb():
    
    incidents = project0.extractincidents("/tmp/Project0/Arrest1.pdf")
    len_inc = len(incidents)
    # Create Dataase
    db = project0.createdb()
	
    # Insert Data
    project0.populatedb(db, incidents)
	
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    sql = '''SELECT * FROM arrests'''
    c.execute(sql)
    assert len(c.fetchall()) == len_inc
