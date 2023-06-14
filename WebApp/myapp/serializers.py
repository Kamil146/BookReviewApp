from rest_framework import serializers
from .models import Book,Category,Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all(),many=True)
    class Meta:
        model = Book
        fields = ['id','title','author','summary','publisher','category']

class ReviewSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title',read_only=True)
    publication_datetime = serializers.DateTimeField(source='publication_date',format="%Y-%m-%d %H:%M:%S",read_only=True)
    class Meta:
        model =Review
        fields = ['id','rating','comment','publication_datetime','book_title']