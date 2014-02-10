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
		'''Creates an instance of the Beer Model '''
		brew = self.create_brewery()
		return Beer.objects.create(name="Coors Light",slug="coors-light",brewery=brew,localilty="D",description="a great beer",image1="budlight")
	
	def test_brewery_model(self):
		'''Test if object is an instance of our brewery model and if the object's attributes are correct'''
		brewery = self.create_brewery()	
		self.assertTrue(isinstance(brewery, Brewery))
		self.assertEqual(brewery.slug, 'coors-golden-brewery')	
	
	def test_beer_model(self):
		'''Test if object is an instance of our brewery model and if the object's attributes are correct'''
		beer = self.create_beer()
		self.assertTrue(isinstance(beer, Beer))
		self.assertEqual(beer.localilty, "D")
		
		
		
		
		
		