# Hospital Management System

A comprehensive web-based Hospital Management System built with Flask, enabling efficient management of patients, doctors, appointments, and medical records through role-based access control.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Routes](#api-routes)
- [User Roles](#user-roles)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🏥 Overview

The Hospital Management System is a full-stack web application designed to streamline hospital operations by providing dedicated interfaces for patients, doctors, and administrators. The system automates appointment scheduling, manages medical records, and facilitates communication between healthcare providers and patients.

### Key Highlights
- **Role-Based Access Control**: Three distinct user roles (Patient, Doctor, Admin) with specific permissions
- **Appointment Management**: Smart scheduling with time slot availability checking
- **Medical Records**: Secure storage and retrieval of patient diagnoses and prescriptions
- **Real-time Availability**: Dynamic time slot management preventing double-booking
- **Session-Based Authentication**: Secure login system with password hashing

---

## ✨ Features

### 👤 Patient Features
- **User Registration & Login**: Secure account creation with email validation
- **Profile Management**: Update personal information including gender, phone, and address
- **Appointment Booking**: 
  - Browse available doctors by specialization and department
  - View real-time available time slots (morning, afternoon, evening)
  - Book appointments up to 7 days in advance
  - Automatic conflict prevention
- **Dashboard**: 
  - View upcoming scheduled appointments
  - Track completed appointments history
  - Access medical records count
- **Medical Records Access**: View diagnosis, prescriptions, and doctor notes from past appointments

### 👨‍⚕️ Doctor Features
- **Doctor Dashboard**: 
  - Today's appointments overview
  - Upcoming appointments list
  - Quick access to patient information
- **Appointment Management**: 
  - View all scheduled appointments
  - Mark appointments as completed
  - Filter by date and status
- **Medical Records Creation**: 
  - Add diagnosis and prescriptions post-consultation
  - Include clinical notes
  - Linked to specific appointments
- **Patient Management**: View list of all patients under care
- **Profile Management**: Update gender and phone number
- **Password Management**: Change password with current password verification

### 🔧 Admin Features
- **Comprehensive Dashboard**: Overview of all system entities
- **Department Management**: 
  - Create, update, and delete departments
  - View doctors assigned to each department
- **Doctor Management**: 
  - Add new doctors with department assignment
  - Edit doctor information (name, specialization, fees)
  - Set consultation fees
  - Delete doctors (with dependency checks)
  - Auto-generate doctor accounts with default credentials
- **Patient Management**: 
  - View all registered patients
  - Delete patient records with cascade delete of appointments and records
- **Appointment Oversight**: 
  - View all appointments across the system
  - Delete appointments if needed
  - Monitor appointment status

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.0.1**: Lightweight WSGI web framework
- **Flask-SQLAlchemy 2.5.1**: SQL toolkit and ORM
- **Flask-WTF 0.15.1**: Form handling and validation
- **WTForms 2.3.3**: Form validation library
- **Werkzeug**: Password hashing and security utilities
- **SQLite**: Embedded relational database

### Frontend
- **Jinja2**: Server-side templating engine (bundled with Flask)
- **HTML5 & CSS3**: Markup and styling
- **JavaScript (Vanilla)**: Client-side interactivity
- **Bootstrap** (optional): Responsive design framework

### Development Tools
- **pip**: Package management
- **venv**: Virtual environment management
- **PowerShell/Bash**: Command-line interface

---

## 🏗️ System Architecture

### MVC Pattern
The application follows the Model-View-Controller architectural pattern:

```
hospital_management_system/
│
├── app.py                 # Controller: Routes and business logic
├── models.py              # Model: Database schema and ORM models
├── forms.py               # Form definitions and validators
│
├── templates/             # View: HTML templates
│   ├── base.html          # Base template with common layout
│   ├── index.html         # Landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── patient_dashboard.html
│   ├── doctor_dashboard.html
│   ├── admin_dashboard.html
│   ├── book_appointment.html
│   ├── view_appointments.html
│   ├── doctor_appointments.html
│   ├── add_medical_record.html
│   ├── view_medical_records.html
│   ├── view_medical_record_doctor.html
│   ├── doctor_medical_records.html
│   ├── doctor_patients.html
│   ├── manage_doctors.html
│   ├── manage_patients.html
│   ├── manage_departments.html
│   ├── manage_appointments.html
│   ├── update_patient_profile.html
│   ├── update_doctor_profile.html
│   └── change_password.html
│
├── static/                # Static assets
│   ├── css/
│   │   └── styles.css     # Custom styles
│   ├── js/
│   │   └── scripts.js     # Client-side JavaScript
│   └── images/            # Image assets
│
├── requirements.txt       # Python dependencies
└── hospital_management.db # SQLite database (auto-generated)
```

### Request Flow
1. User sends HTTP request to Flask route
2. Flask route validates session and permissions
3. Form data validated using WTForms
4. Database operations performed via SQLAlchemy ORM
5. Template rendered with Jinja2 and returned to user

---

## 🗄️ Database Schema

### Tables Overview

#### 1. **User Table**
Stores authentication credentials and role information.

```python
User:
  - id (Primary Key)
  - username (Unique, Not Null)
  - email (Unique, Not Null)
  - password (Hashed, Not Null)
  - role (patient/doctor/admin, Default: patient)
  
Relationships:
  - One-to-One with Patient
  - One-to-One with Doctor
```

#### 2. **Patient Table**
Stores patient-specific information.

```python
Patient:
  - id (Primary Key)
  - user_id (Foreign Key → User.id)
  - name (Not Null)
  - dob (Date of Birth)
  - gender (Male/Female/Other)
  - phone (Contact number)
  - address (Residential address)
  
Relationships:
  - One-to-Many with Appointment
  - One-to-Many with MedicalRecord
```

#### 3. **Doctor Table**
Stores doctor-specific information.

```python
Doctor:
  - id (Primary Key)
  - user_id (Foreign Key → User.id)
  - name (Not Null)
  - specialization (Medical specialty)
  - department_id (Foreign Key → Department.id)
  - gender (Optional)
  - phone (Optional)
  - fees (Consultation fee, Default: 500.0)
  
Relationships:
  - One-to-Many with Appointment
```

#### 4. **Department Table**
Stores hospital departments.

```python
Department:
  - id (Primary Key)
  - name (Department name, Not Null)
  
Relationships:
  - One-to-Many with Doctor
```

#### 5. **Appointment Table**
Stores appointment scheduling information.

```python
Appointment:
  - id (Primary Key)
  - patient_id (Foreign Key → Patient.id)
  - doctor_id (Foreign Key → Doctor.id)
  - appointment_date (Date, Not Null)
  - time_slot (Format: "HH:MM", Not Null)
  - period (Morning/Afternoon/Evening)
  - status (Scheduled/Completed/Cancelled, Default: Scheduled)
  
Relationships:
  - One-to-One with MedicalRecord
```

#### 6. **MedicalRecord Table**
Stores medical consultation records.

```python
MedicalRecord:
  - id (Primary Key)
  - patient_id (Foreign Key → Patient.id)
  - appointment_id (Foreign Key → Appointment.id)
  - diagnosis (Text, Not Null)
  - prescription (Text, Not Null)
  - notes (Optional clinical notes)
```

### Entity Relationship Diagram

```
┌─────────┐         ┌─────────┐         ┌────────────┐
│  User   │◄───────►│ Patient │◄───────►│Appointment │
└─────────┘   1:1   └─────────┘   1:N   └────────────┘
     │                    │                     │
     │ 1:1                │ 1:N                 │ 1:1
     ▼                    ▼                     ▼
┌─────────┐         ┌──────────────┐    ┌──────────────┐
│ Doctor  │◄───────►│MedicalRecord │    │MedicalRecord │
└─────────┘   1:N   └──────────────┘    └──────────────┘
     │
     │ N:1
     ▼
┌────────────┐
│ Department │
└────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Download the Project
```powershell
# Navigate to project directory
cd "c:\Users\krrsa\OneDrive - nitnagaland.ac.in\Desktop\24f2000927\hospital_management_system"
```

### Step 2: Create Virtual Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (PowerShell)
.venv\Scripts\Activate.ps1

# For Command Prompt
.venv\Scripts\activate.bat

# For Git Bash
source .venv/Scripts/activate
```

### Step 3: Install Dependencies
```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 4: Initialize Database
The database will be automatically created on first run. To manually initialize:

```powershell
# Run the application once to create database
python app.py
```

This will:
- Create `hospital_management.db` in the project root
- Set up all required tables
- Create a default admin account:
  - **Email**: `admin@hospital.com`
  - **Password**: `admin123`

---

## ⚙️ Configuration

### Environment Variables (Optional)
For production deployment, set these environment variables:

```powershell
# Secret key for session management
$env:SECRET_KEY = "your-secret-key-here"

# Database URI (optional, defaults to SQLite)
$env:DATABASE_URI = "sqlite:///hospital_management.db"

# Flask environment
$env:FLASK_ENV = "production"
```

### Application Settings
Edit `app.py` to customize:

```python
# Line 9-11: Basic configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Change in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### Time Slot Configuration
Edit time slots in `app.py` (around line 345):

```python
time_slots = {
    'morning': ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30'],
    'afternoon': ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'],
    'evening': ['17:00', '17:30', '18:00', '18:30', '19:00', '19:30']
}
```

---

## 🚀 Usage

### Starting the Application

#### Development Mode
```powershell
# Method 1: Direct execution
python app.py

# Method 2: Flask CLI
$env:FLASK_APP = "app.py"
flask run

# Method 3: With debug mode
flask run --debug
```

The application will start on `http://127.0.0.1:5000/`

### Default Admin Credentials
- **Email**: `admin@hospital.com`
- **Password**: `admin123`

⚠️ **Important**: Change the admin password immediately after first login in production!

### User Workflows

#### For New Patients
1. Navigate to `http://127.0.0.1:5000/`
2. Click "Register" and fill in the form
3. Login with registered email and password
4. Complete profile with personal details
5. Book appointments with available doctors
6. View medical records after consultations

#### For Doctors
1. Admin creates doctor account
2. Login with email and default password `doctor123`
3. Change password from doctor dashboard
4. Complete profile information
5. View and manage appointments
6. Add medical records post-consultation

#### For Administrators
1. Login with admin credentials
2. Create departments first
3. Add doctors to departments
4. Monitor system-wide operations
5. Manage all entities as needed

---

## 🛣️ API Routes

### Public Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Landing page |
| `/register` | GET, POST | User registration |
| `/login` | GET, POST | User authentication |
| `/logout` | GET | Session termination |

### Patient Routes (Authentication Required)
| Route | Method | Description |
|-------|--------|-------------|
| `/patient_dashboard` | GET | Patient dashboard |
| `/book_appointment` | GET, POST | Book new appointment |
| `/get_available_slots/<doctor_id>/<date>` | GET | Get available time slots (AJAX) |
| `/view_appointments` | GET | View all appointments |
| `/view_medical_records` | GET | View all medical records |
| `/update_patient_profile` | GET, POST | Update patient profile |

### Doctor Routes (Authentication Required)
| Route | Method | Description |
|-------|--------|-------------|
| `/doctor_dashboard` | GET | Doctor dashboard |
| `/doctor_appointments` | GET | View all appointments |
| `/complete_appointment/<id>` | POST | Mark appointment as completed |
| `/add_medical_record/<appointment_id>` | GET, POST | Create medical record |
| `/view_medical_record/<appointment_id>` | GET | View specific medical record |
| `/doctor_medical_records` | GET | View all medical records |
| `/doctor_patients` | GET | View all patients |
| `/update_doctor_profile` | GET, POST | Update doctor profile |
| `/change_password` | GET, POST | Change password |

### Admin Routes (Authentication Required)
| Route | Method | Description |
|-------|--------|-------------|
| `/admin_dashboard` | GET | Admin dashboard |
| `/manage_doctors` | GET, POST | Manage doctors (add/view) |
| `/edit_doctor/<id>` | POST | Edit doctor information |
| `/delete_doctor/<id>` | POST | Delete doctor |
| `/manage_patients` | GET | View all patients |
| `/delete_patient/<id>` | POST | Delete patient |
| `/manage_departments` | GET, POST | Manage departments |
| `/edit_department/<id>` | POST | Edit department |
| `/delete_department/<id>` | POST | Delete department |
| `/manage_appointments` | GET | View all appointments |
| `/delete_appointment/<id>` | POST | Delete appointment |

---

## 👥 User Roles

### Patient Role
**Permissions**:
- ✅ Create and manage own account
- ✅ Book appointments
- ✅ View own appointments and medical records
- ✅ Update own profile
- ❌ Cannot access doctor/admin features

**Use Case**: Regular hospital visitors seeking medical consultation

### Doctor Role
**Permissions**:
- ✅ View assigned appointments
- ✅ Add medical records for consultations
- ✅ View list of patients
- ✅ Update own profile and password
- ❌ Cannot manage other doctors or system settings

**Use Case**: Medical professionals providing consultations

### Admin Role
**Permissions**:
- ✅ Full system access
- ✅ Manage doctors, patients, departments
- ✅ View all appointments and records
- ✅ System configuration
- ⚠️ Cannot view/edit medical record details (privacy)

**Use Case**: Hospital administrators managing operations

---

## 📸 Screenshots

### Landing Page
- Clean interface with login/register options
- Overview of hospital management features

### Patient Dashboard
- Upcoming appointments with doctor details
- Completed appointments history
- Quick access to book new appointments
- Medical records summary

### Doctor Dashboard
- Today's appointments with time slots
- Upcoming appointments calendar view
- Patient list and medical records access

### Admin Dashboard
- Statistics overview (departments, doctors, patients, appointments)
- Quick navigation to management sections
- Recent appointments list

### Appointment Booking
- Doctor selection dropdown (filtered by department)
- Date picker (7-day advance booking)
- Dynamic time slot loading based on availability
- Real-time conflict checking

---

## 🌐 Deployment

### Production Considerations

#### 1. Use Production WSGI Server
Install Waitress (Windows) or Gunicorn (Linux):

```powershell
# For Windows
pip install waitress

# Create serve.py
from waitress import serve
from app import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
```

Run with:
```powershell
python serve.py
```

#### 2. Disable Debug Mode
In `app.py`, change:
```python
if __name__ == '__main__':
    app.run(debug=False)  # Set to False
```

#### 3. Use Environment Variables
Store sensitive data in environment variables:
```powershell
$env:SECRET_KEY = "production-secret-key-here"
```

Update `app.py`:
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-key')
```

#### 4. Database Migration (PostgreSQL for Production)
For production, consider PostgreSQL:

```powershell
# Install PostgreSQL adapter
pip install psycopg2-binary

# Update DATABASE_URI
$env:DATABASE_URI = "postgresql://user:password@localhost/hospital_db"
```

#### 5. Deploy to Cloud Platforms

**Heroku Deployment**:
```powershell
# Create Procfile
web: python serve.py

# Create runtime.txt
python-3.11.0

# Deploy
heroku create hospital-mgmt-system
git push heroku main
```

**PythonAnywhere Deployment**:
1. Upload files via Files tab
2. Create virtual environment
3. Install requirements
4. Configure WSGI file
5. Reload web app

#### 6. Security Best Practices
- Change default admin password
- Use strong `SECRET_KEY`
- Enable HTTPS in production
- Implement rate limiting
- Add CSRF protection (already included via Flask-WTF)
- Regular security audits

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. **ModuleNotFoundError: No module named 'flask'**
**Solution**: Virtual environment not activated or dependencies not installed
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 2. **Database is locked**
**Solution**: Close all database connections or viewers
```powershell
# Delete __pycache__ and restart
Remove-Item -Recurse __pycache__
python app.py
```

#### 3. **TemplateNotFound error**
**Solution**: Ensure templates directory exists and contains required HTML files
```powershell
# Verify structure
Get-ChildItem templates\
```

#### 4. **Login fails with correct credentials**
**Solution**: Password hashing issue, reset admin user:
```powershell
python
>>> from app import app, db, User
>>> from werkzeug.security import generate_password_hash
>>> with app.app_context():
...     admin = User.query.filter_by(email='admin@hospital.com').first()
...     admin.password = generate_password_hash('admin123')
...     db.session.commit()
```

#### 5. **Appointments not showing available slots**
**Solution**: Check JavaScript console for errors, ensure AJAX endpoint is accessible
- Verify `/get_available_slots/<doctor_id>/<date>` route works
- Check browser console (F12) for JavaScript errors

#### 6. **Static files (CSS/JS) not loading**
**Solution**: Clear browser cache or check static folder path
```powershell
# Verify static files exist
Get-ChildItem static\css\
Get-ChildItem static\js\
```

#### 7. **Port 5000 already in use**
**Solution**: Change port or kill existing process
```powershell
# Run on different port
python app.py --port 5001

# Or find and kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

---

## 🚀 Future Enhancements

### Planned Features
1. **Email Notifications**
   - Appointment confirmation emails
   - Reminder emails 24 hours before appointment
   - Medical record availability notifications

2. **Advanced Scheduling**
   - Recurring appointments
   - Emergency appointment slots
   - Doctor leave management
   - Waiting list functionality

3. **Reporting & Analytics**
   - Patient visit history reports
   - Doctor performance metrics
   - Department-wise statistics
   - Revenue tracking

4. **Payment Integration**
   - Online payment for consultation fees
   - Invoice generation
   - Payment history tracking

5. **Enhanced Security**
   - Two-factor authentication (2FA)
   - Role-based permission granularity
   - Audit logs for sensitive operations
   - Session timeout management

6. **Mobile Application**
   - React Native or Flutter app
   - Push notifications
   - Offline support

7. **Telemedicine Integration**
   - Video consultation support
   - Chat functionality
   - Prescription delivery tracking

8. **Document Management**
   - Upload lab reports
   - Store X-rays and scans
   - Prescription image uploads

9. **Improved UI/UX**
   - Responsive design improvements
   - Dark mode
   - Accessibility enhancements (WCAG compliance)
   - Multi-language support

10. **API Development**
    - RESTful API for mobile apps
    - API documentation (Swagger/OpenAPI)
    - Rate limiting and API keys

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 style guide for Python code
- Add docstrings to all functions
- Write unit tests for new features
- Update README.md for significant changes

### Bug Reports
Please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

---

## 📄 License

This project is developed for educational purposes. Feel free to use and modify as needed.

### Disclaimer
This is a prototype system for learning purposes. For production use in healthcare:
- Ensure HIPAA/GDPR compliance
- Implement proper data encryption
- Conduct security audits
- Obtain necessary certifications

---

## 📞 Support

For questions or support:
- Create an issue in the repository
- Email: admin@hospital.com (update with actual contact)

---

## 📚 Additional Resources

### Learn More
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [WTForms Documentation](https://wtforms.readthedocs.io/)
- [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/)

### Related Projects
- Hospital management systems on GitHub
- Healthcare management frameworks
- Medical record systems

---

## 🎓 Credits

Developed as part of hospital management system project.

**Technologies Used**:
- Flask, SQLAlchemy, WTForms, Werkzeug
- HTML, CSS, JavaScript
- SQLite

---

## 📝 Changelog

### Version 1.0.0 (Initial Release)
- User authentication and authorization
- Patient, Doctor, and Admin dashboards
- Appointment booking and management
- Medical record creation and viewing
- Department and doctor management
- Profile update functionality
- Password management for doctors

---

**Project Status**: ✅ Active Development

---

Made with ❤️ for better healthcare management
