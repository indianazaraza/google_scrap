# README.md
A web scraper on google news. The code takes titles from the first twenty news items.

Execute google_news.py with crontab on Linux:

1. Create a file .sh at same level as the file .py 

2. Then write:

~~~
!# bin/bash

cd /your/path
python3 google_news.py
~~~

3. Give execute permissions with **chmod +x file.sh**

4. Execute in the terminal **crontab -e**, choose an editor and write: 
~~~
09*** /your/path/file.sh
~~~
The file.sh will run execute every day of the year at 9 PM

- First star = day of the month

- Second star = month of the year

- Third star = day of the week

5. Save and exit
