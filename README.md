
🎓 Final Project
InFyWise: Women’s Health Management API

InFyWise is an API designed to help women better understand and manage their health journey, particularly regarding symptoms, diseases (such as endometriosis or PCOS), and medical follow-up.
It enables the creation of a symptom journal, scheduling of medical appointments, sharing of testimonies, and access to reliable health information validated by professionals.

🚀 Key Features

User Management: Create and manage profiles with distinct roles (Patient, Doctor, Administrator).

Symptom Journal: Patients can record their daily symptoms, intensity, and type.

Appointment Scheduling: Patients can book consultations with specialized doctors.

Medical Validation: Doctors can review and validate symptom entries, adding comments.

Content Moderation: Administrators can manage and validate testimonies and disease files.

Disease Files: Access a database of information on women’s health conditions, curated by administrators.

Testimonies: Patients can share their experiences, subject to moderation before publication.

📝 User Stories per Role
👩‍🦰 As a Patient
Manage my Symptom Journal

User Story: As a Patient, I want to record, edit, and view my symptoms to track my health evolution over time.

Acceptance Criteria:

I can create a new symptom entry linked to my id_patient.

Each entry must include a date, symptom type, intensity, and description.

I can view the complete history of my symptoms.

Book Online Appointments

User Story: As a Patient, I want to find a doctor and book an appointment online to simplify managing my consultations.

Acceptance Criteria:

I can search for doctors by specialty.

I can choose a doctor and a date/time to schedule an appointment.

The appointment must be recorded and linked to my id_patient and the doctor’s id_doctor.

Share my Experience

User Story: As a Patient, I want to submit a testimony to share my experience with the community and provide support.

Acceptance Criteria:

I can write and submit a testimony.

The testimony is linked to my id_patient.

The testimony is only visible publicly after validation by an Administrator.

👨‍⚕️ As a Doctor
Access Patient Records

User Story: As a Doctor, I want to view my patients’ symptom journals to have a precise history of their health status.

Acceptance Criteria:

I can access the list of patients with whom I have an appointment.

By selecting a patient, I can view all symptom entries linked to their id_patient.

Validate and Follow Up on Symptoms

User Story: As a Doctor, I want to validate patient symptom entries and add comments to enrich medical follow-up.

Acceptance Criteria:

I can select a specific symptom entry.

I can mark this entry as validated and add a comment.

The validation is saved in the Validation table, linked to my id_doctor and the id_symptom.

🛡️ As an Administrator
Testimony Moderation

User Story: As an Administrator, I want to moderate submitted testimonies to ensure that shared content is relevant and respectful.

Acceptance Criteria:

I can view a list of all testimonies pending validation.

I can approve or reject a testimony, which updates the validated field in the Testimony table.

Manage Disease Files

User Story: As an Administrator, I want to create and update disease files so that users have access to reliable health information.

Acceptance Criteria:

I can add a new DiseaseFile with a title, description, and category.

I can update or delete existing disease files.

## 📊 UML Diagram

```mermaid
classDiagram
    class USER {
        int id_user PK
        string last_name
        string first_name
        string email
        string password
        enum role
        date registration_date
    }

    class PATIENT {
        int id_patient PK, FK -> USER.id_user
        date birth_date
    }

    class DOCTOR {
        int id_doctor PK, FK -> USER.id_user
        string specialty
        string hospital
    }

    class ADMIN {
        int id_admin PK, FK -> USER.id_user
    }

    class SYMPTOM_ENTRY {
        int id_symptom PK
        int id_patient FK -> PATIENT.id_patient
        date record_date
        string symptom_type
        int intensity
        text description
    }

    class APPOINTMENT {
        int id_appointment PK
        int id_patient FK -> PATIENT.id_patient
        int id_doctor FK -> DOCTOR.id_doctor
        date appointment_date
        string appointment_type
        string status
    }

    class DISEASE_FILE {
        int id_disease PK
        string title
        text description
        string category
        date last_update
    }

    class TESTIMONY {
        int id_testimony PK
        int id_patient FK -> PATIENT.id_patient
        text content
        date post_date
        bool validated
    }

    class VALIDATION {
        int id_validation PK
        int id_symptom FK -> SYMPTOM_ENTRY.id_symptom
        int id_doctor FK -> DOCTOR.id_doctor
        text comment
        date validation_date
    }

    %% Relations
    USER <|-- PATIENT : "is a"
    USER <|-- DOCTOR : "is a"
    USER <|-- ADMIN : "is a"

    PATIENT "1" --> "0..*" SYMPTOM_ENTRY : "records"
    PATIENT "1" --> "0..*" APPOINTMENT : "books"
    PATIENT "1" --> "0..*" TESTIMONY : "writes"

    DOCTOR "1" --> "0..*" APPOINTMENT : "handles"
    DOCTOR "1" --> "0..*" VALIDATION : "validates"

    SYMPTOM_ENTRY "1" --> "0..*" VALIDATION : "validated by"

    ADMIN "1" --> "0..*" DISEASE_FILE : "manages"
    ADMIN "1" --> "0..*" TESTIMONY : "moderates"

 ```


