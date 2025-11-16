from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, DateTimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=200)])
    submit = SubmitField('Register')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Login As', choices=[
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Administrator')
    ], validators=[DataRequired()])
    submit = SubmitField('Login')
class AppointmentForm(FlaskForm):
    doctor_id = StringField('Doctor ID', validators=[DataRequired()])
    appointment_date = DateField('Appointment Date', validators=[DataRequired()])
    time_slot = StringField('Time Slot', validators=[DataRequired()])
    submit = SubmitField('Book Appointment')
class MedicalRecordForm(FlaskForm):
    diagnosis = TextAreaField('Diagnosis', validators=[DataRequired()])
    prescription = TextAreaField('Prescription', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Record')