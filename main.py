# Importation des modules nécessaires
from scrap.twitter_request import make_twitter_request
from scrap.data_processing import process_twitter_response
from scrap.config import hashtag
import os

from fastapi import FastAPI, File, UploadFile, HTTPException
from fast_api.fast_api import process_uploaded_file  # Assurez-vous que le chemin d'importation est correct

# Faire une requête à l'API Twitter
# response_request = make_twitter_request()

# # Vérifier si la requête a réussi
# if response_request.status_code == 200:
#     # Traitement de la réponse JSON
#     response_json = response_request.json()
#     df = process_twitter_response(response_json)

#     # Sauvegarder les données dans un fichier CSV
#     csv_filename = f'twitter_data_{hashtag}.csv'
#     df.to_csv(csv_filename, index=False)

#     print(f"Data successfully saved to '{csv_filename}'")
# else:
#     print(f"Error: {response_request.status_code}")
#     print(response_request.text)

# Initialisation de l'application FastAPI
app = FastAPI()

# Définition de l'endpoint pour le téléchargement de fichiers
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), perform_cleaning: bool = False):
    try:
        # Appel de la fonction de traitement du fichier téléchargé
        return process_uploaded_file(file, perform_cleaning)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# Exécution de l'application FastAPI
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
