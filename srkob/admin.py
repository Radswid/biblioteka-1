# -*- coding: utf-8 -*-
from django.contrib import admin
from srkob.models import Author, Book, Genre, Profile


class BookAdmin(admin.ModelAdmin):
    fieldsets =[(None, {'fields': ['title', 'author', 'genre', 'about']}),('Informacje o wypożyczeniu',{'fields': ['user', 'date', 'state'], 'classes': ['collapse']}),]
    list_display = ('title', 'genre', 'user','date' ,'state')


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Profile)
