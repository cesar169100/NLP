from dotenv import load_dotenv
import os

load_dotenv()
class Settings:
    def __init__(self):
        self.AWS_ACCCESS_KEY = os.getenv("AWS_ACCCESS_KEY")
        self.AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
        self.EC2_PUBLIC_DNS = os.getenv("EC2_PUBLIC_DNS")

def get_settings():
    settings = Settings()
    return settings
    
    