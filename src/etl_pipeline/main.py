from prefect import flow, task, get_client
from ETLPipeline import etl_flow
from config import get_settings

settings = get_settings()

def main(numero):
    etl = etl_flow(numero)
    return etl

if __name__=="__main__":
    # api_key = settings.PREFECT_APPI_KEY
    # api_url = settings.PREFECT_APPI_URL
    
    # # Configura el cliente de Prefect Cloud
    # client = get_client(api_key=api_key, api_url=api_url)
    print(main(5))