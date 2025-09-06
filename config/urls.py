from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("trix-editor/", include("trix_editor.urls")),
    path("api/v1/project/", include("apps.projects.urls")),
    path("api/v1/technology/", include("apps.technology.urls")),
    path("api/v1/contact/", include("apps.contact.urls")),
    path("api/v1/statistics/", include("apps.stats.urls")),
    path("api/v1/team/", include("apps.team.urls")),
    path("api/v1/services/", include("apps.services.urls")),
    path("api/v1/blogs/", include("apps.blog.urls"))
]
