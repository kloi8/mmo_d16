from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    TYPE = (
        ('tanks', 'Танки'),
        ('heals', 'Хилы'),
        ('damage dealers', 'ДД'),
        ('merchants', 'Торговцы'),
        ('gild masters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('potions makers', 'Зельевары'),
        ('spell masters', 'Мастера заклинаний')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    title = models.CharField(max_length=128)
    text = RichTextUploadingField('Text', blank=True, null=True)
    category = models.CharField(max_length=20, choices=TYPE, default='heal')
    upload = models.FileField(upload_to='uploads/')
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}  |  {self.author}  |  {self.dateCreation}  |  {self.category}  |  {self.text[:64]}'

    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)))

    def get_categories(self):
        cat_menu = [
            'tanks',
            'heals',
            'damage dealers',
            'merchants',
            'gild masters',
            'questgivers',
            'blacksmiths',
            'leatherworkers',
            'potions makers',
            'spell masters',
        ]
        return cat_menu


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BinaryField(default=False)
    resp_date = models.DateTimeField(auto_now_add=True)

