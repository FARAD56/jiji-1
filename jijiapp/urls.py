from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api_schema',get_schema_view(title= 'API schema',description='Guide for the REST API'), name='api_schema'),
    path('admin/', admin.site.urls),
    path('jiji/', include('jiji.urls')),
    path('', include('base.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
