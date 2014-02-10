from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.test import TestCase
from beer.models import Brewery, Beer

#Tests that you could create an instance of the Brewery Model
class BreweryTest(TestCase):

	def setUp(self):
		'''Creates an instance of a user'''
		self.user = User.objects.create(username='test')

	def create_brewery(self):
		'''Creates an instance of the Brewery Model '''
		return Brewery.objects.create(name="Coors Golden Brewery",
		slug = "coors-golden-brewery",
		description="Freshly Made Brew")

	def create_beer(self):	
	
		brew = self.create_brewery()
		
		return Beer.objects.create(name="Coors Light",slug="coors-light",brewery=brew,localilty="D",description="a great beer",image1="budlight")
	
	def test_model_url(self):
		brewery = self.create_brewery()
		#Checks if the object brewery is an instance of the Brewery Model	
		self.assertTrue(isinstance(brewery, Brewery))
		#Check if a slug is created from name when no slug is given
		self.assertEqual(brewery.slug, 'coors-golden-brewery')	
	
	def test_beer_model(self):
		beer = self.create_beer()
		self.assertTrue(isinstance(beer, Beer))
		self.assertEqual(beer.localilty, "D")
		
		
		
		
		
		