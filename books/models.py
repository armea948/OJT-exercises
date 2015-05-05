from django.db import models
from django.utils import timezone
import datetime


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    phone = models.CharField(max_length=20, default=9999)
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    def get_full_name(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    description = models.TextField(default="")
    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        date_today = timezone.now().date()
        return self.publication_date >= date_today - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
