from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, ReviewViewSet


urlpatterns = router.urls

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'reviews', ReviewViewSet, basename='review')

