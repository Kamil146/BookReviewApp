from django.contrib import admin
from .models import  Review,Category,Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('id','publication_date')
admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Review,ReviewAdmin)