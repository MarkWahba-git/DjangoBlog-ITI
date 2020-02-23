# pyblog
A simple Blog using Python Django and MySQL  

# Config 
Initial your database by :
  1) create a db in your mysql server called 'pyblog' : 
    open terminal :
      ```
        mysql -u root -p 
        <your passowd>
        create database pyblog;
        \q
      ```
  2) open the shell and config the db:
  ```
    python manage.py makemigration
    python manage.py migrate
  ```

