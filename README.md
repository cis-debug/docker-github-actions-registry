# 🚀 Docker Registry + GitHub Actions

## 📌 Description

Ce projet met en place une pipeline CI/CD avec **GitHub Actions** permettant de :

* tester une application Python avec `pytest`
* construire une image Docker
* se connecter automatiquement à Docker Hub
* publier automatiquement l'image Docker sur Docker Hub

L'objectif est de comprendre le fonctionnement d'une pipeline DevOps allant du **Git Push** jusqu'à la publication d'une image dans un **Container Registry**.

---

## 🎯 Objectif

Le projet automatise le processus suivant :

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
🧪 Tests Python
   │
   ▼
🐳 Build Docker
   │
   ▼
🔐 Login Docker Hub
   │
   ▼
📦 Push de l'image
   │
   ▼
Docker Hub
```

---

## 🏗️ Architecture

```text
                    GitHub
                       │
                       │ git push
                       ▼
              ┌─────────────────┐
              │ GitHub Actions  │
              └────────┬────────┘
                       │
                       ▼
                🧪 Python Tests
                       │
                  tests OK ✅
                       │
                       ▼
                 🐳 Docker Build
                       │
                       ▼
               🔐 Docker Login
                       │
                       ▼
                📦 Docker Hub
                       │
                       ▼
             Docker Image :latest
```

---

## 📁 Structure du projet

```text
docker-github-actions-registry/
│
├── .github/
│   └── workflows/
│       └── docker.yml
│
├── .dockerignore
├── Dockerfile
├── app.py
├── requirements.txt
├── test_app.py
└── README.md
```

---

## 🐍 Application Python

L'application contient trois fonctions simples :

```python
add()
multiply()
is_even()
```

Elle affiche également quelques résultats lorsqu'elle est exécutée.

Exemple :

```text
================================
   DOCKER REGISTRY PROJECT
================================

2 + 3 = 5
4 × 5 = 20
Is 10 even? True
```

---

## 🧪 Tests Python

Les tests sont réalisés avec **pytest**.

Les tests vérifient :

* l'addition
* la multiplication
* la vérification d'un nombre pair

Commande utilisée :

```bash
python3 -m pytest
```

Résultat attendu :

```text
3 passed
```

---

## 🐳 Docker

L'application est exécutée dans un container Docker basé sur :

```text
python:3.12-slim
```

### Construire l'image

```bash
docker build -t docker-registry-python .
```

### Exécuter le container

```bash
docker run --rm docker-registry-python
```

---

## 📦 Docker Hub

L'image Docker est automatiquement publiée sur **Docker Hub** grâce à GitHub Actions.

Format de l'image :

```text
USERNAME/docker-github-actions-registry:latest
```

Le tag utilisé dans ce projet est :

```text
latest
```

---

## ⚙️ GitHub Actions

Le workflow se trouve dans :

```text
.github/workflows/docker.yml
```

Il contient deux jobs :

### 1. Python Tests

Le premier job :

* récupère le repository
* installe Python
* installe les dépendances
* exécute `pytest`

```text
Python Tests
     │
     ▼
   pytest
```

---

### 2. Build and Push Docker Image

Le deuxième job :

* se connecte à Docker Hub
* configure Docker Buildx
* construit l'image
* publie l'image sur Docker Hub

Le job Docker utilise :

```yaml
needs: test
```

Cela signifie que la publication Docker ne peut avoir lieu que si les tests Python réussissent.

```text
Tests ✅
   │
   ▼
Docker Build
   │
   ▼
Docker Push
```

Si les tests échouent :

```text
Tests ❌
   │
   X
Docker Push arrêté
```

---

## 🔐 GitHub Secrets

Les identifiants Docker Hub ne sont pas écrits directement dans le code.

Deux **GitHub Secrets** sont utilisés :

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Le token Docker Hub est utilisé à la place du mot de passe du compte.

Dans GitHub :

```text
Settings
   ↓
Secrets and variables
   ↓
Actions
```

Puis les secrets sont utilisés dans le workflow :

```yaml
username: ${{ secrets.DOCKERHUB_USERNAME }}
password: ${{ secrets.DOCKERHUB_TOKEN }}
```

⚠️ Aucun mot de passe ou token n'est présent dans le repository.

---

## 🔄 Pipeline CI/CD

Le pipeline complet est :

```text
        git push
           │
           ▼
   GitHub Actions
           │
           ▼
    Python Tests
           │
       ┌───┴───┐
       │       │
      ❌      ✅
       │       │
     STOP      ▼
          Docker Build
               │
               ▼
         Docker Login
               │
               ▼
          Docker Push
               │
               ▼
           Docker Hub
```

---

## 🧪 Test de fonctionnement

Un test volontairement incorrect a été utilisé afin de vérifier le comportement de la pipeline.

Lorsque le test échoue :

```text
Python Tests ❌
```

le job Docker n'est pas exécuté grâce à :

```yaml
needs: test
```

Après restauration du test :

```text
Python Tests ✅
        ↓
Docker Build and Push ✅
```

---

## 📥 Télécharger l'image depuis Docker Hub

Une fois l'image publiée, elle peut être récupérée avec :

```bash
docker pull USERNAME/docker-github-actions-registry:latest
```

Puis exécutée avec :

```bash
docker run --rm USERNAME/docker-github-actions-registry:latest
```

---

## 🛠️ Technologies utilisées

* 🐍 Python
* 🧪 pytest
* 🐳 Docker
* 📦 Docker Hub
* ⚙️ GitHub Actions
* 🔐 GitHub Secrets
* 🏗️ Docker Buildx
* 🔧 Git
* 🐧 Linux / WSL

---


## 🚀 Améliorations possibles

Évolutions possibles du projet :

* ajouter plusieurs tags Docker (`latest`, version, commit SHA)
* publier automatiquement plusieurs architectures
* ajouter un scan de sécurité de l'image
* utiliser Docker Compose
* ajouter un environnement de staging
* déployer automatiquement le container
* ajouter des notifications de pipeline
* utiliser une stratégie de versioning automatique

---

## 🎓 Ce que je retiens

Cette mission m'a permis de comprendre le principe d'une pipeline CI/CD complète :

```text
Code
 ↓
Tests
 ↓
Build
 ↓
Registry
 ↓
Image Docker
```

J'ai également appris à utiliser des secrets pour éviter d'exposer des informations sensibles dans le code source.

---

## 👩‍💻 Auteur

**Cisse Ndeye**

GitHub :

https://github.com/cis-debug
