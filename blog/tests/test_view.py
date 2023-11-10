from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from account.models import Rate
from account.serializers import PostSerializer
from blog.models import Post
from blog.views import PostListAPIView


class PostListAPIViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user2', password='222')
        self.factory = APIRequestFactory()
        self.view = PostListAPIView.as_view()
        self.posts = [
            Post.objects.create(title='Post 1', content='Content 1'),
            Post.objects.create(title='Post 2', content='Content 2')
        ]
        Rate.objects.create(user=self.user, post=self.posts[0], rank=4)


    def test_post_list_unauthenticated(self):
        request = self.factory.get('/post-list/')
        response = self.view(request)
        self.assertEqual(response.status_code, 403)  # Ensure unauthorized access is forbidden
