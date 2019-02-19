# cs5293sp19-project0
Madhumitha Pachapalayam Sivasalapathy

Run the code :

	"pipenv run python -m pytest" is used to test all the test cases.
	"pipenv run python" is used to run python and from that we can import project0 and can run our modules
	"project0.ran_status" will run the random status module.

Please refer the saved files in the following location :

	Database is stored in \tmp\Project0\normanpd.db .
	Pdf is stored in \tmp\Project0\Arrest.pdf  .

Modules:
	Created the following module

	1.Download the data : Where pdf is downloaded from the url "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-13%20Daily%20Arrest%20Summary.pdf"

	2.Extract the fields : Tried various functions to extract data from pdf but resulted in poorly formated data. So solved it using "re package". Regular expression makes it easier. 	

	3.Create a SQLite database to store the data named normanpd.db
	
	4.Insert into SQLite table : from the previous module extacted the table and inserted records into the table arrets.

	5.Random arrest : Returned one random arrest by querying the normanpd.db at a time. 

Reference:

	"http://normanpd.normanok.gov/content/daily-activity" - from which the website was downloaded.
	"https://docs.python.org" - Used the website for python usage.
	Used assignment0's test modules to construct testcases. 





