from django.urls import path

from blog.views import PostListAPIView

urlpatterns = [
    path('post-list/', PostListAPIView.as_view(), name='post_list'),

]
