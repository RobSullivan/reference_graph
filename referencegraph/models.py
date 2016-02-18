from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=500)
	pmid = models.CharField(max_length=50)


class Author(models.Model):
	name = models.CharField(max_length=100)


class Journal(models.Model):
	pass


class ArticleReferences(models.Model):
	pass
