# FastOCR - API d'extraction de texte depuis des PDFs

Une API REST moderne et performante construite avec **FastAPI** pour extraire du texte depuis des fichiers PDF en utilisant la technologie OCR (Optical Character Recognition) avec **Tesseract**.

## 🚀 Fonctionnalités

- **Extraction de texte depuis PDFs** : Conversion automatique de PDFs en images puis extraction du texte via OCR
- **API REST asynchrone** : Architecture moderne avec FastAPI pour des performances optimales
- **Support multi-pages** : Traitement automatique de tous les pages d'un document PDF
- **Interface simple** : Endpoint unique et intuitif pour l'upload et l'extraction

## 🛠️ Technologies utilisées

- **FastAPI** : Framework web moderne et rapide pour construire des APIs
- **Tesseract OCR** : Moteur OCR open-source de Google
- **Pytesseract** : Wrapper Python pour Tesseract
- **pdf2image** : Conversion de PDFs en images
- **Pillow (PIL)** : Traitement d'images
- **Uvicorn** : Serveur ASGI haute performance

## 📋 Prérequis

### Système d'exploitation

- **macOS** : Utilisez Homebrew
- **Linux** : Utilisez apt-get ou votre gestionnaire de paquets
- **Windows** : Téléchargez les binaires depuis le site officiel

### Dépendances système

#### macOS
```bash
brew install tesseract poppler
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr poppler-utils
```

## 🔧 Installation

1. **Cloner le repository**
```bash
git clone <votre-repo-url>
cd fastapi-images-ocr
```

2. **Créer un environnement virtuel**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou
.venv\Scripts\activate  # Sur Windows
```

3. **Installer les dépendances Python**
```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Démarrer le serveur

```bash
uvicorn main:app --reload
```

Le serveur sera accessible sur `http://localhost:8000`

### Documentation interactive

Une fois le serveur démarré, accédez à :
- **Swagger UI** : `http://localhost:8000/docs`
- **ReDoc** : `http://localhost:8000/redoc`

### Endpoints

#### `GET /`
Retourne un message de bienvenue.

**Réponse :**
```json
{
  "message": "Hello World"
}
```

#### `POST /extract-pdf-text`
Extrait le texte d'un fichier PDF uploadé.

**Requête :**
- **Content-Type** : `multipart/form-data`
- **Body** : Fichier PDF (form-data avec clé `file`)

**Réponse :**
```json
{
  "message": "Texte extrait du PDF..."
}
```

### Exemple avec cURL

```bash
curl -X POST "http://localhost:8000/extract-pdf-text" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

### Exemple avec Python

```python
import requests

url = "http://localhost:8000/extract-pdf-text"
files = {"file": open("document.pdf", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

## 📁 Structure du projet

```
fast-ocr/
├── main.py              # Application FastAPI principale
├── requirements.txt     # Dépendances Python
└── README.md           # Documentation
```

## 🔍 Comment ça fonctionne ?

1. **Upload du PDF** : Le fichier PDF est reçu via l'endpoint POST
2. **Conversion en images** : Chaque page du PDF est convertie en image avec `pdf2image`
3. **OCR** : Tesseract analyse chaque image et extrait le texte
4. **Agrégation** : Le texte de toutes les pages est combiné
5. **Retour** : Le texte complet est renvoyé en JSON

## 🎯 Cas d'utilisation

- Digitalisation de documents papier scannés
- Extraction de texte depuis des PDFs non-éditables
- Automatisation de traitement de documents
- Archivage et indexation de documents
- Analyse de contenu de documents

## 📝 Notes

- La qualité de l'extraction dépend de la qualité du PDF source
- Les PDFs scannés nécessitent une bonne résolution pour de meilleurs résultats
- Le traitement peut prendre du temps pour les documents volumineux

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT.

---

**Développé avec ❤️ en utilisant FastAPI et Tesseract OCR**

