# UE19-Lab-05 : Application d'API de Blagues

Ce projet est un simple script Python qui interroge [JokesAPI](https://jokeapi.dev/) pour récupérer une blague de programmation en français et l'afficher dans la console.

## 🚀 Fonctionnalités

* Effectue un appel GET à une API publique (`JokesAPI`).
* Analyse la réponse JSON.
* Gère les blagues en une partie (type `single`) et en deux parties (type `twopart`).
* Gère les erreurs de base (erreurs HTTP, de connexion).

## 🛠️ Comment l'installer et le lancer

Vous pouvez lancer ce projet de deux manières : localement avec Python ou via Docker.

### 1. Exécution locale (avec Python)

**Prérequis :**
* [Python 3](https://www.python.org/) (version 3.7+ recommandée)
* [Git](https://git-scm.com/)

**Instructions :**

1.  Clonez ce repository sur votre machine :
    ```bash
    git clone [https://github.com/](https://github.com/)[VOTRE_NOM_UTILISATEUR]/ue19-lab-05.git
    cd ue19-lab-05
    ```

2.  (Optionnel mais recommandé) Créez un environnement virtuel :
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4.  Exécutez l'application :
    ```bash
    python app.py
    ```

### 2. Exécution avec Docker

**Prérequis :**
* [Docker](https://www.docker.com/products/docker-desktop/)

**Instructions :**

1.  Clonez le repository (si ce n'est pas déjà fait) :
    ```bash
    git clone [https://github.com/](https://github.com/)[VOTRE_NOM_UTILISATEUR]/ue19-lab-05.git
    cd ue19-lab-05
    ```

2.  Construisez l'image Docker :
    Le `.` à la fin indique à Docker de chercher le `Dockerfile` dans le dossier actuel.
    ```bash
    docker build -t blague-api .
    ```

3.  Lancez un conteneur basé sur l'image que vous venez de créer :
    `--rm` supprime le conteneur après son exécution pour nettoyer.
    ```bash
    docker run --rm blague-api
    ```
