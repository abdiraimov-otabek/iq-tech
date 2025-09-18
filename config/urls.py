from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("trix-editor/", include("trix_editor.urls")),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/project/", include("apps.projects.urls")),
    path("api/v1/technology/", include("apps.technology.urls")),
    path("api/v1/contact/", include("apps.contact.urls")),
    path("api/v1/statistics/", include("apps.stats.urls")),
    path("api/v1/team/", include("apps.team.urls")),
    path("api/v1/services/", include("apps.services.urls")),
    path("api/v1/blogs/", include("apps.blog.urls")),
    path("api/v1/partners/", include("apps.partners.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
