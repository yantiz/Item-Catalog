# Item Catalog
- This project builds a basic website that allows users to log in via their Google accounts as well as add, edit, and delete their own items under each category.
- In addition to their own items, users are allowed to check out fellow users' items by click the relevant links.
- The names of each category and item are unique and used as primary keys in the database.
- The JSON endpoint for this site is implemented and could be accessed through the URL `http://localhost:8000/catalog/json`.


## Technologies that are used
- Front End: Jinja2
- Web Framework: Flask
- Form Submission: WTForms
- Backend: SQLAlchemy

## To play around with this project locally
1. Download and install the [virtual machine](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip) using **Vagrant** and **VirtualBox** (or other equivalent tools).
2. Download the source files of the project put them into the folder named `catalog`, which is under the path `/vagrant` of the virtual machine.
3. Download and install other dependencies for this project using the commands `pip install Flask-SQLAlchemy` and `pip install Flask-WTF` (Note: You might need to append
`sudo` before the commands for permission concerns.)
4. Navigate into the folder `catalog`. Then set up the database and add some predefined categories into the database using the commands `python database_setup.py` and 
`python add_categories.py`. You are welcomed to define more categories by adding more code into `add_categories`.
5. Finally, you are able to run this project by typing `python project.py`. Have fun.
