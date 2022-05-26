from django.urls import path
from . import views

# /movies/1
# /old_system/movies/1

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='detail')
]
