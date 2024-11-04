from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)


urlpatterns = [
    # path('', views.getData),
    # path('', include(router.urls)),
]
