# desafioDIO-textract
Neste desafio foi pedido para gerar um código em python que imprima o texto extraído de uma imagem com o uso AWS Textract 

Optei em usar o AWS CloudShell ao invés do AWS CLI para a execução do desafio, pois desta forma é possível testar sem instalar nada na minha máquina. 

Documentação:
- [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/)
- [Amazon Textract](https://docs.aws.amazon.com/pt_br/textract/)

Primeiramente, acessamos a nossa conta e abrimos o Amazon Textract para verificar se ele esta conseguindo extrair as informações da imagem corretamente. Testei algumas imagens e a extração não foi a ideal com extração incompleta por dificuldade de reconhecer as palavras ou por frases completas estarem em diferentes linhas o que não deixa muito amigável. Então, decidi usar uma lista de material escolar parecida com o do professor para fazer a extração dos dados com o python.

No Amazon Textract o melhor formato foi texto simples que conseguiu extrair as linhas corretamente. Veja o print abaixo:

[Acessando o terminal na AWS](assets/AcessandoCloudShell.png)



Para acessar a AWS Cloud Shell você loga na sua conta aws e clica no ícone na barra superior direita
 
