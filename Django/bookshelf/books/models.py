from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    biography = models.TextField(default=0)


    def get_full_name(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    edition = models.IntegerField(default=0)
    isbn = models.CharField(max_length=40)
    def __unicode__(self):
        return self.title
