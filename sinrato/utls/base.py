from django.db import models

class basemodel(models.model):
    created = models.DateTimeField(auto_now_add=True),
    update = models.DateTimeField(auto_now=True)


class meta:
    abstract = True
    