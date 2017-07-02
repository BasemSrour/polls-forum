from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [
		# ex: /forum/
		url(r'^$', views.IndexView.as_view(), name = 'index'),
		# ex: /forum/5/ for post details
		url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
		# ex: /forum/5/results for results
		url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results'),
		# ex: /forum/5/vote for voting
		url(r'^(?P<post_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
]