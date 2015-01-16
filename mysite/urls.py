from django.conf.urls import patterns, include, url
from mysite import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', reverse(admin.site.urls), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.MainIndexView.as_view(), name='main_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
)
