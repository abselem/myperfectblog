from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path('', views.showblog, name='showblog' ),
    path('<int:post_id>/', views.specific_post, name='specific_post'),
]