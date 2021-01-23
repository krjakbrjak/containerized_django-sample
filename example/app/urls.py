from rest_framework import routers
from .views import BookViewSet

app_name = "app"

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
