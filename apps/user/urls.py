from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^edit_user/', views.edit_user),
    url(r'^',views.user_center),
]
