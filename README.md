# cs5293sp19-project0
Madhumitha Pachapalayam Sivasalapathy

Run the code :

	"pipenv run python -m pytest" is used to test all the test cases.(read hard coded pdf and does all the tests)
	"pipenv run python project0/main.py --arrests <url>" is used to run project0 and can run our modules

Please refer the saved files in the following location :

	Database is stored in \tmp\Project0\*.db .
	Pdf is stored in \tmp\Project0\Arrest*.pdf  .

Modules:
	Created the following module

	1.Download the data : Where pdf is downloaded from the url "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-16%20Daily%20Arrest%20Summary.pdf". 
	Also downloaded various dates of the pdf for training. url extraction was similar to the extraction from assignment0 and was very helpful 

	2.Extract the fields : Tried various functions to extract data from pdf but resulted in poorly formated data.
	So solved it using "re package". Regular expression makes it easier. It was a hard part. 
	It has various complications like missing values and multiline values. 
	Each row was extracted using ';' and the each field is extrated via regular expression. 
	3 columns arrestee location, offence and arrestee was hard to seperate. but using regular expression it was easier. 	

	3.Create a SQLite database to store the data named normanpd.db. It takes 9 fields.
	
	4.Insert into SQLite table : from the previous module extacted the table and inserted records into the table arrets by combining data from incidents..

	5.Random arrest : Returned one random arrest by querying the database by seperating each fields with thorn symbol. 
	
	6.Multiple status : Added one more module to print multiple random queries from the database


Test cases: Unit testing is done for every module

	* Test case 1: To check url fetch it was implemented. [Warning : it might not work if the url containing the page expired.]
	* Test case 2: This test will check Each fields are extracted from the pdf and missing values,cleaning are handled properly.
	* Test case 3: Verifies the creation of the database.
	* Test case 4: This one verifies that no. of incidents is equal to no. of data in the database thus ensuring every row is inserted properly.
	* Test case 5: To verify the status module is displayting random results.


Reference:

	"http://normanpd.normanok.gov/content/daily-activity" - from which the website was downloaded.
	"https://docs.python.org" - Used the website for python usage.
	Used assignment0's test modules to construct testcases.

