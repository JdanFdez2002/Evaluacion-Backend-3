from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [
    path("api/mangas/", views.manga_api, name="manga_api"),
    path("", views.feed_premium, name="premium_feed"),
]
