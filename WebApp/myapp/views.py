from django.db.models import Q
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        search = request.query_params.get('search','')
        category = request.query_params.get('category','')
        if search:
            title_q=Q(title__contains=search)
            author_q = Q(author__contains=search)
            books=books.filter(title_q | author_q)
        if category:
            books = books.filter(category__name__icontains=category)
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE'])
def book(request,id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)