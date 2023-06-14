from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.books_list),
    path ('book/<int:id>',views.book),
    path('reviews/',views.review_list),
    path('review/<int:id>',views.review_add)
]