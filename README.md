# Django Forms Challenge

## Description

This challenge was made as a live coding interview, and I decided to make it part of my portfolio.

## Installation

1. Clone the repository locally
`git clone git@github.com:Naveduran/DjangoFormsChallenge.git`
or
`git clone https://github.com/Naveduran/DjangoFormsChallenge.git`

2. Install the requirements:
`pip install -t requirements.txt`

3. Set the database:
`python3 manage.py makemigrations && python3 manage.py migrate`

4. Run the server:
`python3 manage.py runserver`
Click the link to see the page.

5. Optionally, create superuser credentials to see the admin platform:
`python3 manage.py createsuperuser`

## Challenge Instructions(English)

Create a project called “Test”
Create within this an app called “Academy”
The app must contain a home template with 2 buttons:

- The first button called "Student Info" should lead to another template where the fields can be entered: ID (mandatory for front and only numeric), name (only letters), Phone (only numbers)

- The second button called "Assignments" should lead to a template that allows you to associate a subject to any previously entered student (subject records can be entered by the admin).

Both the student entry and the subject assignment must have the layout and style of this mockup: (Sadly I could not download the image to show it here).

Design the model considering all of the above and please include all the respective validations.

## Challenge Instructions(Original in Spanish)

Cree un proyecto llamado “Test”
Cree dentro de este una app llamada “Academy”
La app debe contener un template home con 2 botones:

- El primer botón llamado “Student Info” debe dirigir a otro template donde se puedan ingresar los campos: ID (obligatorio por front y solo númerico), name (solo letras), Phone (solo números)

- El segundo botón llamado “Assignments” debe llevar a un template que permita asociarle una materia a cualquier estudiante ingresado previamente (los registros de materia pueden ingresarse por el admin).

Tanto el ingreso de students como de asignación de materia deben tener el maquetado y estilo de este mockup:(Tristemente no pude descargar la imagen para mostrarla aqui).

Diseñe el modelo considerando todo lo anterior y por favor incluya todas las validaciones respectivas.

## Included components

- Models: Student and Assignment.
- Forms, Views, and Urls:
	+ Home: Main menu to enter into the other views.
	+ Student Info: Allows creating an student.
	+ Assignments: Allow assign a new course to a student.
- Admin: basic registration of the models to allow the courses creation.

## End

Thanks for visiting!
