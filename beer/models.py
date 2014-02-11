from django.db import models

BEER_CHOICES = (
    ('D', 'Domestic'),
    ('I', 'Import'), 	
)

class Brewery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name	

class Beer(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brewery = models.ForeignKey(Brewery, related_name='beers') 	
    localilty = models.CharField(max_length=1, choices=BEER_CHOICES)
    description = models.TextField(blank=True)
#    image1 = models.ImageField(upload_to="img/beerthumbs", null=True, blank=True, max_length=100, help_text="50x180px image" )

    def __unicode__(self):
        return self.name


