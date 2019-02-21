import pandas as pd
import numpy as np
import urllib, json
import urllib.request
from typing import List, Dict, Any
import tempfile
import PyPDF2 
import argparse
import sqlite3
import re

#Fetching all the incidents

def fetchincidents(url):
    """ This function downloads the json data from the url."""
    # TODO add code here
    data=urllib.request.urlopen(url)
    raw_pdf_file = data.read()
    fileName = '/tmp/Project0/Arrest'+str(np.random.randint(0,100))+'.pdf'
    # Saving a pdf document
    with open(fileName, 'wb') as f:
        f.write(raw_pdf_file)
    return (fileName)

# reading the pdf
def extractincidents(fname) :
    with open(fname, 'rb') as f:
        # Read the PDF
            pdfReader = PyPDF2.PdfFileReader(f)
            pdfReader.getNumPages()

        # Get the first page
            page1 = pdfReader.getPage(0).extractText()

            #Splitting each row by ";"
            row =page1.split(';')

            #Seperating the first columnas header
            match = re.search(r"Officer",row[0])
            match.span()[1]
            dim = len(row)
            for i in range(dim-1, 1, -1) :
                   row[i]=row[i-1]
            row[1] = row[0][match.span()[1]:]
            row[0] = row[0][:match.span()[1]-1]
            row[1]

            #Replacing ' \n' and '-\n'

            dim =len(row)+1
            colum= [] * dim
            for i in range(1,dim-1) :
                row[i] = row[i].replace(' \n',' ')

            for i in range(1,dim-1) :
                row[i] = row[i].replace('-\n','-')

            # Date/ time extraction
            dim =len(row)-1
            time=[None] * dim
            for i in range(1,dim+1) :
                match = re.search(r'\d\d?/\d{1,2}/\d{4} \d\d?:\d\d',row[i])
                time[i-1] = match.group(0)

            # case number extraction
            dim =len(row)-1
            case=[None] * dim
            for i in range(1,dim+1) :
                match = re.search(r'\d{4}-\d{8}',row[i])
                case[i-1] = match.group(0)

            dim = len(row)-1
            temp=[None] * dim
            for i in range(1,dim+1) :
                m = re.search('\d{4}-\d{8}\n([\na-zA-Z0-9/=>&\s.\'\(\)-]+)\n\d\d?/\d\d?/\d{4}', row[i])
                if m:
                    found = m.group(1)
                    temp[i-1]=found
            #Extracting offense
            offense=[None] * dim
            dim = len(row)-1
            for i in range(0,dim) :
                m = re.search('\n([A-Z0-9/=>&\s.\'\(\)-]+)\n', temp[i])
                if m:
                    found = m.group(1)
                    offense[i]=found

            for i in range(0,dim) :
                offense[i] = offense[i].replace('\n',' ')

            #Arrst_loc
            Arrst_loc=[None] * dim
            dim = len(row)-1
            temp2=[None] * dim
            for i in range(1,dim+1) :
                m = re.search('([A-Z0-9/ .\'-]+)\n', temp[i-1])
                if m:
                    found = m.group(1)
                    Arrst_loc[i-1]=found

            #Arresti
            Arresti=[None] * dim
            dim = len(row)-1
            temp2=[None] * dim
            for i in range(0,dim) :
                m = re.search('\n([A-Z0-9=>&/ \(\).\'-]+)\n([A-Z][A-Za-z]+[ a-zA-Z]+)', temp[i])
                if m:
                    found = m.group(2)
                    Arresti[i]=found

            #Extracting arrestie Birthday
            arrestie_Birthday = [None]*dim
            arrestie_date = [None]*dim
            address1 = [None]*dim
            for i in range(1,dim+1) :
                address1[i-1] = re.findall(r'\d\d?/\d\d?/\d{4}',row[i])
                arrestie_date=address1[i-1]
                arrestie_Birthday[i-1]=arrestie_date[1]


            #ArrestieAddres
            ArrestieAddres=[None] * dim
            dim = len(row)-1
            temp2=[None] * dim
            for i in range(1,dim+1) :
                m = re.search('\d\d?/\d\d?/\d{4}\n([A-Za-z0-9. \'-]+)\n([A-Za-z\n ])*(\d{5})', row[i])
                if m:
                    found = m.group(0)
                    ArrestieAddres[i-1]=found
                else :
                    m = re.search('\d\d?/\d\d?/\d{4}\n([A-Za-z0-9\n ]+)\n', row[i])
                    if m:
                        found = m.group(0)
                        ArrestieAddres[i-1]=found

            for i in range(0,dim) :
                m = re.search('\n([A-Za-z0-9\. \'-]+)\n([A-Za-z\n ])*(\d{5})?', ArrestieAddres[i])
                if m:
                    found = m.group(0)
                    ArrestieAddres[i]=found

            for i in range(0,dim) :
                m = re.search('([A-Za-z0-9. \'-]+)\n([A-Za-z\n ])*(\d{5})?', ArrestieAddres[i])
                if m:
                    found = m.group(0)
                    ArrestieAddres[i]=found

            for i in range(0,dim) :
                ArrestieAddres[i] = ArrestieAddres[i].replace('\n',',')


            # Status
            status = [None] * dim
            for i in range(1,dim+1) :
                m = re.search('\n\d{5,10}\n([A-Za-z \(\))/-]+)', row[i])
                if m:
                    found = m.group(1)
                    status[i-1]=found
                else:
                    m = re.search('\n([A-Za-z \(\))/-]+)\n\d{4} - [A-Z][a-zA-Z]+', row[i])
                    if m:
                        found = m.group(1)
                        status[i-1]=found

            #Officer
            officer = [None] * dim
            for i in range(1,dim+1) :
    #            m = re.search('\n\d{5,10}\n([A-Za-z \(\))/-]+)\n([A-Za-z0-9 -]+)', row[i])
                m = re.search('\d{4} - [A-Z][a-zA-Z]+', row[i])
                if m:
                    found = m.group(0)
                    officer[i-1]=found

            # creating a data frame of the data extracted
            data = [None] * dim
            for i in range(0,dim):
                data[i]=[time[i],case[i],Arrst_loc[i],offense[i],Arresti[i],arrestie_Birthday[i],ArrestieAddres[i],status[i],officer[i]]

            df = pd.DataFrame(data)
            df.columns = ["time","case","arrestie_location_details","offense","arrestee","arrestie_Birthday","arrestie_address","status","officer"]
            #df = df[:-1]

            return(data)



