from django.urls import path, re_path
from basicapp import views

urlpatterns = [
    re_path('^$', views.form_name_view, name='form_names'),
]