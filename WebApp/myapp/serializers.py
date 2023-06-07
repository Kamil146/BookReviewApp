from rest_framework import serializers
from .models import Book,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all(),many=True)
    class Meta:
        model = Book
        fields = ['id','title','author','summary','publisher','category']