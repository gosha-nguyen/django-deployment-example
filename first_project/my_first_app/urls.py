from django.conf.urls import url
from my_first_app import views as first_views

urlpatterns = [
    url(r'^$',first_views.index,name="index")
]
