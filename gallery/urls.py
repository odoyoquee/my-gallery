from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.image_today,name = 'imageToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^images/(\d+)',views.Image,name ='image'),
    url(r'^category/(\w+)',views.category_image,name='category_list'),
    url(r'^location/(\w+)',views.location_image,name='location_list'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)