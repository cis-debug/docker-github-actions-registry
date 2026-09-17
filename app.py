"""
app.py
Petit module Python simple pour démontrer une pipeline DevOps :
- tests pytest
- build d'une image Docker
- push automatique vers Docker Hub (plus tard via GitHub Actions)
"""

def add(a: int, b: int) -> int:
    """Retourne la somme de a et b."""
    return a + b


def greet(name: str) -> str:
    """Retourne une phrase de salutation."""
    return f"Hello {name}!"


if __name__ == "__main__":
    # Message simple pour vérifier que l'image Docker s'exécute bien
    print(greet("from Docker Hub CI"))
