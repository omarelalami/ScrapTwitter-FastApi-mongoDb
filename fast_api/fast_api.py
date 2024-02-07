# Importer les bibliothèques nécessaires
import pandas as pd  # Manipulation de données
from io import StringIO  # Gestion du texte comme fichiers
from fast_api.data_handling import perform_data_cleaning  # Nettoyage de données
from fast_api.sentiment_handling import perform_sentiment_analysis  # Analyse des sentiments
from fast_api.database_handling import save_to_mongodb  # Enregistrement dans MongoDB

# Définir une fonction pour le traitement des fichiers
def process_uploaded_file(file, perform_cleaning=False):  # Fonction pour le traitement des CSV

  # Essayer de lire le fichier CSV, gérer les erreurs
  try:
    
    df = pd.read_csv(file.file)  # Lire le CSV dans un DataFrame
    
    results = []  # Initialiser la liste des résultats


    # Traiter chaque ligne
    for index, row in df.iterrows():
      line_content = row['snippet']  # Obtenir la représentation sous forme de chaîne de la ligne

      # Nettoyer les données si spécifié
      cleaned_line = perform_data_cleaning(line_content) if perform_cleaning else line_content
      
      # Effectuer une analyse des sentiments
      sentiment_result = perform_sentiment_analysis(cleaned_line)
      print(""*30)
      print(cleaned_line)
      print(""*30)
      # Enregistrer les résultats dans la base de données
      save_to_mongodb(file.filename, cleaned_line, sentiment_result)

      # Ajouter les résultats à la liste
      results.append({"line_content": cleaned_line, "Toxicity level": sentiment_result})

    # Retourner une réponse réussie avec les résultats
    return {"status": "success", "filename": file.filename, "results": results}

  # Gérer les erreurs spécifiques
  except (ValueError, FileNotFoundError) as e:
    raise ValueError("Format de fichier invalide ou fichier introuvable")

  # Gérer les erreurs générales
  except Exception as e:
    raise ValueError("Erreur interne du serveur")
