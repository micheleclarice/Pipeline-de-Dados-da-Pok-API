import requests
import pandas as pd
import time

# --- Constantes do Projeto ---
# É uma boa prática definir valores fixos no início do script.
BASE_URL = "https://pokeapi.co/api/v2/pokemon"
NUM_POKEMONS = 151  # Vamos capturar os 151 Pokémons originais
OUTPUT_FILE = "pokemon_dataset.csv"


def fetch_pokemon_data(pokemon_id):
    """
    Passo de Extração (E): Busca dados de um Pokémon específico na API.
    """
    url = f"{BASE_URL}/{pokemon_id}"
    
    try:
        response = requests.get(url)
        # Verifica se a requisição falhou (ex: 404 Pokémon não encontrado)
        response.raise_for_status() 
        print(f"Sucesso: Dados extraídos para o Pokémon ID {pokemon_id}")
        return response.json()
    except requests.exceptions.RequestException as e:
        # Informa se um Pokémon específico falhar
        print(f"Erro ao buscar Pokémon ID {pokemon_id}: {e}")
        return None


def transform_pokemon_data(data):
    """
    Passo de Transformação (T): Limpa e estrutura os dados brutos (JSON).
    """
    if data is None:
        return None

    # Extraindo tipos de forma segura (alguns Pokémons têm 1 tipo, outros 2)
    types = data['types']
    primary_type = types[0]['type']['name'] if len(types) > 0 else None
    secondary_type = types[1]['type']['name'] if len(types) > 1 else None

    # Montando um dicionário limpo
    # Isso é muito mais limpo do que usar o JSON gigante da API.
    transformed = {
        'id': data['id'],
        'name': data['name'].capitalize(),
        'height_m': data['height'] / 10.0,  # Convertendo decímetros para metros
        'weight_kg': data['weight'] / 10.0, # Convertendo hectogramas para quilogramas
        'primary_type': primary_type,
        'secondary_type': secondary_type,
        'hp': data['stats'][0]['base_stat'],
        'attack': data['stats'][1]['base_stat'],
        'defense': data['stats'][2]['base_stat'],
        'special_attack': data['stats'][3]['base_stat'],
        'special_defense': data['stats'][4]['base_stat'],
        'speed': data['stats'][5]['base_stat'],
    }
    
    return transformed


def save_to_csv(data_list, filename):
    """
    Passo de Carregamento (L): Salva os dados transformados em um arquivo CSV.
    """
    if not data_list:
        print("Nenhum dado para salvar.")
        return

    # Converte a lista de dicionários em um DataFrame do Pandas
    df = pd.DataFrame(data_list)
    
    # Salva o DataFrame em um arquivo CSV, sem o índice padrão do pandas
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"\nSucesso! Pipeline concluído.")
    print(f"Dados salvos em '{filename}' com {len(df)} registros.")


def main():
    """
    Função principal que orquestra todo o processo de ETL.
    """
    print("--- Iniciando Pipeline de ETL Pokémon ---")
    
    all_pokemon_data = []
    
    # Loop para Extrair e Transformar dados de todos os Pokémons
    for i in range(1, NUM_POKEMONS + 1):
        raw_data = fetch_pokemon_data(i)
        transformed_data = transform_pokemon_data(raw_data)
        
        if transformed_data:
            all_pokemon_data.append(transformed_data)
        
        # Pequena pausa para não sobrecarregar a API
        time.sleep(0.1) 

    # Carrega (Salva) os dados
    save_to_csv(all_pokemon_data, OUTPUT_FILE)
    print("--- Pipeline Finalizado ---")


# Esta linha padrão do Python garante que a função main()
# só seja executada quando você rodar o script diretamente.
if __name__ == "__main__":
    main()
