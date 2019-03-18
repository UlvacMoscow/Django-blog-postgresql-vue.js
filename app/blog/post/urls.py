from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


# router = routers.DefaultRouter()
# router.register(r'post', api.PostViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/api_post/', api.api_post),
    path('api/post_add/', api.add_post),
    path('api/api_post_detail/<int:pk>/', api.api_post_detail),
)

urlpatterns += (
     path('', views.news_list, name="list_news"),
     path('single/<int:pk>', views.new_single, name="single_new"),
     # path('single/all',)
    # urls for Post
    path('app_name/post/', views.PostListView.as_view(), name='app_name_post_list'),
    path('app_name/post/create/', views.PostCreateView.as_view(), name='app_name_post_create'),
    path('app_name/post/detail/<int:pk>/', views.PostDetailView.as_view(), name='app_name_post_detail'),
    path('app_name/post/update/<int:pk>/', views.PostUpdateView.as_view(), name='app_name_post_update'),
)
