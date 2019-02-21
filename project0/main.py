import argparse

import project0

def main(url):
    # Download data
    Fname = project0.fetchincidents(url)

    # Extract Data
    incidents = project0.extractincidents(Fname)
	
    # Create Dataase
    db = project0.createdb()
	
    # Insert Data
    project0.populatedb(db, incidents)
	
    # Print Status
    sts = project0.status(db)

    # Print multiple random status 
    project0.multiple_sts(db)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True, 
                         help="The arrest summary url.")
     
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)

