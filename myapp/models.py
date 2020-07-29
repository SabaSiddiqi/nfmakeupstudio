from django.db import models
from django import forms
from django import forms
from .models import *

#Createyourmodelshere.

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

class coverPhoto(models.Model):
    coverPhoto_name = models.CharField(max_length=50)
    coverPhoto_image = models.ImageField(upload_to='images/')

class portfolioPhoto_makeup(models.Model):
    portfolioPhoto_makeup_name = models.CharField(max_length=50)
    portfolioPhoto_makeup_image = models.ImageField(upload_to='images/makeup/')
    portfolioPhoto_makeup_heading = models.CharField(max_length=50, blank=True)
    portfolioPhoto_makeup_caption = models.CharField(max_length=100, blank=True)
    STATUS_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),)
    portfolioPhoto_makeup_column = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')


class portfolioPhoto_hairdo(models.Model):
    portfolioPhoto_hairdo_name = models.CharField(max_length=50)
    portfolioPhoto_hairdo_image = models.ImageField(upload_to='images/hairdo/')
    portfolioPhoto_hairdo_heading = models.CharField(max_length=50, blank=True)
    portfolioPhoto_hairdo_caption = models.CharField(max_length=100, blank=True)
    STATUS_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),)
    portfolioPhoto_hairdo_column = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')

class portfolioPhoto_henna(models.Model):
    portfolioPhoto_henna_name = models.CharField(max_length=50)
    portfolioPhoto_henna_image = models.ImageField(upload_to='images/henna/')
    portfolioPhoto_henna_heading = models.CharField(max_length=50, blank=True)
    portfolioPhoto_henna_caption = models.CharField(max_length=100, blank=True)
    STATUS_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),)
    portfolioPhoto_henna_column = models.CharField(max_length=1,choices=STATUS_CHOICES, default='1')

class services(models.Model):
    services_name = models.CharField(max_length=50)
    services_description = models.CharField(max_length=100)

class html_info(models.Model):
    value_1 = models.CharField(max_length=50)
    value_2 = models.CharField(max_length=100)

