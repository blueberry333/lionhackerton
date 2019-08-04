from django.db import models

from django.conf import settings

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

