from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	contact_no = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=255)
	contact_no = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	acronym = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.acronym

class Author(models.Model):
	firstname = models.CharField(max_length=255)
	middlename = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	department = models.ForeignKey(Department)
	def __unicode__(self):
		return self.lastname + ', ' + self.firstname

class Book(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(Author)
	publisher = models.ForeignKey(Publisher)
	category = models.ForeignKey(Category)
	def __unicode__(self):
		return self.title