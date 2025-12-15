# appointment_service.py

from datetime import date

appointments = [
    {
        "id": 1,
        "name": "Emily Rodriguez",
        "date": "2025-11-05",
        "time": "11:30",
        "duration": "30 min",
        "doctor": "Dr. Rajesh Kumar",
        "mode": "Video Call",
        "status": "Confirmed",
        "type": "Telemedicine",
        "reason": "Cold",
        "symptoms": "Fever",
        "note": "",
        "phone": "9999999999",
        "email": "emily@test.com"
    },
    
]

def get_appointments(filters=None):
    results = appointments.copy()
    filters = filters or {}

    if filters.get("date"):
        results = [a for a in results if a["date"] == filters["date"]]

    if filters.get("status") and filters["status"] != "All":
        results = [a for a in results if a["status"] == filters["status"]]

    if filters.get("doctor") and filters["doctor"] != "All":
        results = [a for a in results if a["doctor"] == filters["doctor"]]

    return results


def create_appointment(appt):
    appointments.append(appt)
    return appt


def update_appointment_status(appt_id, new_status):
    for a in appointments:
        if a["id"] == appt_id:
            a["status"] = new_status
            return a
    return None


def delete_appointment(appt_id):
    global appointments
    appointments = [a for a in appointments if a["id"] != appt_id]
