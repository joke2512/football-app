# football-app
Football webapp, located at:
http://footballapp-env.eba-kidmyeuu.eu-central-1.elasticbeanstalk.com/


## Structure
#### `dbInit.py`
Initializes the database - creating the table and inserting the data.
#### `wsgi.py`
Routing interface, etc.
#### `views.py`
Functions to create views.
#### `ultils.py`
Utility functions.
#### `templates`
Folder with template files. Python files that return an html string when called.



## Comments on funcionality
### Teambuilder
The teambuilder funcitonality is not working in the hosted version, I had some issues with the deployement.
The file `teambuilderLOCAL.py` can be used to test this funcitonality.
### Pictures
The pictures in the dataset all returns a 404 error, so no pictures will be displayed on the page.

