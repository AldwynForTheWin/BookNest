from django.contrib import admin
from booksys.models import Publisher, Department, Category, Author, Book

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'author', 'publisher','category')
	list_filter = ['pub_date']
	search_fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('lastname', 'firstname', 'middlename', 'department')

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'contact_no')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'contact_no')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('acronym', 'description')

# 	fieldsets = [
# 		('Edit Book Title', {'fields': ['title']}),
# 		('Edit Book Infos', {'fields': ['pub_date', 'author', 'publisher', 'category'], 'classes': ['collapse']})
# 	]
# 	inlines = [AuthorInline, DepartmentInline, PublisherInline, CategoryInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)