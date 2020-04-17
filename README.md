# password-generator-with-sqlite3
This is a Python project that uses tkinter GUI and SQLite3.

Perform the following:
1. Save the file in a location. Make that as your working directory.
2. Make sure db.py is in the same library as the generate_pwd.py.
3. Run generate_pwd.py script.
4. You will see a window as shown in Image Window 1.png
5. Select the complexity of password by selecting the length of the password you wish to generate.
6. Give Application Name and Email Id, for which you wish to generate the password.
7. Click on Generate Password button.
8. Your password will appear in a new window.


# Module db.py
1. import sqlite3
2. Function db_create_database() is used to create a database app_pwd.db (if not created already, else it connects to it)
3. Function db_create_table() is used to create a table application_password table (if not exists already)
4. Function insert() is used to insert data into the table.
5. Function select() is used to select the rows from the table.
