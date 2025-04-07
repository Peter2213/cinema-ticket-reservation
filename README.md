# Cinema Ticket Reservation System

This project is a backend system for a cinema ticket reservation application built using Django and Django Rest Framework (DRF). It provides APIs for managing guests, reservations, and movies.

## Features

### 1. Function-Based Views (FBV)

- **FBV_List**: Handles `GET` and `POST` requests to list all guests or create a new guest.
  - URL: `/rest/fbvlist/`
- **FBV_pk**: Handles `GET`, `PUT`, and `DELETE` requests for a specific guest by primary key.
  - URL: `/rest/fbvpk/<int:pk>/`

### 2. Class-Based Views (CBV)

- **CBV_List**: Handles `GET` and `POST` requests to list all guests or create a new guest.
  - URL: `/rest/cbvlist/`
- **CBV_pk**: Handles `GET`, `PUT`, and `DELETE` requests for a specific guest by primary key.
  - URL: `/rest/cbvpk/<int:pk>/`

### 3. Mixins-Based Views

- **Mixins_List**: Handles `GET` and `POST` requests using DRF mixins.
  - URL: `/rest/mixinslist/`
- **Mixins_pk**: Handles `GET`, `PUT`, and `DELETE` requests for a specific guest using DRF mixins.
  - URL: `/rest/mixinspk/<int:pk>/`

### 4. Generic Views

- **Generic_List**: Handles `GET` and `POST` requests using DRF generic views.
  - URL: `/rest/GenericList/`
- **Generic_pk**: Handles `GET`, `PUT`, and `DELETE` requests for a specific guest using DRF generic views.
  - URL: `/rest/Genericpk/<int:pk>/`

### 5. ViewSets and Routers

- **GuestViewSet**: Provides a complete set of CRUD operations for guests using DRF ViewSets.
  - URL: `/rest/viewset/`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cinema-ticket-reservation
   ```


2-Install dependencies:

```python
pip install -r requirements.txt
```

3-Run migrations:

```python
python manage.py migrate
```


4.Start the development server:

```python
python manage.py runserver
```
