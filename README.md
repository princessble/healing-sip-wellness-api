# Healing Sip Wellness Appointment API

## Project Overview

Healing Sip Wellness Appointment API is a backend project built with Python and FastAPI. It manages appointment bookings for a fictional wellness brand called Healing Sip.

The API allows users to view, create, update, and delete wellness appointments.

## Problem Statement

Healing Sip needs a simple digital system to manage wellness appointment bookings. Instead of handling appointments manually, this API provides structured endpoints for creating appointments, viewing client bookings, updating appointment status, and cancelling appointments.

## Features

- View all wellness appointments
- View one appointment by ID
- Create a new appointment
- Update appointment status
- Delete or cancel an appointment
- Validate email format
- Prevent duplicate appointment IDs
- Handle errors for missing appointments

## Tools Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- VS Code
- GitHub

## Project Structure

```text
healing-sip-wellness-api/
│
├── app/
│   └── main.py
│
├── screenshots/
│   ├── api_docs.png
│   └── create_appointment_success.png
│
├── README.md
└── requirements.txt
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/appointments` | Get all appointments |
| GET | `/appointments/{appointment_id}` | Get one appointment |
| POST | `/appointments` | Create a new appointment |
| PUT | `/appointments/{appointment_id}/status` | Update appointment status |
| DELETE | `/appointments/{appointment_id}` | Delete an appointment |

## How to Run This Project

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Start the API server:

```bash
uvicorn app.main:app --reload
```

or:

```bash
python -m uvicorn app.main:app --reload
```

3. Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Sample Appointment Data

```json
{
  "id": 3,
  "client_name": "Blessing Fortune",
  "email": "blessing@example.com",
  "service_type": "Juice Therapy Consultation",
  "appointment_date": "2026-06-10",
  "appointment_time": "11:30",
  "concern": "Needs support with wellness routine and energy balance",
  "status": "Pending"
}
```

## What I Demonstrated

Through this project, I demonstrated my ability to:

- Build a backend API using FastAPI
- Create API endpoints
- Use Pydantic models for data validation
- Handle basic errors with HTTP exceptions
- Work with JSON data
- Structure a backend project professionally
- Document an API project clearly for GitHub

## Future Improvements

In the future, I would like to:

- Connect the API to a database
- Add user authentication
- Add appointment reminders
- Add service categories
- Add admin dashboard functionality
- Deploy the API online
