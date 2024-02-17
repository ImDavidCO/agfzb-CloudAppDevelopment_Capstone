import requests
import json
from requests.auth import HTTPBasicAuth
from .models import CarDealer
from .models import DealerReview



# Supongamos que tienes una clase DealerView en otro archivo models.py
# from .models import DealerView

# URL base de tu servicio de concesionarios en la nube
BASE_URL = "https://4aa020d5-64a6-431a-abb5-7d1af88582bc-bluemix.cloudantnosqldb.appdomain.cloud"

# Método para realizar solicitudes HTTP GET
def get_request(url, **kwargs):
    try:
        response = requests.get(url, params=kwargs, headers={'Content-Type': 'application/json'},
                                auth=HTTPBasicAuth('apikey', 'api_key'))
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        return response.json()  # Devuelve el resultado JSON de la respuesta
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud HTTP: {err}")
        return None

# Método para realizar solicitudes HTTP POST
def post_request(url, **kwargs):
    try:
        response = requests.post(url, params=kwargs, json=payload, headers={'Content-Type': 'application/json'},
                                 auth=HTTPBasicAuth('apikey', 'api_key'))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud HTTP: {err}")
        return None

# Método para obtener concesionarios desde un servicio en la nube

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            print("DEaler",dealer_doc)
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

# Método para obtener revisiones de concesionarios por ID desde un servicio en la nube
def get_dealer_reviews_from_cf(url, dealer_id):
    try:
        # Call get_request() with the specified arguments
        json_result = get_request(url, dealerId=dealer_id)
        results = []

        if json_result:
            # Parse the JSON results into a list of DealerReview objects
            reviews = json_result
            for review in reviews:
                review_obj = DealerReview(
                    dealership=review.get("dealership"),
                    name=review.get("name"),
                    purchase=review.get("purchase"),
                    review=review.get("review"),
                    purchase_date=review.get("purchase_date"),
                    car_make=review.get("car_make"),
                    car_model=review.get("car_model"),
                    car_year=review.get("car_year"),
                    sentiment=review.get("sentiment"),
                    id=review.get("id")
                )
                results.append(review_obj)

        return results
    except Exception as e:
        print(f"Error getting dealer reviews: {e}")
        return None


# Método para analizar sentimientos de revisiones utilizando Watson NLU
def analyze_review_sentiments(text):
    try:
        # Llama a get_request() con los argumentos especificados
        # Realiza el análisis de sentimientos y devuelve el resultado
        # ...

        return sentiment_label
    except Exception as e:
        print(f"Error al analizar sentimientos de la revisión: {e}")
        return None
