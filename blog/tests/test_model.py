from django.test import TestCase

from blog.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Test Title', content='Test Content')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'Test Title')
        self.assertEqual(expected_content, 'Test Content')

    def test_str_representation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), post.title)
