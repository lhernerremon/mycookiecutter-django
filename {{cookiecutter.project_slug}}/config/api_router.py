# Django
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# ViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", ViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += []
