from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    bookno=models.IntegerField(primary_key = "bookno");
    bookname=models.CharField(max_length = 20);
    authorname=models.CharField(max_length = 25);
    bookrate=models.IntegerField();
    rating=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
      list_display=("bookno","bookname","authorname","bookrate","rating");



























