
# MediFlow 🏥
### Hospital Appointment Management System

MediFlow is a beginner-friendly, open-source project designed to simplify hospital appointment booking through a web interface and Python backend.

## Features
- Book hospital appointments
- Select a medical department
- Enter appointment date and reason for visit
- Store appointment details using SQLite
- View saved appointments through the backend API

## Technology Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Database: SQLite

## Project Structure
```text
MediFlow/
├── README.md
├── LICENSE
├── requirements.txt
├── backend/
│   └── app.py
└── frontend/
    ├── index.html
    ├── style.css
    └── booking.html
```

## Setup Instructions

### 1. Install Python
Install Python 3.10 or later.

### 2. Install dependencies
Open a terminal in the project root and run:

```bash
pip install -r requirements.txt
```

### 3. Start the backend
Run:

```bash
python backend/app.py
```

The Flask server runs at `http://127.0.0.1:5000`.

### 4. Open the frontend
Open `frontend/index.html` in a browser.

The booking form sends requests to the local backend. Keep the backend running while using the form.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check backend status |
| POST | `/appointments` | Book an appointment |
| GET | `/appointments` | View saved appointments |

## Database
SQLite stores appointment details in a local database file created by the backend.

## Testing
Test the backend status endpoint, submit an appointment with all required fields, check that missing fields are rejected, and verify saved appointments using the GET endpoint.

These tests must be run locally before the project can be considered verified.

## Limitations
- This is an educational prototype, not a production hospital system.
- Patient authentication and access control are not implemented.
- Patient information is not suitable for real clinical use.
- The frontend and backend integration requires local testing.

## Future Improvements
- Patient registration and login
- Appointment management
- Patient history management
- Secure authentication and data protection

## License
Distributed under the MIT License. See [LICENSE](LICENSE).

## Status
Under development.
