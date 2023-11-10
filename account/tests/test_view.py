from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from account.models import Rate
from blog.models import Post


class RateCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user2', password='222')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(id=10, title='Test Post', content='Test Content')

    def test_create_new_rating(self):
        url = reverse('add_rank')
        data = {'user': self.user.id, 'post': self.post.id, 'rank': 5}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rate.objects.count(), 1)
        new_rating = Rate.objects.get()
        self.assertEqual(new_rating.rank, 5)

    def test_update_existing_rating(self):
        # Create an initial rating
        initial_rating = Rate.objects.create(user=self.user, post_id=self.post.id, rank=3)

        url = reverse('add_rank')
        data = {'user': self.user.id, 'post': self.post.id, 'rank': 4}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rate.objects.count(), 1)
        updated_rating = Rate.objects.get()
        self.assertEqual(updated_rating.rank, 4)
        self.assertEqual(updated_rating.id, initial_rating.id)  # Ensuring it's the same rating object
