from rest_framework.routers import DefaultRouter
from reservation_service.views import CustomUserViewSet, HotelViewSet, HotelRoomViewSet, RoomResevationViewSet

router = DefaultRouter()
router.register("hotels", HotelViewSet)
router.register("rooms", HotelRoomViewSet)
router.register("reservations", RoomResevationViewSet)
router.register("user", CustomUserViewSet)

urlpatterns = router.urls