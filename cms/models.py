from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):
    '''書籍'''
    name = models.CharField(u'書籍名', max_length=255)
    publisher = models.CharField(u'出版社', max_length=255, blank=True)
    page = models.IntegerField(u'ページ数', blank=True, default=0)

    def __str__(self):    # Python2: def __unicode__(self):
        return self.name

class User(models.Model):
    '''ユーザ'''
    name = models.TextField(u'ユーザ名', blank=False)
    age = models.IntegerField(u'年齢', blank=True)
    def __str__(self):
       return self.name

class Impression(models.Model):
    '''感想'''
    user = models.ForeignKey(User, verbose_name=u'ユーザ', related_name='impressions',default=1)
    book = models.ForeignKey(Book, verbose_name=u'書籍', related_name='impressions')
    comment = models.TextField(u'コメント', blank=True)
    star = models.IntegerField(u'評価', blank=False, default=1, validators=[MaxValueValidator(5),MinValueValidator(1)])

    def __str__(self):    # Python2: def __unicode__(self):
        return self.comment

