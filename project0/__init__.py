from . import main
def main(url) :
    # save pdf from url
    Fname = main.fetchincidents(url)
    # Extract Data
    incidents = main.extractincidents(Fname)
    # Create Dataase
    db = main.createdb()
    # Insert Data
    main.populatedb(db, incidents)
    # Print Status
    sts = main.status(db)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True,
                         help="The arrest summary url.")
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)

#def ran_status():
    #db = '/tmp/Project0/normanpd.db'
    #sts = main.status(db)


