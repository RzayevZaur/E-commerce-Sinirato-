from django.db import models


# Create your models here.

class corep(models.Model):
    GENRE=(

        (0,'Choose'),
        (1,'Sci-fil'),
        (2,'adventure'),
        (3,'Dram')
        
    )

    title=models.CharField(max_length=255,verbose_name='Title of the your core',help_text='max character limit 255'),
    description=models.TextField(verbose_name='your user description'),
    fullname= models.CharField(max_length=20,verbose_name='Your name(Author)',help_text='max 20 character ')
    imdb =models.DecimalField(max_digits=5,decimal_places=2,verbose_name='core py')
    is_adviced=models.BooleanField(default=True,verbose_name='do you like  this core')
    genre=models.IntegerField(choices=GENRE,default=0,verbose_name='Genre of you core')

    class Meta:
        verbose_name='blogpost' 
        verbose_name_plural='All Movie Posts'

    def __str__(self):
        return self.title
    