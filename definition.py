import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Credential File link
CREDENTIALS_FILE = os.path.join(BASE_DIR, "data", "credentials.json")

# Folder Paths
Gallery_Folder = os.path.join(BASE_DIR, "static", "photos") + os.sep

# Web path used in image URLs (must stay relative)
Gallery_URL = "static/photos/"
