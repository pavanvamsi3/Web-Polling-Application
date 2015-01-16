from django.http import HttpResponse
from django.views import generic
import mysite.settings

class MainIndexView(generic.ListView):
	template_name = 'mysite/main.html'
	context_object_name = "apps_list"

	def get_queryset(self):
		apps = (mysite.settings.INSTALLED_APPS)
		user_apps = []
		for app in apps:
			if(app.startswith("django")):
				continue
			else:
				user_apps.append(app)
		return user_apps
      