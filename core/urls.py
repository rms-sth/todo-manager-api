from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register(r"users", viewsets.UserViewSet)
router.register(r"category", viewsets.CategoryViewSet)
router.register(r"todo", viewsets.ToDoViewSet)

urlpatterns = [
    path(
        "todo/multiple-delete/",
        viewsets.MultipleToDoDeleteView.as_view(),
        name="todo_multiple_delete",
    ),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
