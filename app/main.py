from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr



app = FastAPI(
    title="Healing Sip Wellness Appointment API",
    description="A backend API for managing wellness appointment bookings for Healing Sip.",
    version="1.0.0"
)


class Appointment(BaseModel):
    id: int
    client_name: str
    email: EmailStr
    service_type: str
    appointment_date: str
    appointment_time: str
    concern: str
    status: str = "Pending"


class StatusUpdate(BaseModel):
    status: str


appointments = [
    {
        "id": 1,
        "client_name": "Amara Johnson",
        "email": "amara@example.com",
        "service_type": "Nutrition Consultation",
        "appointment_date": "2026-06-01",
        "appointment_time": "10:00",
        "concern": "Needs support with healthy eating and energy levels",
        "status": "Confirmed"
    },
    {
        "id": 2,
        "client_name": "David Smith",
        "email": "david@example.com",
        "service_type": "Mindfulness Session",
        "appointment_date": "2026-06-03",
        "appointment_time": "14:00",
        "concern": "Stress management and emotional balance",
        "status": "Pending"
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to the Healing Sip Wellness Appointment API",
        "project": "Healing Sip Wellness Appointment API",
        "status": "Running successfully"
    }


@app.get("/appointments")
def get_all_appointments():
    return {
        "total_appointments": len(appointments),
        "appointments": appointments
    }


@app.get("/appointments/{appointment_id}")
def get_appointment_by_id(appointment_id: int):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    raise HTTPException(status_code=404, detail="Appointment not found")


@app.post("/appointments")
def create_appointment(appointment: Appointment):
    for existing_appointment in appointments:
        if existing_appointment["id"] == appointment.id:
            raise HTTPException(
                status_code=400,
                detail="Appointment ID already exists"
            )

    new_appointment = appointment.model_dump()
    appointments.append(new_appointment)

    return {
        "message": "Appointment created successfully",
        "appointment": new_appointment
    }


@app.put("/appointments/{appointment_id}/status")
def update_appointment_status(appointment_id: int, status_update: StatusUpdate):
    allowed_statuses = ["Pending", "Confirmed", "Completed", "Cancelled"]

    if status_update.status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid status. Use Pending, Confirmed, Completed, or Cancelled."
        )

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointment["status"] = status_update.status
            return {
                "message": "Appointment status updated successfully",
                "appointment": appointment
            }

    raise HTTPException(status_code=404, detail="Appointment not found")


@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointments.remove(appointment)
            return {
                "message": "Appointment deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Appointment not found")
