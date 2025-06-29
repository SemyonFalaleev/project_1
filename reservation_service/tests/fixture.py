import pytest
from reservation_service.models import Hotel, HotelRoom, CustomUser
from datetime import date

@pytest.fixture
def user(db):
    return CustomUser.objects.create_user(username="testuser", password="pass")

@pytest.fixture
def hotel(db):
    return Hotel.objects.create(
        name="Test Hotel",
        country="Testland",
        city="Test City",
        street="Test Street",
        street_number="123"
    )

@pytest.fixture
def room(db, hotel):
    return HotelRoom.objects.create(hotel=hotel, description="ТЕСТ", number_room=101)

@pytest.fixture
def reservation_data_obj(user, room):
    return {
        "hotel_room": room,
        "user": user,
        "date_start": date(2025, 7, 1),
        "date_end": date(2025, 7, 5),
    }

@pytest.fixture
def reservation_data_json(user, room):
    return {
        "hotel_room": room.id,
        "user": user.id,
        "date_start": date(2025, 7, 1),
        "date_end": date(2025, 7, 5), 
    }