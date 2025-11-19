# Utiliser une image Python officielle comme image de base
# 'slim' est une version légère, idéale pour la production
FROM python:3.7-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances listées dans requirements.txt
# --no-cache-dir pour ne pas stocker le cache pip (réduit la taille de l'image)
# -r pour "requirements"
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script de l'application dans le répertoire de travail
COPY app.py .

# Commande à exécuter lorsque le conteneur démarre
# Équivaut à lancer "python app.py" dans le terminal
CMD ["python", "app.py"]
