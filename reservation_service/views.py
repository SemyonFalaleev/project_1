from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Hotel, HotelRoom, RoomReservation
from .serializers import CustomUserSerializer, HotelSerializer, HotelRoomSerializer, RoomResevationSerializer

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelRoomViewSet(ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    def get_queryset(self):
        queryset = HotelRoom.objects.all()
        hotel_id = self.request.query_params.get("hotel_id")
        if hotel_id:
            queryset = queryset.filter(hotel=hotel_id)
        return queryset
    

class RoomResevationViewSet(ModelViewSet):
    queryset = RoomReservation.objects.all()
    serializer_class = RoomResevationSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
