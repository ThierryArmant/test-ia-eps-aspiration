import os
import requests
from bs4 import BeautifulSoup

# Création du dossier de stockage s'il n'existe pas
if not os.path.exists("data_aspirations"):
    os.makedirs("data_aspirations")

def aspirer_rubriques():
    rubriques = [2, 4, 7]
    for r in rubriques:
        url = f"https://ipackeps.ac-creteil.fr/spip.php?rubrique{r}"
        print(f"--- Aspiration de la rubrique {r} ---")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraction des articles du CMS SPIP
        articles = soup.find_all('div', class_='article')
        with open(f"data_aspirations/rubrique_{r}.txt", "w", encoding="utf-8") as f:
            for art in articles:
                titre = art.find('h2').get_text(strip=True) if art.find('h2') else "Sans titre"
                corps = art.get_text(separator='\n', strip=True)
                f.write(f"\n[TITRE : {titre}]\n{corps}\n---")
    print("Aspiration terminée.")

if __name__ == "__main__":
    aspirer_rubriques()
