from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='patient')  # Roles: patient, doctor, admin
    patient = db.relationship('Patient', backref='user', uselist=False)
    doctor = db.relationship('Doctor', backref='user', uselist=False)
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200))
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    medical_records = db.relationship('MedicalRecord', backref='patient', lazy=True)
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(15))
    fees = db.Column(db.Float, default=500.0)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    doctors = db.relationship('Doctor', backref='department', lazy=True)
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)  # Format: "HH:MM"
    period = db.Column(db.String(20), nullable=False)  # Morning, Afternoon, Evening
    status = db.Column(db.String(20), default='Scheduled')  # Status: Scheduled, Completed, Cancelled
    medical_record = db.relationship('MedicalRecord', backref='appointment', uselist=False)
class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    diagnosis = db.Column(db.Text, nullable=False)
    prescription = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text)