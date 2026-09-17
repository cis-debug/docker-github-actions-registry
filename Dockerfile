# Image de base officielle Python (légère)
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier requirements en premier pour profiter du cache Docker
COPY requirements.txt /app/requirements.txt

# Installer dépendances (ici pytest, suffisant pour la démo)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le code
COPY app.py /app/app.py

# Commande par défaut
CMD ["python", "/app/app.py"]
