# Real-time Chat Application

A real-time chat application built with Django and WebSocket support.

## Features

- User Authentication (Register/Login)
- Real-time messaging using WebSocket
- Responsive design
- User list with online/offline status
- Message history
- Collapsible user menu

## Technology Stack

- Backend: Django, Django Channels
- Frontend: HTML, CSS, JavaScript
- Database: SQLite/MySQL
- Real-time: WebSocket (Daphne server)

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/muzzammilsayyed/chat-app.git
cd chat-application
```


2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

# Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create .env file in the project root with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=3306
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser (admin account):
```bash
python manage.py createsuperuser
```

## Running the Application

The application uses Daphne server for WebSocket support. Run the server using:

```bash
python -m daphne chat_project.asgi:application
```

The application will be available at: http://127.0.0.1:8000/auth/register/


## Usage

1. Access the application through your web browser
2. Register a new account or login
3. View available users in the left sidebar
4. Click on a user to start chatting
5. Use the collapse button to toggle the user list
6. Send messages in real-time

## Project Structure

```
chat_project/
├── chat/                   # Main chat application
├── accounts/              # User authentication
├── static/                # Static files (CSS, JS)
├── templates/             # HTML templates
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Common Issues and Solutions

1. If WebSocket connection fails:
- Make sure you're running the server with Daphne
- Check if your browser supports WebSocket
- Check the browser console for errors

## Live Demo
[URL soon]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

