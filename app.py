import requests
import sys

def get_joke():
    """
    Interroge JokesAPI pour une blague de programmation en français et l'affiche.
    """
    # URL de l'API ciblée (Blagues de programmation, en français, safe)
    url = "https://v2.jokeapi.dev/joke/Any?lang=fr"
    
    print("Recherche d'une blague en cours...")
    
    try:
        # Effectuer la requête GET
        response = requests.get(url)
        
        # Vérifier si la requête a réussi (code de statut 200)
        response.raise_for_status()
        
        # Convertir la réponse JSON en dictionnaire Python
        data = response.json()
        
        # Vérifier si l'API a retourné une erreur (ex: pas de blague trouvée)
        if data['error']:
            print("Désolé, l'API n'a pas pu trouver de blague pour le moment.")
            return

        print("\n" + "="*30)
        
        # Afficher la blague en fonction de son type
        if data['type'] == 'single':
            # Blague en une seule partie
            print("Blague (1 partie) :")
            print(data['joke'])
        elif data['type'] == 'twopart':
            # Blague en deux parties (question/réponse)
            print("Blague (2 parties) :")
            print(f"Q: {data['setup']}")
            print(f"R: {data['delivery']}")
            
        print("="*30 + "\n")

    except requests.exceptions.HTTPError as errh:
        print(f"Erreur HTTP : {errh}", file=sys.stderr)
    except requests.exceptions.ConnectionError as errc:
        print(f"Erreur de connexion : {errc}", file=sys.stderr)
    except requests.exceptions.Timeout as errt:
        print(f"Erreur de Timeout : {errt}", file=sys.stderr)
    except requests.exceptions.RequestException as err:
        print(f"Oups: Quelque chose s'est mal passé : {err}", file=sys.stderr)
    except KeyError:
        # Gérer le cas où la structure JSON attendue est différente
        print("Erreur : La réponse de l'API n'a pas le format attendu.", file=sys.stderr)

if __name__ == "__main__":
    get_joke()
