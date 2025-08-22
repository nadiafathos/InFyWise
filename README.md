# InFyWise Project
projet de fin de formation


InFyWise : API de gestion de la santé féminine

InFyWise est une API conçue pour aider les femmes à mieux comprendre et gérer leur parcours de santé, en particulier en ce qui concerne les symptômes, maladies (comme l'endométriose ou le SOPK) et le suivi médical. Elle permet la création d'un journal de symptômes, la prise de rendez-vous médicaux, le partage de témoignages et la consultation d'informations validées par des professionnels de santé.

🚀 Fonctionnalités Principales

Gestion des utilisateurs : Créez et gérez des profils avec des rôles distincts (patient, médecin, administrateur).

Journal de symptômes : Les patients peuvent enregistrer leurs symptômes quotidiens, leur intensité et leur type.

Prise de rendez-vous : Les patients peuvent planifier des consultations avec des médecins spécialisés.

Validation médicale : Les médecins peuvent consulter et valider les entrées de symptômes de leurs patients, et y ajouter des commentaires.

Modération de contenu : Les administrateurs peuvent gérer et valider les témoignages et les fiches maladies.

Fiches maladies : Accédez à une base de données d'informations sur les maladies féminines, modérées par des administrateurs.

Témoignages : Les patients peuvent partager leurs expériences, soumises à modération avant publication.
📝 User Stories pour les Rôles

👩‍⚕️ User Stories


En tant que Patient
Gestion de mon journal de symptômes


User Story : En tant qu’utilisateur avec le rôle Patient, je veux pouvoir enregistrer, modifier et consulter mes symptômes pour suivre l'évolution de ma santé au fil du temps.

Critères d'Acceptation :
Je peux créer une nouvelle entrée de symptôme, associée à mon id_patient.
Chaque entrée doit inclure une date, un type de symptôme, une intensité et une description.
Je peux visualiser l'historique complet de mes symptômes.
Prise de rendez-vous en ligne


User Story : En tant qu’utilisateur avec le rôle Patient, je veux pouvoir trouver un médecin et prendre un rendez-vous en ligne pour simplifier la gestion de mes consultations.

Critères d'Acceptation :
Je peux rechercher des médecins selon leur spécialité.
Je peux choisir un médecin et une date/heure pour créer un rendez-vous.
Le rendez-vous doit être enregistré et lié à mon id_patient et à l'id_medecin.
Partage de mon expérience


User Story : En tant qu’utilisateur avec le rôle Patient, je veux pouvoir soumettre un témoignage pour partager mon expérience avec la communauté et apporter mon soutien.


Critères d'Acceptation :
Je peux rédiger et soumettre un témoignage.
Le témoignage est associé à mon id_patient.
Le témoignage n'est visible publiquement qu'après sa validation par un administrateur.


En tant que Médecin
Accès aux dossiers patients

User Story : En tant qu’utilisateur avec le rôle Médecin, je veux pouvoir consulter les journaux de symptômes de mes patients pour obtenir un historique précis de leur état de santé.


Critères d'Acceptation :
Je peux accéder à la liste des patients avec qui j'ai un rendez-vous.
En sélectionnant un patient, je peux voir toutes les entrées de symptômes qui lui sont associées via son id_patient.


Validation et suivi des symptômes


User Story : En tant qu’utilisateur avec le rôle Médecin, je veux pouvoir valider les entrées de symptômes d'un patient et y ajouter des commentaires pour enrichir le suivi médical.

Critères d'Acceptation :
Je peux sélectionner une entrée de symptôme spécifique.
Je peux marquer cette entrée comme validée et ajouter un commentaire, qui est enregistré dans la table Validation et lié à mon id_medecin et à l'id_symptome.


En tant qu'Administrateur
Modération des témoignages
User Story : En tant qu’utilisateur avec le rôle Administrateur, je veux pouvoir modérer les témoignages soumis pour garantir que le contenu partagé est pertinent et respectueux.


Critères d'Acceptation :
Je peux consulter une liste de tous les témoignages en attente de validation.
Je peux valider ou rejeter un témoignage, ce qui met à jour le champ validé dans la table Temoignage.
Gestion des fiches maladies


User Story : En tant qu’utilisateur avec le rôle Administrateur, je veux pouvoir créer et mettre à jour des fiches maladies pour que les utilisateurs aient accès à des informations fiables.
Critères d'Acceptation :
Je peux ajouter une nouvelle FicheMaladie avec un titre, une description et une catégorie.
Je peux modifier ou supprimer des fiches maladies existantes.

📊 Diagramme UML – Schéma relationnel




    USER {
        int id_user PK
        string nom
        string prenom
        string email
        string mot_de_passe
        enum role
        date date_inscription
    }

    PATIENT {
        int id_patient PK, FK -> USER.id_user
        date date_naissance
    }

    MEDECIN {
        int id_medecin PK, FK -> USER.id_user
        string specialite
        string hopital
    }

    ADMIN {
        int id_admin PK, FK -> USER.id_user
    }

    SYMPTOMEENTRY {
        int id_symptome PK
        int id_patient FK -> PATIENT.id_patient
        date date_enregistrement
        string type_symptome
        int intensite
        text description
    }

    RENDEZVOUS {
        int id_rdv PK
        int id_patient FK -> PATIENT.id_patient
        int id_medecin FK -> MEDECIN.id_medecin
        date date_rdv
        string type_rdv
        string statut
    }

    FICHEMALADIE {
        int id_maladie PK
        string titre
        text description
        string categorie
        date date_maj
    }

    TEMOIGNAGE {
        int id_temoignage PK
        int id_patient FK -> PATIENT.id_patient
        text contenu
        date date_post
        bool valide
    }

    VALIDATION {
        int id_validation PK
        int id_symptome FK -> SYMPTOMEENTRY.id_symptome
        int id_medecin FK -> MEDECIN.id_medecin
        text commentaire
        date date_validation
    }

    %% Relations

    USER ||--|| PATIENT : "est un"
    USER ||--|| MEDECIN : "est un"
    USER ||--|| ADMIN : "est un"

    PATIENT ||--o{ SYMPTOMEENTRY : "enregistre"
    PATIENT ||--o{ RENDEZVOUS : "prend"
    PATIENT ||--o{ TEMOIGNAGE : "écrit"
    MEDECIN ||--o{ RENDEZVOUS : "assure"
    MEDECIN ||--o{ VALIDATION : "valide"
    SYMPTOMEENTRY ||--o{ VALIDATION : "est validé par"
    ADMIN ||--o{ FICHEMALADIE : "gère"
    ADMIN ||--o{ TEMOIGNAGE : "modère"

📘 Modèle Logique de Données (MLD)

USER(id_user PK, nom, prénom, email, mot_de_passe, rôle, date_inscription)

PATIENT(id_patient PK, id_user FK→USER.id_user, date_naissance)

MÉDECIN(id_medecin PK, id_user FK→USER.id_user, spécialité, hôpital)

ADMIN(id_admin PK, id_user FK→USER.id_user)

SYMPTOMEENTRY(id_symptome PK, id_patient FK→PATIENT.id_patient,
date_enregistrement, type_symptome, intensite, description)

RENDEZVOUS(id_rdv PK, id_patient FK→PATIENT.id_patient,
id_medecin FK→MEDECIN.id_medecin, date_rdv, type_rdv, statut)

FICHEMALADIE(id_maladie PK, titre, description, catégorie, date_maj)

TEMOIGNAGE(id_temoignage PK, id_patient FK→PATIENT.id_patient,
contenu, date_post, valide)

VALIDATION(id_validation PK, id_symptome FK→SYMPTOMEENTRY.id_symptome,
id_medecin FK→MEDECIN.id_medecin, commentaire, date_validation)


















📌 Fiche Technique – InFyWise

🛠️ Technologies utilisées

Backend (API)

Framework : Flask (Python 3.11+)


Base de données : PostgreSQL


ORM : SQLAlchemy + Marshmallow (validation/sérialisation)


Authentification : JWT (JSON Web Token)


Tests : Postman / Thunder Client


Architecture : RESTful API (MVC simplifié)


Conteneurisation : Docker & Docker Compose


Frontend (WebApp)
Framework : Angular 20+


IDE : WebStorm (JetBrains)


UI/UX : TaiinlwdCSS + Angular Material


Routing : Angular Router


Gestion d’état : RxJS


Build : Webpack 5 (via Angular CLI)


Gestion de projet & Déploiement
Versionning : Git


Hébergement repo : GitHub (perso) + GitLab 


CI/CD : GitLab CI/CD (optionnel)


Déploiement : Docker (backend + frontend dans containers séparés)


Documentation : Swagger/OpenAPI + README



📂 Architecture du projet
projet-sante/
│── backend/                  # API Flask
│   ├── app/                  # Code source Flask
│   │   ├── routes/           # Routes REST
│   │   ├── models/           # Modèles SQLAlchemy
│   │   ├── schemas/          # Schemas Marshmallow
│   │   ├── services/         # Logique métier
│   │   └── __init__.py
│   ├── tests/                # Tests unitaires API
│   ├── config.py             # Config DB, JWT...
│   ├── requirements.txt      # Dépendances Python
│   └── wsgi.py               # Entrée Flask
│
│── frontend/                 # Application Angular
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/   # Composants UI
│   │   │   ├── pages/        # Pages (rendez-vous, symptômes…)
│   │   │   ├── services/     # Services API
│   │   │   └── guards/       # Auth Guards
│   ├── angular.json
│   ├── package.json
│   └── tsconfig.json
│
│── docker-compose.yml        # Orchestration containers
│── Dockerfile.backend        # Image Flask
│── Dockerfile.frontend       # Image Angular
│── README.md                 # Documentation

🔑 Fonctionnalités principales
Utilisateurs
Création et gestion de comptes (Patient, Médecin, Admin)


Authentification sécurisée par JWT


Gestion des rôles et permissions


Patients
Enregistrement des symptômes


Prise de rendez-vous avec un médecin


Rédaction de témoignages


Médecins
Consultation et validation des symptômes


Suivi des patients


Gestion des rendez-vous


Admin
Gestion des fiches maladies


Modération des témoignages


Supervision des utilisateurs











