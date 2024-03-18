from django.urls import path
from . import views
from .admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_synopsis, name='movie_synopsis'),
]