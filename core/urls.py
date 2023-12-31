from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

third_party_urlpatterns = [
    # path('^markdown/', include('django_markdown.urls')),
    path("select2/", include("django_select2.urls")),
]
swagger_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + third_party_urlpatterns

urlpatterns = [
    path("control-pannel/", admin.site.urls, name='admin'),
    path("", include("blog.urls", namespace="blog")),
    path("", include("security.urls", namespace="security")),
] + swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'security.views.page_not_found_error.not_found_page_view'
handler500 = 'security.views.internal_server_error.internal_server_page_view'
