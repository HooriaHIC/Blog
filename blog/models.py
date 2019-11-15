from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

TITLE_CHOICES = [
    ('PSYCHOLOGICAL HORROR', 'Psychological horror'),
    ('ALIEN', 'Alien'),
    ('INESCAPABLE', 'Inescapable'),
    ('PERSONAL HORROR', 'Personal Horror'),
    ('HORROR MYTH', 'Horror Myth'),
    ('GHOST HORROR', 'Ghost Horror'),
    ('ZOMBIE', 'Zombies'),
    ('HAUNTED HOUSE', 'Haunted House')
]


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    horror_type = models.CharField(
        default='Horror', max_length=300, choices=TITLE_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class List(models.Model):
    title = models.CharField(max_length=300, default="Top Ten")
    content = models.TextField(default='')

    item1 = models.CharField(default="item 1", max_length=600)
    item1_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item2 = models.CharField(default="item 2", max_length=600)
    item2_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item3 = models.CharField(default="item 3", max_length=600)
    item3_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item4 = models.CharField(default="item 4", max_length=600)
    item4_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item5 = models.CharField(default="item 5", max_length=600)
    item5_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item6 = models.CharField(default="item 6", max_length=600)
    item6_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item7 = models.CharField(default="item 7", max_length=600)
    item7_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item8 = models.CharField(default="item 8", max_length=600)
    item8_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item9 = models.CharField(default="item 9", max_length=600)
    item9_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    item10 = models.CharField(default="item 10", max_length=600)
    item10_image = models.ImageField(
        default='default.jpg', upload_to='post_pics')

    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
