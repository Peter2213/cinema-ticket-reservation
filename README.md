# Cinema Ticket Reservation System

This project is a backend system for a cinema ticket reservation application built using Django and Django Rest Framework (DRF). It provides APIs for managing guests, reservations, and movies.

## Features

-**GuestViewSet**: Provides a complete set of CRUD operations for guests using DRF ViewSets.

-**MovieViewSet**: Provides CRUD operations for movies with a **searching feature**.

- You can search for movies by `movie_name` or `category` using query parameters.
- Example: `/rest/viewset/movie/?search=<search_term>`

-**ReservationViewSet**: Provides CRUD operations for reservations.

These ViewSets are registered with a `DefaultRouter`, which automatically generates the necessary routes.


### Additional Endpoints

-**Find Movie**: A custom endpoint to find a movie using Function-Based Views.

- URL: `/findmovie/`

-**New Reservation**: A custom endpoint to create a new reservation using Function-Based Views.

- URL: `/newreservation/`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Peter2213/cinema-ticket-reservation
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
