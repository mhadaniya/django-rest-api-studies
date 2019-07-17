from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create a user
        user1 = User.objects.create_user(username='user1', password='q1w2e3')
        user1.save()

        #Create a post
        post = Post.objects.create(
            author = user1,
            title = 'Teste blog 1',
            body = 'Lorem ipsum...',
        )
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_autor = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'

        self.assertEqual(expected_autor, 'user1')
        self.assertEqual(expected_title, 'Test blog 1')
        self.assertEqual(expected_body, 'Lorem ipsum...')
