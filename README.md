# Fatec LP2 Crawler

Crawler de extração de dados para fins acadêmicos.  
Este projeto foi desenvolvido para a disciplina de Linguagens de Programação 2 (LP2), na Fatec Rio Claro.

Este é um raspador de dados (web scraper) minimalista construído em Python, focado na extração de informações empresariais (CNPJs) de sites de consulta pública. O objetivo principal deste repositório é demonstrar o uso de requisições HTTP e Expressões Regulares (Regex) para manipulação de dados em larga escala.

## Funcionalidades

- Extração via Regex: Busca automática de padrões de CNPJ formatados (`XX.XXX.XXX/XXXX-XX`).
- Simulação de Navegador: Utiliza headers de `User-Agent` para contornar bloqueios simples de bots.
- Persistência Local: Salva o conteúdo HTML bruto baixado para auditoria ou processamento offline.
- Containerização: Totalmente configurado para rodar via Docker, garantindo um ambiente isolado e livre de conflitos de dependências.

## Tecnologias Utilizadas

- [Python](https://www.python.org/): Linguagem principal do projeto.
- [Requests](https://requests.readthedocs.io/): Para realizar chamadas HTTP.
- [Docker](https://www.docker.com/): Para padronização e execução do ambiente.
- RegEx (Expressões Regulares): Para filtragem e coleta precisa de dados.

## Como Executar

Você pode rodar este projeto de duas formas:

### 1. Utilizando Docker (Recomendado)

Certifique-se de ter o Docker e o Docker Compose instalados. Na raiz do projeto, execute:

```bash
docker-compose up --build
```
O script será executado dentro do container e os resultados (incluindo o arquivo `empresas.html`) aparecerão na sua pasta local graças aos volumes mapeados.

### 2. Manualmente (Instalação Local)

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Execute o script:
```bash
python app.py
```

## Estrutura do Projeto

- `app.py`: O coração do crawler. Realiza a requisição, salva o HTML e extrai os dados.
- `empresas.html`: Arquivo gerado após a execução com o conteúdo da página acessada.
- `Dockerfile` & `docker-compose.yaml`: Configurações de infraestrutura como código.
- `requirements.txt`: Lista de dependências Python.
- `web-scraping.pdf`: Material de apoio e documentação teórica.

## Contexto Acadêmico

Este projeto faz parte do currículo da Fatec de Rio Claro, servindo como laboratório prático para entender como a Web funciona nos bastidores e como automatizar tarefas repetitivas de coleta de dados.

## Autor

Desenvolvido por Tarsis Lima.  
Fatec Rio Claro  
[GitHub Profile](https://github.com/tarsislimadev)

## Licença

Este projeto está sob a licença [MIT](./LICENSE).
