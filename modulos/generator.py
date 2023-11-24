import json
import openai
import requests
from config import api_key  # Importar a chave de API do arquivo config.py
import os
from urllib.parse import urlparse

class ImageGenerator:
    def __init__(self, filename="data.json", folder="static/logo-generator"):
        self.filename = filename
        self.folder = folder
        openai.api_key = api_key

    def read_prompt_from_json(self):
        """Lê e retorna o prompt do arquivo JSON."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("prompt", "")
        except IOError as e:
            print(f"Não foi possível ler o arquivo: {e}")
            return ""
        except json.JSONDecodeError:
            print("Erro de formatação no arquivo JSON.")
            return ""

    def generate_image(self, prompt_text):
        """Gera a imagem usando a API do DALL·E 3."""
        try:
            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt_text,
                size="1024x1024",
                n=1,
            )
            return response['data'][0]['url']
        except Exception as e:
            print(f"Erro ao solicitar a geração da imagem: {e}")
            return None

    def is_valid_url(self, url):
        """Verifica se a URL é válida."""
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def download_image(self, url, filename="generated_image.png"):
        """Baixa a imagem da URL fornecida e salva no diretório especificado."""
        if not self.is_valid_url(url):
            print("URL inválida.")
            return None

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(self.folder, filename)
            with open(path, 'wb') as file:
                file.write(response.content)
            return path
        else:
            print("Não foi possível baixar a imagem.")
            return None

    def run(self):
        """Executa o processo principal de geração e download da imagem."""
        prompt_text = self.read_prompt_from_json()
        if prompt_text:
            image_url = self.generate_image(prompt_text)
            if image_url:
                saved_image_path = self.download_image(image_url)
                if saved_image_path:
                    print(f"A imagem foi salva em: {saved_image_path}")
                else:
                    print("Não foi possível baixar a imagem.")
        else:
            print("Prompt não encontrado no arquivo JSON.")

# Uso da classe
if __name__ == "__main__":
    generator = ImageGenerator()
    generator.run()
