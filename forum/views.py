from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Post, Reply

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'forum/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):
		"""Return the last five published posts"""
		return Post.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Post
	template_name = 'forum/detail.html'

class ResultsView(generic.DetailView):
	model = Post
	template_name = 'forum/results.html'

def vote(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	try:
		selected_reply = post.reply_set.get(pk=request.POST['reply'])
	except (KeyError, Reply.DoesNotExist):
		# Redisplay the post replying form
		return render(request, 'forum/detail.html', {'post': post, 'error_message': "You didn't select a reply", })
	else:
		selected_reply.votes_for_reply += 1
		selected_reply.save()
		# Alaways return HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if an user hits the Back button
		return HttpResponseRedirect(reverse('forum:results', args=(post.id,)))