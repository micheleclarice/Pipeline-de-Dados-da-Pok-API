# 🚀 Projeto de Pipeline de Dados Pokémon

## 📄 Descrição

Este é um projeto de pipeline de dados (ETL) desenvolvido como parte dos meus estudos em Engenharia de Dados. O script Python busca dados da [PokéAPI](https://pokeapi.co/) (uma API pública e gratuita), realiza um processo de transformação e limpeza, e salva os dados estruturados em um arquivo CSV pronto para análise.

### Funcionalidades
* **Extração (E):** Conecta-se à PokéAPI e extrai dados de múltiplos Pokémons.
* **Transformação (T):** Limpa e estrutura os dados brutos (JSON), selecionando campos de interesse, renomeando colunas e realizando conversões de unidades (ex: altura e peso).
* **Carregamento (L):** Salva os dados transformados em um arquivo `.csv` local.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:** Para manipulação e estruturação dos dados em DataFrames.
* **Requests:** Para realizar as chamadas HTTP e consumir a API.

---

## ⚙️ Como Rodar o Projeto

Você pode rodar este script localmente seguindo os passos abaixo:

**1. Clone o repositório:**
```bash
git clone [COLE AQUI A URL DO SEU REPOSITÓRIO]
cd [NOME-DA-PASTA-DO-PROJETO]
```

**2. (Opcional) Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # No Windows:
