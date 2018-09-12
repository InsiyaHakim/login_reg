# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt
import datetime

# Create your models here.

class UserManager(models.Manager):
    def creating_db(self,form_data):

        f_name=str(form_data['f_name'])
        l_name=str(form_data['l_name'])
        email=str(form_data['email'])
        b_day=str(form_data['b_day'])
        password=str(form_data['password'])
        c_password=str(form_data['confirm'])

        error=[]
        if str.isalpha(f_name) == False or str.isalpha(l_name) == False:
            error.append("First and Last name should'nt have any digit(s)")
        if len(f_name) <= 2:
            error.append("First Name should be atleast 8 characters")
        if len(l_name) <= 2:
            error.append("Last Name should be atleast 8 characters")
        if len(b_day) == 0:
            error.append("Enter your birth date!!!")
        if not EMAIL_REGEX.match(email):
            error.append("Email is not valid")
        if len(password)<= 2:
            error.append("Password must be 8 character(s)")
        if password != c_password:
            error.append("password confirmation is incorrect")

        date_of_birth = str(datetime.datetime.strptime(b_day, "%Y-%m-%d")).split()[0]
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        if date_of_birth == today:
            error.append("You cannot Enter Today's date!!!!")

        user = self.filter(email=email)
        if len(user) != 0:
            error.append("Invalid Email")

        if len(error)>0:
            return error
        else:
            fname = f_name.capitalize()
            lname = l_name.capitalize()
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            self.create(f_name=fname,l_name=lname,email=email,password=hash1,b_day=b_day)
            return error

    def logging(self,form_data):
        error=[]
        email=str(form_data['email'])
        password=str(form_data['password'])
        user=self.filter(email=email)
        if len(user) == 0:
            error.append("Invalid Email")
            return error

        p_check=user[0]
        if not bcrypt.checkpw(password.encode(), p_check.password.encode()):
            error.append("Invalid Password!!!")
            return error
        else:
            return p_check.id


    def selecting_user(self,user_id):
        check=User.object.get(id=user_id)
        context={
            "user":check
        }
        return context

class User(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=500)
    b_day=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    object=UserManager()