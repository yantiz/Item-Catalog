# Item Catalog
- This project builds a basic website that allows users to log in externally via their Google accounts as well as add, edit, and delete their own items under each category.
- In addition to their own items, users are allowed to check out fellow users' items by click relevant links.
- The names of each category and item are unique and used as primary keys in the database.
- The correct versions of dependencies are included in `requirements.txt`.


## Technologies that are used
- Front End: Jinja2
- Web Framework: Flask
- Form Submission: WTForms
- Backend: SQLAlchemy
- Authentication and Authorization: AJAX and Google OAuth 2.0

## Instruction on how to connect to my app's webpage through browsers
This project is currently hosted by a Apache HTTP Server supported by Amazon Web Service (AWS).
[Click me](http://ec2-35-167-117-224.us-west-2.compute.amazonaws.com/) to see the hosted app.

## To play around with this project locally
1. Download the [virtual machine](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip) using **Vagrant** and **VirtualBox** (or other equivalent tools).
2. Download the source files of the project and put them into the folder named `catalog` of the downloaded virtual machine.
3. Go back one level to the folder `vagrant` and then get the virtual machine running by typing the commands `vagrant up` and `vagrant ssh`. Make sure you've already 
installed **Vagrant** and **VirtualBox** (or other equivalent tools) before running the virtual machine.
4. Inside the environment of the virtual machine, navigate to the path `/vagrant/catalog` and install other dependencies for this project using the commands
`pip install Flask-SQLAlchemy` and `pip install Flask-WTF` (Note: You might need to append `sudo` before the commands for some permission concerns.)
5. Configure the database and subsequently add some predefined categories into the database using the commands `python database_setup.py` and `python add_categories.py`. You are welcomed to define more categories for this project by adding more code into `add_categories.py`.
6. Finally, you are able to run this project by typing `python project.py`. When you want to finish, type `CTRL-C` to quit the project and type `exit` and `vagrant halt` to
terminate the virtual machine.
