# PolRoute - Distributed Database Analysis

### Trabalho de Implementação - Banco de Dados Distribuídos

## 📋 Descrição

Este repositório contém a implementação do trabalho da disciplina **Banco de Dados Distribuídos**, orientado pelo professor **Daniel Cardoso Moraes de Oliveira**.

O trabalho consiste na modelagem, consulta e análise de desempenho utilizando o **dataset PolRoute-DS** (https://doi.org/10.5753/jidm.2022.2355), que contém dados de criminalidade do Estado de São Paulo. A cidade é representada como um **grafo de vias segmentadas**, onde cada rua é particionada em segmentos de 100 a 200 metros, com vértices interligando os segmentos.

A implementação envolve a criação de um **schema** no middleware ou framework escolhido, com suporte a **processamento paralelo de consultas**, visando otimizar a execução sobre grandes volumes de dados.

---

## 📊 Dataset - PolRoute-DS

O dataset está disponível em: [https://osf.io/mxrgu/](https://osf.io/mxrgu/)

🗂️ Arquivos disponíveis:

- **crime.csv** (~263 MB): Total de crimes por tipo, por segmento e período.
- **segment.csv** (~46 MB): Informações sobre os segmentos de vias.
- **vertice.csv** (~4 MB): Detalhes sobre os vértices, incluindo distrito e vizinhança.
- **district.csv** (~5 MB): Dados sobre os distritos da cidade.
- **neighborhood.csv** (~2 MB): Informações sobre as vizinhanças.
- **time.csv** (~850 KB): Períodos de tempo utilizados na análise criminal.

---

## Objetivos

- Criar o schema do **PolRoute-DS** no middleware ou framework de processamento paralelo escolhido, como:
  - [Apache Hive](https://hive.apache.org/)
  - [Oracle Express](https://www.oracle.com/database/technologies/appdev/xe.html)
  - Ou outro de escolha do grupo.

- Desenvolver consultas para responder às seguintes questões:

1. Total de crimes por tipo e por segmento das ruas do distrito de **IGUATEMI** em **2016**.
2. Total de crimes por tipo e por segmento das ruas do distrito de **IGUATEMI** entre **2006 e 2016**.
3. Total de ocorrências de **Roubo de Celular** e **Roubo de Carro** no bairro de **SANTA EFIGÊNIA** em **2015**.
4. Total de crimes por tipo em **vias de mão única** durante **2012**.
5. Total de **Roubos de Carro** e **Celular** em todos os segmentos durante **2017**.
6. IDs dos segmentos com o **maior índice criminal** (soma total de crimes) em **novembro de 2010**.
7. IDs dos segmentos com o **maior índice criminal** durante os **finais de semana de 2018**.

- **Analisar o desempenho** das consultas de forma sequencial e paralela (em ambiente multicore ou distribuído).

---

## Estrutura do Repositório

- `/schema` — Scripts para criação do schema e tabelas.
- `/queries` — Consultas SQL desenvolvidas.
- `/analysis` — Relatório de análise de desempenho.
- `/data` — Arquivos CSV do dataset (opcional, conforme o tamanho e uso do Git LFS).

---

## Tecnologias e Ferramentas

- Middleware/framework de processamento paralelo (ex.: Apache Hive, Oracle).
- SQL ou linguagem específica do framework escolhido.
- Google Colab (opcional, para casos de limitações de hardware local).
- Git e GitHub para versionamento e colaboração.

---

## Como executar

1. [FAZER...]

---

## ⚠️ Observações importantes

Devido ao tamanho dos arquivos CSV, principalmente o `crime.csv` (262,9 MB), é necessário utilizar o Git Large File Storage (LFS) para gerenciar adequadamente estes arquivos. Para instalar e utilizar o Git LFS:

1. Instale o Git LFS seguindo as instruções em: [https://docs.github.com/pt/repositories/working-with-files/managing-large-files](https://docs.github.com/pt/repositories/working-with-files/managing-large-files)
2. Execute `git lfs install` no seu repositório
3. Configure os arquivos que devem ser rastreados pelo LFS usando `git lfs track "*.csv"`
4. Commit o arquivo `.gitattributes`

---

## Autores

- João Victor Lagos de Aguiar
- [Nome do Integrante 2]
- [Nome do Integrante 3]

---

