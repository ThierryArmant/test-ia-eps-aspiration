import os
import streamlit as st
from llama_index.core import Document

def charger_documents_aspirations():
    documents = []
    dossier = "data_aspirations"
    
    # On vérifie que le dossier existe
    if os.path.exists(dossier):
        for fichier in os.listdir(dossier):
            # Il va lire chaque fichier .txt trouvé dans le dossier
            if fichier.endswith(".txt"):
                chemin_complet = os.path.join(dossier, fichier)
                with open(chemin_complet, "r", encoding="utf-8") as f:
                    contenu = f.read()
                    documents.append(Document(text=contenu, metadata={"source": fichier}))
    return documents
