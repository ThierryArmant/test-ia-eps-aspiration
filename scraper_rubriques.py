import os
import requests
from bs4 import BeautifulSoup

# URL de base du site
BASE_URL = "https://ipackeps.ac-creteil.fr"

def extraire_article(url_article):
    r = requests.get(url_article)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Extraction des éléments
    titre = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Sans_titre"
    texte = soup.find('div', class_='texte').get_text(separator='\n', strip=True) if soup.find('div', class_='texte') else "Pas de texte"
    video = soup.find('iframe')['src'] if soup.find('iframe') else "Pas de vidéo"
    
    # Recherche de la FAQ (souvent dans une div spécifique ou liste)
    faq = soup.find('div', class_='faq').get_text(separator='\n', strip=True) if soup.find('div', class_='faq') else "Pas de FAQ"
    
    return f"TITRE: {titre}\n\nTEXTE: {texte}\n\nVIDEO: {video}\n\nFAQ: {faq}"

def scraper():
    rubriques = [2, 4, 7]
    for r in rubriques:
        url_rubrique = f"{BASE_URL}/spip.php?rubrique{r}"
        r_page = requests.get(url_rubrique)
        soup = BeautifulSoup(r_page.content, 'html.parser')
        
        # On trouve tous les liens vers les articles
        # Note : Il faudra peut-être ajuster le sélecteur selon la classe CSS du site
        liens = soup.select('a.titre.ajax') 
        
        for lien in liens:
            url_art = BASE_URL + "/" + lien['href']
            contenu = extraire_article(url_art)
            
            # Sauvegarde dans un fichier propre par article
            nom_fichier = f"{titre_propre(lien.text)}.txt"
            with open(f"data_aspirations/{nom_fichier}", "w", encoding="utf-8") as f:
                f.write(contenu)

def titre_propre(t):
    return "".join([c if c.isalnum() else "_" for c in t])[:50]

if __name__ == "__main__":
    scraper()
