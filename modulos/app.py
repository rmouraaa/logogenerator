from ui import BrandDataCollector
from prompt import BrandPromptCreator
from generator import ImageGenerator
from vector import ImageVectorizer

def main():
    # Coletar dados da marca
    collector = BrandDataCollector()
    collector.collect_data()

    # Criar o prompt
    prompt_creator = BrandPromptCreator()
    prompt_creator.run()

    # Gerar a imagem
    generator = ImageGenerator()
    generator.run()

    # Vetorizar a imagem
    vectorizer = ImageVectorizer()
    vectorizer.run()

    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
