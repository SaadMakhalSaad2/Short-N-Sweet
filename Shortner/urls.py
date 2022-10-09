
from django.urls import path
from django.views.generic import RedirectView
from Shortner import views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', RedirectView.as_view(url='/shorten/')),
    path('shorten/', views.get_form, name='urlform'),
    path('<short_url>/', views.redirect_short_url, name='redirectpath'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
