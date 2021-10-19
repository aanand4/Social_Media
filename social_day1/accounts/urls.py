from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView
#from .views import PostDetailView
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='Home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='About'),
    url(r'^like/$', views.like_post, name='like_post')
]

# <app>/<model>_<viewtype>.html