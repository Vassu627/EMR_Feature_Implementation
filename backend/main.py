from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Appointment(BaseModel):
    id: int
    name: str
    date: str
    time: str
    duration: str
    doctor: str
    mode: str
    status: str
    type: str
    reason: str
    symptoms: str
    note: str
    phone: str
    email: str


appointments = [
    {
        "id": 1,
        "name": "Emily Rodriguez",
        "date": "2024-11-05",
        "time": "11:30 AM",
        "duration": "30 min",
        "doctor": "Dr. Rajesh Kumar",
        "mode": "Video Call",
        "status": "Confirmed",
        "type": "Telemedicine",
        "reason": "Cold and Flu",
        "symptoms": "Fever, cough",
        "note": "Video consultation requested",
        "phone": "+91 98765 43212",
        "email": "emilyr@email.com"
    },
    {
        "id": 2,
        "name": "Michael Chen",
        "date": "2024-11-05",
        "time": "10:00 AM",
        "duration": "45 min",
        "doctor": "Dr. Priya Sharma",
        "mode": "In-Person",
        "status": "Scheduled",
        "type": "Consultation",
        "reason": "Annual Physical",
        "symptoms": "",
        "note": "",
        "phone": "+91 98765 43210",
        "email": "michael@email.com"
    }
]

@app.get("/appointments", response_model=List[Appointment])
def get_appointments(status: str = "All", doctor: str = "All"):
    result = appointments
    if status != "All":
        result = [a for a in result if a["status"] == status]
    if doctor != "All":
        result = [a for a in result if a["doctor"] == doctor]
    return result


@app.post("/appointments", response_model=Appointment)
def create_appointment(appt: Appointment):
    appointments.append(appt.dict())
    return appt


@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    global appointments
    appointments = [
        a for a in appointments
        if (a.id if isinstance(a, Appointment) else a["id"]) != appointment_id
    ]
    return {"message": "Appointment deleted"}


@app.put("/appointments/{appointment_id}")
def update_status(appointment_id: int, status: str):
    for a in appointments:
        if (a.id if isinstance(a, Appointment) else a["id"]) == appointment_id:
            if isinstance(a, Appointment):
                a.status = status
            else:
                a["status"] = status
            return a
    return {"error": "Appointment not found"}

