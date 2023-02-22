from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import IndexView, PostDetailView, AuthorDetailView, PostCreateView, ProfileUserView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<post_slug>/', PostDetailView.as_view(), name='detail-post'),
    path('author/<author_id>/', AuthorDetailView.as_view(), name='detail-author'),
    path('test/', PostCreateView.as_view()),
    path('profile/<user_id>/', ProfileUserView.as_view(), name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)