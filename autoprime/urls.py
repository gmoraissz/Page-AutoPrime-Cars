from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "AutoPrime — Administração"
admin.site.site_title = "AutoPrime"
admin.site.index_title = "Painel de controle"

urlpatterns = [
    path("admin/", admin.site.urls),
    # Página inicial: lista de carros, detalhe e contato
    path("", include("carros.urls")),
]

# Serve as fotos enviadas (MEDIA) apenas em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
