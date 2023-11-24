import json

class BrandDataCollector:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def get_input(self, prompt):
        """Solicita entrada do usuário até que um valor válido seja fornecido."""
        while True:
            response = input(prompt).strip()
            if response:
                return response
            print("Este campo é obrigatório. Por favor, forneça uma resposta.")

    def choose_category(self):
        """Permite que o usuário escolha uma categoria de uma lista predefinida."""
        categories = [
            "Tecnologia", "Alimentação", "Entretenimento", "Publisher", 
            "Eventos", "Esportes", "Empresarial", "Automobilístico", "Economia Circular"
        ]
        print("Escolha a categoria do seu negócio:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        while True:
            choice = input("Digite o número da categoria: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("Escolha inválida. Por favor, selecione um número da lista.")

    def save_to_json(self, data):
        """Salva os dados em um arquivo JSON com tratamento de erros."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"As informações foram salvas com sucesso no arquivo '{self.filename}'.")
        except IOError as e:
            print(f"Não foi possível salvar o arquivo: {e}")

    def collect_data(self):
        """Coleta dados da marca do usuário."""
        brand_data = {
            "brand-name": self.get_input("Qual o nome da sua empresa? "),
            "brand-description": self.get_input("Descreva a sua marca: "),
            "brand-signature": self.get_input("Você tem slogan? "),
            "brand-category": self.choose_category()  
        }
        self.save_to_json(brand_data)

    def read_data(self):
        """Lê e retorna os dados do arquivo JSON."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except IOError as e:
            print(f"Não foi possível ler o arquivo: {e}")
            return None

# Uso da classe
if __name__ == "__main__":
    collector = BrandDataCollector()
    collector.collect_data()
