from django.db import models


# Create your models here.

class orderp(models.Model):
    
    title=models.CharField(max_length=255,verbose_name='Title of the your order',help_text='max character limit 255')
    description=models.TextField(verbose_name='your user description')
    fullname= models.CharField(max_length=20,verbose_name='Your name(Author)',help_text='max 20 character ')
   

    class Meta:
        verbose_name='orderpost' 
        verbose_name_plural='All Movie Posts'

    def __str__(self):
        return self.title
    