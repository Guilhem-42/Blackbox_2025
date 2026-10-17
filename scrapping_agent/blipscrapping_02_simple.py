#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Liste de mots vides courants à exclure dans l'analyse
STOP_WORDS = {
    "de", "la", "le", "les", "et", "des", "en", "un", "une", "du", "pour", "sur",
    "avec", "par", "au", "aux", "ce", "ces", "dans", "qui", "que", "se", "plus",
    "ne", "pas", "ou", "mais", "comme", "a", "il", "elle", "nous", "vous", "ils",
    "elles", "son", "sa", "ses", "être", "avoir", "faire", "tout", "sans", "sont"
}ls

def scraper_titres(url="https://techcrunch.com/"):
    """Scrape les titres d'articles récents sur TechCrunch."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erreur HTTP {response.status_code} lors du scraping")
    soup = BeautifulSoup(response.text, 'html.parser')
    titres = []
    for a in soup.find_all('a', class_='post-block__title__link'):
        titre = a.get_text(strip=True)
        if titre:
            titres.append(titre)
    return titres

def analyser_frequence_mots(titres):
    """Analyse la fréquence des mots dans les titres, excluant les stop words."""
    mots = []
    for titre in titres:
        mots_titre = re.findall(r'\b\w+\b', titre.lower())
        mots.extend([mot for mot in mots_titre if mot not in STOP_WORDS and len(mot) > 2])
    compteur = Counter(mots)
    return compteur.most_common(10)

def generer_rapport_texte(mots_freq, titres):
    """Génère un rapport texte des résultats."""
    rapport = f"""
=== RAPPORT D'ANALYSE DES TENDANCES TECH ===

Nombre d'articles analysés : {len(titres)}

=== TOP 10 DES MOTS CLÉS ===
"""
    for i, (mot, freq) in enumerate(mots_freq, 1):
        rapport += f"{i:2d}. {mot:<15} : {freq} occurrences\n"
    
    rapport += f"""
=== LISTE DES TITRES ANALYSÉS ===
"""
    for i, titre in enumerate(titres, 1):
        rapport += f"{i:2d}. {titre}\n"
    
    rapport += f"""
=== FIN DU RAPPORT ===
Généré automatiquement avec blipscrapping_02_simple.py
"""
    return rapport

if __name__ == "__main__":
    try:
        print("Démarrage du scraping de TechCrunch...")
        titres = scraper_titres()
        if not titres:
            print("Aucun titre récupéré, vérifiez l'URL ou la structure du site.")
        else:
            print(f"✓ {len(titres)} titres récupérés avec succès")
            
            print("Analyse de la fréquence des mots...")
            mots_freq = analyser_frequence_mots(titres)
            
            print("Génération du rapport...")
            rapport = generer_rapport_texte(mots_freq, titres)
            
            # Sauvegarde du rapport dans un fichier texte
            with open("rapport_tendances_tech.txt", "w", encoding="utf-8") as f:
                f.write(rapport)
            
            print("✓ Rapport généré avec succès : rapport_tendances_tech.txt")
            
            # Affichage du résumé
            print("\n=== RÉSUMÉ ===")
            print(f"Articles analysés : {len(titres)}")
            print("Top 5 des mots clés :")
            for i, (mot, freq) in enumerate(mots_freq[:5], 1):
                print(f"  {i}. {mot} ({freq} occurrences)")
                
    except Exception as e:
        print(f"Erreur : {e}")