📘 Logical Data Model (LDM)

USER(id_user PK, last_name, first_name, email, password, role, registration_date)

PATIENT(id_patient PK, id_user FK→USER.id_user, birth_date)

DOCTOR(id_doctor PK, id_user FK→USER.id_user, specialty, hospital)

ADMIN(id_admin PK, id_user FK→USER.id_user)

SYMPTOM_ENTRY(id_symptom PK, id_patient FK→PATIENT.id_patient,
record_date, symptom_type, intensity, description)

APPOINTMENT(id_appointment PK, id_patient FK→PATIENT.id_patient,
id_doctor FK→DOCTOR.id_doctor, appointment_date, appointment_type, status)

DISEASE_FILE(id_disease PK, title, description, category, last_update)

TESTIMONY(id_testimony PK, id_patient FK→PATIENT.id_patient,
content, post_date, validated)

VALIDATION(id_validation PK, id_symptom FK→SYMPTOM_ENTRY.id_symptom,
id_doctor FK→DOCTOR.id_doctor, comment, validation_date)


📌 Technical Sheet – InFyWise
🛠️ Technologies Used
Backend (API)

Framework: Flask (Python 3.11+)

Database: PostgreSQL

ORM: SQLAlchemy + Marshmallow (validation/serialization)

Authentication: JWT (JSON Web Token)

Testing: Postman / Thunder Client

Architecture: RESTful API (simplified MVC)

Containerization: Docker & Docker Compose

Frontend (WebApp)

Framework: Angular 20+

IDE: WebStorm (JetBrains)

UI/UX: TailwindCSS + Angular Material

Routing: Angular Router

State Management: RxJS

Build Tool: Webpack 5 (via Angular CLI)

Project Management & Deployment

Version Control: Git

Repository Hosting: GitHub (personal) + GitLab

CI/CD: GitLab CI/CD (optional)

Deployment: Docker (backend + frontend in separate containers)

Documentation: Swagger/OpenAPI + README

📂 Project Architecture
projet-sante/
│── backend/                  # Flask API
│   ├── app/                  # Flask source code
│   │   ├── routes/           # REST routes
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Marshmallow schemas
│   │   ├── services/         # Business logic
│   │   └── __init__.py
│   ├── tests/                # API unit tests
│   ├── config.py             # DB, JWT configuration...
│   ├── requirements.txt      # Python dependencies
│   └── wsgi.py               # Flask entry point
│
│── frontend/                 # Angular application
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/   # UI components
│   │   │   ├── pages/        # Pages (appointments, symptoms…)
│   │   │   ├── services/     # API services
│   │   │   └── guards/       # Auth Guards
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
│
│── docker-compose.yml        # Containers orchestration
│── Dockerfile.backend        # Flask image
│── Dockerfile.frontend       # Angular image
│── README.md                 # Documentation

🔑 Main Features
Users

Account creation & management (Patient, Doctor, Admin)

Secure JWT authentication

Role & permission management

Patients

Symptom tracking

Booking appointments with doctors

Writing & submitting testimonials

Doctors

Reviewing and validating symptoms

Patient monitoring

Managing appointments

Administrators

Managing disease information sheets

Moderating testimonials

Supervising users

📂 Backend Structure
backend/
│── app.py              # Flask app entry point
│── requirements.txt    # Python dependencies
│
├── app/                # Main API code
│   ├── __init__.py     # Initialize Flask app
│   ├── routes/         # Route files
│   │   ├── __init__.py
│   │   └── user_routes.py
│   ├── models/         # Model files (DB later)
│   │   ├── __init__.py
│   │   └── user_model.py
│   └── services/       # Business logic (optional for later)
│       └── __init__.py














