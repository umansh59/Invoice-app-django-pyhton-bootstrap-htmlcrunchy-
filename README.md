 Invoice-app-django-pyhton-bootstrap-htmlcrunchy-

 create an environment using conda 
 install pyhthon 3 
 install pip3
 install django 
 install crunchy 
 install registration redux 
 install pandas 
 intall crispy forms 
 intall reportlab
 intall crispy_bootstrap5
 intall mysqlclient
all the below commands will run in the location of manage.py in the src folder 
To create a new  super user 
run command : python manage.py createsuperuser 

before starting  edit the mysql database settings and install mysql connector for the python 
and run commands :
python manage.py makemigrations 
python manage.py migrate 

to run the django server run command :
python manage.py runserver 

not working features 
the recent invoices tab in the new invoice page you can also exclude completely its on preference
the genrated invoice still prints none or 0 in the emppty fields 
the no of fields is not dynamic atmost i can add 10 entries per bill 
