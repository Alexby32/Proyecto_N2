from datetime import date
from pyexpat import model
from time import time
from unicodedata import name
from django.db import models

# Create your models here.
class login (models.Model):
    name = models.CharField(max_length=30);
    password = models.CharField(max_length=25);
    
class usuario (models.Model):
    id_user = models.IntegerField(primary_key = True);
    name = models.CharField(max_length=30);
    address = models.CharField(max_length=10);
    email = models.CharField(max_length=25);
    phone = models.CharField(max_length=10);
    user = models.CharField(max_length=20);
    password = models.CharField(max_length=20);
    
class genre (models.Model):
    id_genre = models.IntegerField(primary_key = True);
    description = models.CharField(max_length=25); 
    
class movie (models.Model):
    id_movie = models.IntegerField(primary_key = True);
    name_movie = models.CharField(max_length=25);
    gender = models.CharField(max_length=25);
    year = models.IntegerField();
    duration =  models.CharField(max_length=5);
    id_genre =  models.ForeignKey ('genre', on_delete = models.CASCADE);
    
class time (models.Model):
    id_time = models.IntegerField(primary_key = True); 
    date = models.DateField ();
    time = models.CharField(max_length=10);
    id_movie = models.ForeignKey ('movie', on_delete = models.CASCADE);
 
class room (models.Model):
    id_room = models.IntegerField(primary_key = True);
    name_room = models.CharField(max_length=25)
    total_seats = models.IntegerField();
    id_time = models.ForeignKey
 
class reservation (models.Model):
    idResevation = models.IntegerField(primary_key = True);
    language_movie = models.CharField(max_length=25);
    duration = models.CharField(max_length=25);
    seating = models.CharField(max_length=25);
    location = models.CharField(max_length=25);
    id_user = models.ForeignKey ('usuario', on_delete = models.CASCADE);
    id_movie = models.ForeignKey ('movie', on_delete = models.CASCADE);
    id_room = models.ForeignKey ('room', on_delete = models.CASCADE);
    

class bill (models.Model):
    id_bill = models.IntegerField(primary_key = True);
    date  = models.DateField();
    total = models.FloatField();
    paymentMethod =  models.CharField(max_length=20);
    id_user = models.ForeignKey ('usuario', on_delete = models.CASCADE);

class invoiceDetail (models.Model):
    id_invoiceDetail = models.IntegerField(primary_key = True);
    quantity = models.IntegerField ();
    id_bill = models.ForeignKey ('bill', on_delete = models.CASCADE);
    id_reservation = models.ForeignKey ('reservation', on_delete = models.CASCADE);