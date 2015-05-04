from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
