from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInLine(admin.TabularInline):
	"""Choice in line"""
	model = Choice
	extra = 3
		

class PollAdmin(admin.ModelAdmin):
	"""Poll Admin"""
	# fields = ['pub_date', 'question']
	fieldsets = [('Text Fields', {'fields':['question']}),
		('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
	]
	inlines = [ChoiceInLine]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)

