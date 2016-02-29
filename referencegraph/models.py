from django.db import models

class Journal(models.Model):
	title = models.CharField(max_length=100)
	doi_prefix = models.CharField(max_length=50)

class Article(models.Model):
	article_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=500)
	pmid = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	journal = models.ForeignKey(Journal)
	article_reference_id = models.IntegerField()



class ArticleReferences(models.Model):
	article_reference_id = models.ForeignKey(Article)
	article_id = models.ForeignKey(Article)
