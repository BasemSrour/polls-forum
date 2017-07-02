from django.contrib import admin

from .models import Post, Reply

# Register your models here.
class ReplyInLine(admin.TabularInline):
	model = Reply
	extra = 3

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['post_text']}),
	('Date and time information', {'fields': ['pub_date']}),
	]
	inlines = [ReplyInLine]
	list_display = ('post_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Post, PostAdmin)
