from django.db import models
from sinrato.utils.base import basemodel


# Create your models here.

class moviep(models.Model):


    title=models.CharField(max_length=255,verbose_name='Title of the your user',help_text='max character limit 255')
    fullname= models.CharField(max_length=20,verbose_name='Your name(Author)',help_text='max 20 character ')
    is_adviced=models.BooleanField(default=True,verbose_name='do you like  this film')

 

    class Meta:
        verbose_name='MoviePost'
        verbose_name_plural='All Movie Posts'

    def __str__(self):
        return self.title
    