from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.starting_page, name='index'),
    path('post/<post_slug>/', views.detail_post, name='detail-post'),
    path('author/<author_id>/', views.detail_author, name='detail-author'),
    path('show_authors/', views.show_all_authors, name="show-authors")
]
