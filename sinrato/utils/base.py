from django.db import models

class basemodel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
      