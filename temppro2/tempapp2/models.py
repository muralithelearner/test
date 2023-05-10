from django.db import models

#class Boysdata(models.Model): here models.Model not from python its import from django that's why we gives as a mother class name
#before we connect the models to database chek the connect to tempapp2 in and database name in setting.py
#python manage.py makemigrations  ==> is used for convert the ORM language to SQL language with the help of pymysql store in mogration folder(as a SQL code)
#python manage.py migrate         ==> is used for take the modify data from the migration folder file(0001) to database 

class Boysdata(models.Model):     # Boysdata is the (Table name)
    name=models.CharField(max_length=15)
    from_city=models.CharField(max_length=15)
    living_purpose=models.CharField(max_length=15)
    occupation=models.CharField(max_length=10)
    starting_date=models.DateField()
    sharig_required=models.IntegerField()

class Service(models.Model):
    shift=models.CharField(max_length=10)
    monday=models.CharField(max_length=10)
    tuesday=models.CharField(max_length=10)
    wednesday=models.CharField(max_length=10)
    thursday=models.CharField(max_length=10)
    friday=models.CharField(max_length=10)
    saturaday=models.CharField(max_length=10)
    sunday=models.CharField(max_length=10)
    

class Hostelboysdata(models.Model):
    name=models.CharField(max_length=25)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50,blank=True)
    block=models.CharField(max_length=5)
    share_members=models.IntegerField()
    room_no=models.IntegerField()
    joining_date=models.DateField()
    rent=models.IntegerField()
    image=models.ImageField(upload_to='images/')

