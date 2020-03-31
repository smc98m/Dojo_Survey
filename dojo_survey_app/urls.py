from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('process_form', views.process),
    path('results', views.results),
    path('clear_session', views.clear_session),
]