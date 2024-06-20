from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField('Титул', max_length=255)
    content = models.TextField('Содержание')  # Изменили тип на TextField
    is_published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='img/', default='/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='Ссылка', null=True)
    categoria = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title  # Изменили на self.title для отображения заголовка поста

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Categories(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='Ссылка', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
