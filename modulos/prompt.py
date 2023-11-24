import json

class BrandPromptCreator:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def read_data(self):
        """Lê e retorna os dados do arquivo JSON, com tratamento de erros."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except IOError as e:
            print(f"Não foi possível ler o arquivo: {e}")
            return None
        except json.JSONDecodeError:
            print("Erro de formatação no arquivo JSON.")
            return None

    def validate_data(self, data):
        """Valida se os dados necessários estão presentes."""
        return data and "brand-name" in data and "brand-description" in data

    def create_prompt(self, data):
        """Cria um prompt com base nos dados de 'brand-name' e 'brand-description'."""
        brand_name = data["brand-name"]
        brand_description = data["brand-description"]

        return (f"Crie uma marca preto e branco sólida para a empresa '{brand_name}'. somente a marca, nenhum elemento a mais, além disso, sempre devemos pensar as marcas como pictogramas"
                f"Gostaria que a marca fosse '{brand_description}'. "
                "A marca precisa ser sólida, preto e branco")

    def update_json(self, new_data):
        """Atualiza o arquivo JSON com novos dados sem apagar os existentes."""
        try:
            with open(self.filename, "r+", encoding="utf-8") as file:
                existing_data = json.load(file)
                existing_data.update(new_data)
                file.seek(0)
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Não foi possível atualizar o arquivo: {e}")

    def run(self):
        """Executa o processo principal de criação do prompt."""
        data = self.read_data()
        if data and self.validate_data(data):
            prompt = self.create_prompt(data)
            self.update_json({"prompt": prompt})
            print("Prompt criado e salvo com sucesso.")
        else:
            print("Dados necessários não estão disponíveis ou são inválidos.")

# Uso da classe
if __name__ == "__main__":
    prompt_creator = BrandPromptCreator()
    prompt_creator.run()
