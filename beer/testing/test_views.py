from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.test import TestCase
from beer.models import *

class ViewTest(TestCase):
	
	def setUp(self):
		'''allocated a variable to class object of models and created instance of User Model'''
		self.user = User.objects.create(username='test')
		self.brewery = Brewery.objects.create(name='Coors Golden Brewery', slug='coors-golden-brewery', description='Great Brewery')
		self.brewery2 = Brewery.objects.create(name='Anheiser Busch', slug='anheiser-busch', description='Great Brew')
		self.beer = self.create_beer('Coors Light', 'coors-light', self.brewery)
		self.beer2 = self.create_beer('Budweiser','budweiser', self.brewery2)
		
	def create_beer(self, name, slug, brewery):
		'''Function that creates an instance of beer model '''
		return Beer.objects.create(name=name, slug=slug, brewery=brewery, localilty='I', description="Great Brew", image1="/img/beerthumbs/60-Min-IPA")
		
	def test_Beers_All(self):
		'''Tests Beers All View'''
		url = '/beers/'
		req = self.client.get(url)
		self.assertEqual(req.status_code, 200)
		self.assertTemplateUsed(req, 'beersall.html')
		self.assertIn( self.beer.image1.url , req.content)
		self.assertIn( 'href="coors-light"' , req.content)
		self.assertIn('Budweiser', req.content)
		
	def test_single_beer(self):	
		'''Test Single Beer's View '''
		url = '/beers/coors-light/'
		req = self.client.get(url)
		self.assertEqual(req.status_code, 200)
		self.assertTemplateUsed(req, 'singlebeer.html')
		self.assertIn( 'href="/brewerys/coors-golden-brewery"' , req.content)
		self.assertIn('Import', req.content)
		
	def test_single_brewery(self):
		''' Test Single Brewery View '''
		url = '/brewerys/coors-golden-brewery/'
		req = self.client.get(url)
		self.assertEqual(req.status_code, 200)
		self.assertTemplateUsed(req, 'singlebrewery.html')
		self.assertNotIn('href="/beers/budweiser"', req.content)
		self.assertIn('href="/beers/coors-light"', req.content)
		
		
		
		
		