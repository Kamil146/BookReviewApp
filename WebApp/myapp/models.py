from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title= models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    summary=models.TextField()
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.title
class Review(models.Model):
    RATING_OPTIONS = ( (1,1),(2,2),(3,3),(4,4),(5,5),(6,6))
    rating = models.IntegerField(choices=RATING_OPTIONS)
    comment = models.TextField()
    publication_date = models.DateTimeField('Published on:', auto_now=True)
    book = models.ForeignKey(Book,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.book.title + ' review'