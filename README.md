
# 🏨 Hotel Booking API

REST API для управления пользователями, отелями, комнатами и бронированиями на базе Django REST Framework.

---

## 📦 ViewSet-ы

### 🔹 `HotelViewSet`

Управление сущностями **отелей**.

**Роут:** `/hotels/`

| Метод | URL            | Описание                  |
|-------|----------------|---------------------------|
| GET   | `/hotels/`     | Получить список отелей    |
| GET   | `/hotels/{id}/`| Получить отель по ID      |
| POST  | `/hotels/`     | Создать новый отель       |
| PUT   | `/hotels/{id}/`| Обновить отель            |
| DELETE| `/hotels/{id}/`| Удалить отель             |

---

### 🔹 `HotelRoomViewSet`

Управление **номерами отелей**. Поддерживает фильтрацию по `hotel_id`.

**Роут:** `/hotel-rooms/`

| Метод | URL                            | Описание                        |
|-------|--------------------------------|---------------------------------|
| GET   | `/hotel-rooms/`                | Получить список номеров         |
| GET   | `/hotel-rooms/?hotel_id=1`     | Фильтр по ID отеля              |
| GET   | `/hotel-rooms/{id}/`           | Получить номер по ID            |
| POST  | `/hotel-rooms/`                | Создать номер                   |
| PUT   | `/hotel-rooms/{id}/`           | Обновить номер                  |
| DELETE| `/hotel-rooms/{id}/`           | Удалить номер                   |

---

### 🔹 `RoomResevationViewSet`

Управление **бронированиями номеров**. Использует `RoomResevationSerializer`, который проверяет пересечение дат.

**Роут:** `/reservations/`

| Метод | URL                   | Описание                          |
|-------|-----------------------|-----------------------------------|
| GET   | `/reservations/`      | Список бронирований               |
| GET   | `/reservations/{id}/` | Получить бронь по ID              |
| POST  | `/reservations/`      | Создать новую бронь (с валидацией)|
| PUT   | `/reservations/{id}/` | Обновить бронь                    |
| DELETE| `/reservations/{id}/` | Удалить бронь                     |

**Пример ошибки при пересечении дат:**
```json
{
  "non_field_errors": [
    "На эту дату комната уже забронированна!"
  ]
}
```

---

### 🔹 `CustomUserViewSet`

Управление пользователями (кастомная модель `CustomUser`).

**Роут:** `/users/`

| Метод | URL              | Описание               |
|-------|------------------|------------------------|
| GET   | `/users/`        | Список пользователей   |
| GET   | `/users/{id}/`   | Информация по ID       |
| POST  | `/users/`        | Создание пользователя  |
| PUT   | `/users/{id}/`   | Обновление             |
| DELETE| `/users/{id}/`   | Удаление               |

---

## 🔧 Примеры curl-запросов

**Создание отеля:**
```bash
curl -X POST http://localhost:8000/hotels/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Hilton", "country": "Россия", "city": "Москва", "street": "Тверская", "street_number": "12"}'
```

**Фильтрация комнат по отелю:**
```bash
curl http://localhost:8000/hotel-rooms/?hotel_id=1
```

**Создание брони:**
```bash
curl -X POST http://localhost:8000/reservations/ \
     -H "Content-Type: application/json" \
     -d '{"hotel_room": 3, "user": 2, "date_start": "2025-07-10", "date_end": "2025-07-12"}'
```

---

## ⚙️ Настройка роутов (пример)

```python
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, HotelRoomViewSet, RoomResevationViewSet, CustomUserViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('hotel-rooms', HotelRoomViewSet)
router.register('reservations', RoomResevationViewSet)
router.register('users', CustomUserViewSet)
```

---

