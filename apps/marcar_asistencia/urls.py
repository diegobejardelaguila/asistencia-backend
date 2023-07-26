from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from .views import *


urlpatterns = [

	re_path("asistencia/((?P<pk>\d+)/)?", csrf_exempt(AsistenciaView.as_view())),
	
]