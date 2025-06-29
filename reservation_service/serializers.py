from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import CustomUser, Hotel, HotelRoom, RoomReservation

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "name", "country", "city", "street", "street_number"]

class HotelRoomSerializer(ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ["id", "hotel", "number_room", "description"]

class RoomResevationSerializer(ModelSerializer):
    hotel_name = SerializerMethodField()
    hotel_address = SerializerMethodField()
    class Meta:
        model = RoomReservation
        fields = ['id', 'hotel_room', 'user', 'date_start', 'date_end', "hotel_name", "hotel_address"]
    def validate(self, attrs):
        date_start = attrs["date_start"]
        date_end = attrs["date_end"]
        room = attrs["hotel_room"]
        validate_data = RoomReservation.objects.filter(
            hotel_room = room,
            date_start__lt = date_end,
            date_end__gt = date_start
        )
        if validate_data.exists():
            raise ValidationError("На эту дату комната уже забронированна!")
        return attrs
    def get_hotel_name(self, obj):
        return obj.hotel_room.hotel.name

    def get_hotel_address(self, obj):
        return f"{obj.hotel_room.hotel.country}, {obj.hotel_room.hotel.city}, {obj.hotel_room.hotel.street}, {obj.hotel_room.hotel.street_number}" 


    

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'