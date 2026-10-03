import json
import boto3
from botocore.exceptions import ClientError

# Essa função verifica se existe uma imagem detectada e se não existe cria o cliente para extraí-la pelo textract
def detect_file_text() -> None:
    client = boto3.client("textract")
    try:
        with open("lista-escolar.jpg", "rb") as le:
            document_bytes = le.read()

        response = client.detect_document_text(Document={"Bytes": document_bytes})

        with open("response.json", "w") as response_file:
            response_file.write(json.dumps(response))

    except ClientError as e:
        print(f"Erro processando documento: {e}")


def get_lines() -> list[str]:
     """
    O que o get_lines faz:
    - Tenta abrir o arquivo response.json (que contém a resposta do Textract).
    - Se conseguir abrir:
        * Lê o JSON.
        * Pega os blocos (Blocks).
        * Filtra apenas os blocos do tipo "LINE".
        * Retorna uma lista com o texto de cada linha.
    - Se não conseguir abrir (porque o arquivo não existe ainda):
        * Chama detect_file_text() para gerar o response.json.
        * Depois chama get_lines() de novo, garantindo que já exista o arquivo e que você obtenha os dados na mesma execução.
    """
    try:
        with open("response.json", "r") as f:
            data = json.loads(f.read())
            blocks = data["Blocks"]
        return [block["Text"] for block in blocks if block["BlockType"] == "LINE"]
    except IOError:
        detect_file_text()
        return get_lines()  # chama de novo para ler após gerar


# Faz o chamamento do código e imprime o texto da lista
if __name__ == "__main__":
    for line in get_lines():
        print(line)
