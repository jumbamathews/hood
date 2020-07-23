from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/title$', views.add_hood, name='add_hood'),
    url(r'^search/', views.search, name='search_results'),
    url(r'^business/', views.business, name='business'),
    url(r'^accounts/profile/(\d+)', views.profile, name='profile'),
    url(r'^accounts/edit-profile/', views.edit_profile, name='edit-profile'),
    url(r'^post/(\d+)', views.post, name='post'),
    url(r'^new/post/', views.new_post, name='new-post'),
    url(r'^new/business/', views.new_business, name='new-business')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
