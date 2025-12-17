import webbrowser
import sys
import time

def banner():
    print("""
    #############################################
    #           OSINT INVESTIGATOR              #
    #     Recherche Rapide & Google Dorks       #
    #     Bachelor Cybersec Project             #
    #############################################
    """)

def search_username(target):
    """ Ouvre les pages de recherche pour un pseudo donné. """
    print(f"\n[+] Recherche du pseudo '{target}' sur les réseaux...")
    urls = [
        f"https://www.google.com/search?q=site:instagram.com+%22{target}%22",
        f"https://www.google.com/search?q=site:twitter.com+%22{target}%22",
        f"https://www.reddit.com/user/{target}",
        f"https://checkusernames.com/"  # Outil pour vérifier la dispo
    ]
    open_urls(urls)

def search_email(target):
    """ Cherche si l'email a fuité. """
    print(f"\n[+] Recherche de fuites pour '{target}'...")
    urls = [
        f"https://haveibeenpwned.com/account/{target}",
        f"https://www.google.com/search?q=%22{target}%22",
        f"https://www.google.com/search?q=site:pastebin.com+%22{target}%22"
    ]
    open_urls(urls)

def search_domain(target):
    """ Scan passif d'un domaine. """
    print(f"\n[+] Scan passif du domaine '{target}'...")
    urls = [
        f"https://www.google.com/search?q=site:{target}+ext:pdf",
        f"https://www.virustotal.com/gui/domain/{target}",
        f"https://web.archive.org/web/*/{target}"
    ]
    open_urls(urls)

def secret_search():
    """
    LE MENU CACHÉ (Option 5)
    Recherche avancée sur une personne physique ou un téléphone.
    """
    print("\n" + "*"*40)
    print("   [ACCÈS AUTORISÉ] : MODE INVESTIGATION PERSONNELLE")
    print("*"*40)
    print("Remplissez les champs connus (ou appuyez sur Entrée pour ignorer)")

    prenom = input("Prénom : ").strip()
    nom = input("Nom : ").strip()
    tel = input("Téléphone (ex: 3361234...) : ").strip()

    urls = []

    # 1. Recherche par NOM + PRENOM
    if prenom and nom:
        # Webmii est excellent pour trouver des gens
        urls.append(f"https://webmii.com/people?n={prenom}%20{nom}")
        # Recherche Google ciblée sur les réseaux sociaux pro
        urls.append(f"https://www.google.com/search?q=site:linkedin.com+%22{prenom}+{nom}%22")
        # Recherche de CV ou documents PDF
        urls.append(f"https://www.google.com/search?q=%22{prenom}+{nom}%22+ext:pdf+OR+filetype:doc")
        # Pages Blanches (France)
        urls.append(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={nom}+{prenom}")

    # 2. Recherche par TÉLÉPHONE
    if tel:
        # Nettoyage du numéro (enlève les espaces et tirets)
        clean_tel = tel.replace(" ", "").replace("-", "").replace(".", "")

        # Recherche Google simple du numéro
        urls.append(f"https://www.google.com/search?q=%22{clean_tel}%22")
        # Technique Hacker : Ouvre une conversation WhatsApp sans ajouter le contact
        # Permet de voir la photo de profil et l'heure de connexion ("Vu à...")
        urls.append(f"https://api.whatsapp.com/send?phone={clean_tel}")
        # Recherche inversée (utile si c'est un fixe ou une arnaque)
        urls.append(f"https://www.tellows.fr/num/{clean_tel}")

    if not urls:
        print("[-] Vous n'avez rien saisi. Retour au menu.")
        return

    open_urls(urls)

def open_urls(url_list):
    print(f"--> Je vais ouvrir {len(url_list)} onglets.")
    choix = input("Lancer ? (o/n) : ")
    if choix.lower() == 'o':
        for url in url_list:
            webbrowser.open(url)
            time.sleep(0.5)
        print("[*] Terminé.")
    else:
        print("[-] Annulé.")

def main():
    while True:
        banner()
        print("1. Rechercher un Pseudo")
        print("2. Rechercher un Email")
        print("3. Analyser un Domaine")
        print("4. Quitter")
        # L'option 5 n'est PAS affichée ici (c'est le secret)

        choice = input("\nChoisissez une option : ")

        if choice == '1':
            target = input("Pseudo : ")
            search_username(target)
        elif choice == '2':
            target = input("Email : ")
            search_email(target)
        elif choice == '3':
            target = input("Domaine : ")
            search_domain(target)
        elif choice == '4':
            print("Bye !")
            sys.exit()
        elif choice == '5':
            # C'est ici que la magie opère
            secret_search()
        else:
            print("Option invalide.")

        input("\nEntrée pour continuer...")

if __name__ == "__main__":
    main()