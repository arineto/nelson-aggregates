from django.db import models
from django.contrib.auth.models import User


QUARRY_NAMES = (
		(1, 'Burlington Quarry'),
		(2, 'Waynco Aggregate'),
		(3, 'Uhthoff Quarry'),
		(4, 'Oneida Quarry'),
		(5, 'Lincoln Quarry'),
		(6, 'Lafarge'),
	)


class Price(models.Model):
	quarry = models.IntegerField(max_length=1, choices=QUARRY_NAMES, verbose_name='Quarry')
	tri_axel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Tri Axle', null=True, blank=True)
	tractor_trailer = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Trailer', null=True, blank=True)
	stone_slinger = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Stone Slinger', null=True, blank=True)


class Polygon(models.Model):
	points = models.CharField(max_length=100000)
	title = models.CharField(max_length=10)
	color = models.CharField(max_length=7)
	prices = models.ManyToManyField('Price', null=True, blank=True)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title


class Quarry(models.Model):
	name = models.CharField(max_length=100)
	delivery_address = models.CharField(max_length=200)
	mailing_address = models.CharField(max_length=200)
	office = models.CharField(max_length=15)
	toll = models.CharField(max_length=15)
	fax = models.CharField(max_length=15)
	sales = models.CharField(max_length=50)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	pin = models.FileField(upload_to="quarries_pins/", null=True, blank=True, verbose_name="Pin")

	def __unicode__(self):
		return self.name


class AccessInfo(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.user.username


class PDF(models.Model):
	name = models.CharField(max_length=50, verbose_name="PDF's Name")
	pdf = models.FileField(upload_to="pdfs/", verbose_name="Pin")


class Area(models.Model):
	area = models.CharField(max_length=50, verbose_name="Area")
	color = models.CharField(max_length=7, verbose_name="Color (Hexadecimal)")


class LoginPicture(models.Model):
	picture = models.FileField(upload_to="login_pictures/")