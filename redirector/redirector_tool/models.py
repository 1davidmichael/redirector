from django.db import models

# Create your models here.
class Redirect(models.Model):
    domain = models.CharField(max_length=200)
    source_url = models.CharField(max_length=200)
    destination_url = models.CharField(max_length=200)
    expiration_date = models.DateField('date expires')
    comment = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.source_url
