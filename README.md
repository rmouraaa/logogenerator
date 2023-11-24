Gerador de Imagens de Marca
Descrição
Este projeto é um gerador automatizado de imagens para marcas, que coleta dados da marca, cria um prompt baseado nessas informações, gera uma imagem utilizando a API DALL-E 3, e em seguida vetoriza a imagem para formatos mais amigáveis para uso em branding e marketing.

Funcionalidades
Coleta de dados da marca.
Criação de prompt automático.
Geração de imagem da marca com DALL-E 3.
Vetorização da imagem gerada.
Dependências
Python 3.x
openai (para a API DALL-E 3)
PIL (Python Imaging Library)
Outras bibliotecas Python (json, requests, subprocess, os)
Instalação
Para instalar as dependências necessárias, execute:

bash
Copy code
pip install openai pillow requests
Configuração
Antes de executar o projeto, é necessário configurar a chave de API para o DALL-E 3 no arquivo config.py.

Uso
Para executar o programa, use:

bash
Copy code
python app.py
Siga as instruções no terminal para inserir os detalhes da sua marca. O programa irá automaticamente gerar e vetorizar uma imagem baseada nas informações fornecidas.

Estrutura do Projeto
app.py: Script principal para executar o programa.
ui.py: Módulo para coletar dados da marca.
prompt.py: Módulo para criar o prompt para a geração da imagem.
generator.py: Módulo para gerar a imagem usando a API DALL-E 3.
vector.py: Módulo para vetorizar a imagem gerada.
Exemplos
Após executar o script app.py e seguir as instruções, uma imagem da marca será gerada e salva no diretório especificado, além de ser convertida para o formato SVG.

Licença
[Opensource]

Contato
[contato@rodrigofernandes.com]
