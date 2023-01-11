from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse('detail-author', kwargs={'author_id': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=125)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name='posts', null=True)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"