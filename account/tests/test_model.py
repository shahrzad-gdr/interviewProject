from django.test import TestCase
from django.contrib.auth.models import User

from account.models import Rate
from blog.models import Post
from django.contrib.auth.models import User


class RateModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create(username='user1')
        cls.post = Post.objects.create(title='Test Post', content='Test Content')
        Rate.objects.create(user=cls.user, post=cls.post, rank=4)
        Rate.objects.create(user=cls.user, post=cls.post, rank=2)

    def test_average_rank(self):
        post_id = self.post.id
        average = Rate.average(post_id)
        self.assertEqual(average, 3)  # The average of 4 and 2 is 3

    def test_count_rank(self):
        post_id = self.post.id
        count = Rate.count(post_id)
        self.assertEqual(count, 2)  # Two ratings for the test post
