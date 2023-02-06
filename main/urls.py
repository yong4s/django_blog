from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<post_slug>/', views.detail_post, name='detail-post'),
    path('show_form/', views.show_form, name='show_form'),
    path('add_post/', views.add_post, name='add_post'),
    path('author/<author_id>/', views.detail_author, name='detail-author')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)