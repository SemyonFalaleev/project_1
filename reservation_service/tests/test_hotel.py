import pytest

from reservation_service.serializers import RoomResevationSerializer
from reservation_service.models import RoomReservation
from rest_framework.exceptions import ValidationError
from datetime import date

@pytest.mark.django_db
def test_valid_reservation(reservation_data_json):
    serializer = RoomResevationSerializer(data=reservation_data_json)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.hotel_room.id == reservation_data_json["hotel_room"]
    assert instance.user.id == reservation_data_json["user"]

@pytest.mark.django_db
def test_overlapping_reservation(reservation_data_obj, reservation_data_json):

    RoomReservation.objects.create(**reservation_data_obj)

    overlapping_data = reservation_data_json.copy()
    overlapping_data["date_start"] = date(2025, 7, 4) 
    overlapping_data["date_end"] = date(2025, 7, 8)

    serializer = RoomResevationSerializer(data=overlapping_data)
    with pytest.raises(ValidationError) as exc:
        serializer.is_valid(raise_exception=True)

    assert "уже забронированна" in str(exc.value).lower()

@pytest.mark.django_db
def test_serializer_hotel_fields(reservation_data_obj):
    reservation = RoomReservation.objects.create(**reservation_data_obj)

    serializer = RoomResevationSerializer(instance=reservation)

    data = serializer.data

    assert data["hotel_name"] == "Test Hotel"
    assert data["hotel_address"] == "Testland, Test City, Test Street, 123"