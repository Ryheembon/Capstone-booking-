# Saffron & Sage Restaurant Booking System

A Django-based restaurant booking system that allows customers to make table reservations and manage their bookings online.

## Features

- Table reservation system
- Real-time booking availability check
- Interactive booking calendar
- Time slot management (1:00 PM - 9:00 PM)
- Current bookings display
- Automatic time slot disabling for booked slots

## Technical Stack

- **Backend:** Django
- **Database:** MySQL
- **Frontend:** HTML, JavaScript
- **Styling:** CSS, Bootstrap

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ryheembon/Capstone-booking-.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MySQL database in settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. Navigate to the booking page
2. Select your preferred date
3. Choose an available time slot
4. Enter your details
5. Submit your booking

## Project Structure

- `restaurant/` - Main application directory
  - `templates/` - HTML templates
  - `static/` - CSS, JavaScript, and media files
  - `models.py` - Database models
  - `views.py` - View logic
  - `urls.py` - URL configurations

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
