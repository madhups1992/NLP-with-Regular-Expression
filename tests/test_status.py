import sqlite3
import pytest

import project0
from project0 import project0

def test_status():
        # Extract Data
    incidents = project0.extractincidents("/tmp/Project0/Arrest1.pdf")
    len_inc = len(incidents)
    # Create Dataase
    db = project0.createdb()

    # Insert Data
    project0.populatedb(db, incidents)

    # Print Status
 #   project0.status(db)

    random_status1 = project0.status(db)
    random_status2 = project0.status(db)
    random_status3 = project0.status(db)
    check = 0
    if((random_status1 != random_status2) or (random_status1 !=random_status3)) :
        check = 1
    assert check == 1
