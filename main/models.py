from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post', db_column='user')
    title = models.CharField(max_length=125)
    excerpt = models.CharField(max_length=300)
    img_name = models.ImageField(upload_to='img/', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"
