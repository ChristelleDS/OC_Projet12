# EpicEvents
Application CRM avec une interface API REST.
Développée avec Django et Django Rest Framework.

## Features

Documentation Postman disponible en ligne :
https://documenter.getpostman.com/view/23302006/2s8YsxuAyr


## Installation & lancement

Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/ChristelleDS/OC_Projet12
```
Se placer dans le dossier téléchargé, puis créer un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate   ( ou env\scripts\activate.bat)
```
Linux:
```
source env/bin/activate
```
Installez ensuite les packages requis:
```
pip install -r requirements.txt
```
Ensuite, placez vous à la racine du projet (là ou se trouve le fichier manage.py), puis effectuez les migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Lancer le serveur: 
```
python manage.py runserver
```

## Créer un compte

Pour créer un compte administrateur: 
```
$ python manage.py createsuperuser
```
Vous pouvez ensuite créer un compte utilisateur via http://localhost:8000/api/createUser/ 
ou depuis l'administration du site : http://localhost:8000/admin/
Vous pouvez ensuite utiliser l'applicaton via les différents endpoints décrits dans la documentation. 

## ADMINISTRATION

L'interface d'administration du site permet à un administrateur d'accéder aux fonctionnalités suivantes:
- administration des utilisateurs et de leurs droits
- consultation et édition des données du modèle (client, contrats, évènement etc)
- consultation des logs

Un utilisateur non administrateur accède :
- en lecture aux données du modèle 
- en écriture qu'aux données pour lesquelles il est référent.

Plusieurs groupes d'authorisations ont été implémentées:
- MANAGEMENT : droits d'administrateur
- SALES 
- SUPPORT 