#Creating DataBase


def createdb()  :
    db= '/tmp/Project0/normanpd'+str(np.random.randint(0,100))+'.db'
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    c.execute('''CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
    );''')

    Sqlconn.commit()
    Sqlconn.close()
    return(db)


# Inserting into DB

def populatedb(db, incidents) :
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    dim = len(incidents)
    for i in range(0,dim):
        sql = '''INSERT INTO arrests (arrest_time,case_number,arrest_location,offense,arrestee_name,arrestee_birthday,arrestee_address,status,officer) VALUES (?,?,?,?,?,?,?,?,?)'''
        val = incidents[i]
        c.execute(sql,val)
        Sqlconn.commit()
    Sqlconn.close()
    return(dim)

#Displaying Random recrods from the database
def status(db):
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    sql = '''SELECT * FROM arrests ORDER BY RANDOM()'''
    c.execute(sql)
    rows=c.fetchone()
    strin=rows[0]+"þ"+rows[1]+"þ"+rows[2]+"þ"+rows[3]+"þ"+rows[4]+"þ"+rows[5]+"þ"+rows[6]+"þ"+rows[7]+"þ"+rows[8]+"þ"
    print("\nSingle Random value :\n")
    print(rows[0]+"þ"+rows[1]+"þ"+rows[2]+"þ"+rows[3]+"þ"+rows[4]+"þ"+rows[5]+"þ"+rows[6]+"þ"+rows[7]+"þ"+rows[8]+"þ")
    return(strin)

def fulldb(db):
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    sql = '''SELECT * FROM arrests '''
    c.execute(sql)
    #rows=c.fetchall()
    #strin=rows[0]+"þ"+rows[1]+"þ"+rows[2]+"þ"+rows[3]+"þ"+rows[4]+"þ"+rows[5]+"þ"+rows[6]+"þ"+rows[7]+"þ"+rows[8]+"þ"
    rng = len(c.fetchall() )
    rows=[None]*rng
    strin=[None]*rng
    for i in range(0,rng-2) :
        rows[i]=c.fetchone()
        strin[i]=rows[i][0]+"þ"+rows[i][1]+"þ"+rows[i][2]+"þ"+rows[i][3]+"þ"+rows[i][4]+"þ"+rows[i][5]+"þ"+rows[i][6]+"þ"+rows[i][7]+"þ"+rows[i][8]+"þ"
    print("\n\nPrinting whole data base :  \n")
    for i in range(0,rng-2):
        print(strin[i])
    #for i in range(0,rng-1):

        

    #print(rows[0]+"þ"+rows[1]+"þ"+rows[2]+"þ"+rows[3]+"þ"+rows[4]+"þ"+rows[5]+"þ"+rows[6]+"þ"+rows[7]+"þ"+rows[8]+"þ")
    return(rows)


def multiple_sts(db):
    Sqlconn = sqlite3.connect(db)
    c = Sqlconn.cursor()
    sql = '''SELECT * FROM arrests ORDER BY RANDOM()'''
    c.execute(sql)
    rows=[None]*8
    strin=[None]*8
    for i in range(0,5) :
        rows[i]=c.fetchone()
        strin[i]=rows[i][0]+"þ"+rows[i][1]+"þ"+rows[i][2]+"þ"+rows[i][3]+"þ"+rows[i][4]+"þ"+rows[i][5]+"þ"+rows[i][6]+"þ"+rows[i][7]+"þ"+rows[i][8]+"þ"
    print("\n\nPrinting Multiple random vaules from same database : \n")
    for i in range(0,5):
        print(strin[i])
