from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('credits/<int:movie_pk>/', views.movie_credits),
    # review
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>', views.review_detail),
    # comment
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
    # like
    path('<int:movie_pk>/likes/', views.likes),
    path('<int:review_pk>/review_likes/', views.review_likes),
]