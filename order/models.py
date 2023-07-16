from django.db import models


# Create your models here.

class orderp(models.Model):
    GENRE=(

        (0,'Choose'),
        (1,'Sci-fil'),
        (2,'adventure'),
        (3,'Dram')
        
    )

    title=models.CharField(max_length=255,verbose_name='Title of the your order',help_text='max character limit 255'),
    description=models.TextField(verbose_name='your user description'),
    fullname= models.CharField(max_length=20,verbose_name='Your name(Author)',help_text='max 20 character ')
    imdb =models.DecimalField(max_digits=5,decimal_places=2,verbose_name='order py')
    is_adviced=models.BooleanField(default=True,verbose_name='do you like  this order')
    genre=models.IntegerField(choices=GENRE,default=0,verbose_name='Genre of you order')

    class Meta:
        verbose_name='orderpost' 
        verbose_name_plural='All Movie Posts'

    def __str__(self):
        return self.title
    