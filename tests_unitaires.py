import zipfile
import pandas as pd
import requests
import pytest
 
zip_file_path2 = 'application_train.zip'  
df2 = 'application_train.csv'  

# Créez un objet ZipFile pour ouvrir le fichier ZIP en mode lecture
with zipfile.ZipFile(zip_file_path2, 'r') as zipf:
    with zipf.open(df2) as file_in_zip:
        data_train = pd.read_csv(file_in_zip) 

# TEST CONNEXION API
# URL de l'API
api_url = "http://127.0.0.1:5000/credit/"

# ID client de test
client_id = 100028



def test_dataframe_shape():
    app_train_df = data_train
    assert app_train_df.shape == (149998, 122)

def test_dataframe_type():
    app_train_df = data_train
    assert isinstance(app_train_df, pd.DataFrame), "app_train_df n'est pas un DataFrame."

if __name__ == "__main__":
    pytest.main([__file__])


