from django.contrib import admin
from polls.models import Poll, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class PollAdmin(admin.ModelAdmin):
	
	#This display the list 
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	#This just display's question field in the change list page
	"""fieldsets = [
	    ('Question Field',        {'fields' : ['question']}),
	    ('Date information', {'fields' : ['pub_date']}),

	]"""
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
