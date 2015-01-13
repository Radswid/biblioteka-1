# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Author(models.Model):
    first_name = models.CharField('Imię', max_length=50)
    last_name = models.CharField('Nazwisko', max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __unicode__(self):
        return self.last_name

class Genre(models.Model):
    genre_main = models.CharField('Gatunek', max_length=50)

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

    def __unicode__(self):
        return self.genre_main


    
class Book(models.Model):
    title = models.CharField('Tytuł', max_length=50)
    author = models.ForeignKey(Author)
    about = models.TextField('Opis')
    genre = models.ForeignKey(Genre, verbose_name="Gatunek")
    user = models.ForeignKey(User, verbose_name="Wypożyczył", null=True, blank=True)
    state = models.BooleanField('Wypożyczona')
    date = models.DateField('Data oddania', null=True, blank=True)

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __unicode__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User)
    p_number = models.BigIntegerField('Pesel', max_length=11)
    street = models.CharField('Ulica', max_length=50)
    nr_house = models.IntegerField('Numer domu', max_length=5)
    nr_flat = models.IntegerField('Numer mieszkania', null=True, blank=True, max_length=5)
    post_code = models.CharField('Kod pocztowy', max_length=6)
    city = models.CharField('Miejscowość', max_length=20)
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __unicode__(self):
        return self.user.username
    
    
