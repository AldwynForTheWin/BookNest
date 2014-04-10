from django.contrib import admin
from booksys.models import Publisher, Department, Category, Author, Book

# class BookSysAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		('Edit Book Title', {'fields': ['title']}),
# 		('Edit Book Infos', {'fields': ['pub_date', 'author', 'publisher', 'category'], 'classes': ['collapse']})
# 	]
# 	inlines = [AuthorInline, DepartmentInline, PublisherInline, CategoryInline]

admin.site.register(Book)