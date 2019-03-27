from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from core.views import *

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Karen API', renderer_classes=[
                              OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    path('docs', schema_view, name="docs"),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),
    path('update-profile', UpdateProfileView.as_view(), name='update-profile'),
    path('user', UserView.as_view(), name='user'),
    path('calculate-bmi', CalculateBMIView.as_view(), name='calculate-bmi'),
    path('calculate-dci', CalculateDCIView.as_view(), name='calculate-dci'),
    path('suggested-foods', FoodsView.as_view(), name='suggested-foods'),
]
