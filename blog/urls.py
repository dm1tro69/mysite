from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    #post_view
    path('', views.post_list, name='post_list'),
    path('feed/', LatestPostsFeed(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_feed'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

]