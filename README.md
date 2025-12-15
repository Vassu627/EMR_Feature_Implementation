# EMR Appointment Management System

## Overview

This project is a simplified EMR appointment management system that allows users to:

- Create, edit, delete appointments
- Filter appointments by date, status, and doctor
- View real-time statistics
- Manage in-person and video consultations

## Frontend

- Built using React
- Primary logic implemented in EMR_Frontend_Assignment.jsx
- Tailwind CSS for styling

## Backend

- Python-based appointment service
- appointment_service.py contains pure business logic
- Data stored in-memory for simplicity

## GraphQL Query Design (Conceptual)

The frontend conceptually uses a `getAppointments` query structured as:

```graphql
query getAppointments($status: String, $doctor: String) {
  appointments(status: $status, doctor: $doctor) {
    id
    name
    date
    time
    doctor
    status
    mode
  }
}

## Data Consistency on Update

The Python backend functions operate on a single in-memory data source, ensuring
that all create, update, and delete operations modify the same appointment list.
When an appointment status is updated, the change is immediately reflected in
subsequent reads, simulating a transactional write as would occur in an Aurora
database. In a real-world system, this update would also trigger a GraphQL
subscription to notify connected clients in real time.
```
