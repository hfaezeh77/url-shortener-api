from django.contrib import admin
from django.urls import include, path
from shortener import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("shortener.urls")),
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),
]