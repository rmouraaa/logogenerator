import os
import subprocess
from PIL import Image

class ImageVectorizer:
    def __init__(self, input_folder="static/logo-generator", output_folder="static/vector", filename="generated_image.png"):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.filename = filename

    def convert_to_bmp(self):
        """Converte a imagem para o formato BMP e retorna o caminho do arquivo BMP."""
        input_path = os.path.join(self.input_folder, self.filename)
        bmp_filename = os.path.splitext(self.filename)[0] + ".bmp"
        bmp_path = os.path.join(self.input_folder, bmp_filename)

        if not os.path.exists(input_path):
            print(f"Arquivo de imagem não encontrado: {input_path}")
            return None

        try:
            with Image.open(input_path) as img:
                img.save(bmp_path)
            return bmp_path
        except IOError as e:
            print(f"Erro ao converter a imagem: {e}")
            return None

    def vectorize_image(self, bmp_path):
        """Vetoriza a imagem BMP e salva como SVG."""
        output_path = os.path.join(self.output_folder, os.path.splitext(self.filename)[0] + ".svg")

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        command = f"potrace {bmp_path} -s -o {output_path}"

        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Imagem vetorizada salva em: {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"Erro ao vetorizar a imagem: {e}")
            return None

    def remove_temp_file(self, file_path):
        """Remove um arquivo temporário."""
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

    def run(self):
        """Executa o processo de vetorização da imagem."""
        bmp_path = self.convert_to_bmp()
        if bmp_path:
            svg_path = self.vectorize_image(bmp_path)
            self.remove_temp_file(bmp_path)  # Remove o arquivo BMP temporário
            return svg_path

# Uso da classe
if __name__ == "__main__":
    vectorizer = ImageVectorizer()
    svg_path = vectorizer.run()
    if svg_path:
        print(f"Vetorização concluída. Arquivo SVG: {svg_path}")
    else:
        print("Falha na vetorização da imagem.")
