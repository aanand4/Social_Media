from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.

def home(request):
	request.session.set_expiry(300)
	context = {'posts':Post.objects.all()}
	return render(request, 'accounts/index.html', context)

"""

def post_detail(request, pk):
	post = get_object_or_404(Post, id = pk)
	postid= post.id
	print(postid)
	comments = Comment.objects.filter(post_id = postid).order_by('-id')
	#comments = Comment.objects.all()
	context = {'posts': post, 'comments': comments}
	return render(request, 'accounts/post_detail.html', context)"""

class PostListView(ListView):
	model = Post 
	template_name = 'accounts/index.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

#class PostDetailView(Comment, DetailView):
	#model = Post

def post_detail(request, pk):
	request.session.set_expiry(300)
	post = get_object_or_404(Post, id = pk)
	postid= post.id
	is_liked = False
	if post.likes.filter(id =request.user.id).exists():
		is_liked = True

	
	comments = Comment.objects.filter(post = post).order_by('-id')

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('comment')
			comment = Comment.objects.create(post=post, user=request.user, comment = content)
			comment.save()
			return  HttpResponseRedirect(post.get_absolute_url())
	else:
		comment_form = CommentForm()

	context = {'post': post, 'comments': comments, 'comment_form':comment_form,'is_liked': is_liked, 'total_likes': post.total_likes()}
	return render(request, 'accounts/post_detail.html', context)


def like_post(request):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	if post.likes.filter(id =request.user.id).exists():
		post.likes.remove(request.user)
		is_liked = False
	else:
		post.likes.add(request.user)
		is_liked = True
	return HttpResponseRedirect(post.get_absolute_url())



class PostCreateView(LoginRequiredMixin, CreateView):
	
	model = Post
	fields = ['title','content','image','file']

	def form_valid(self, form):
		form.instance .author  = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content','image']

	def form_valid(self, form):
		form.instance .author  = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post  = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	success_url = '/'

	def test_func(self):
		post  = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'accounts/dashboard.html')