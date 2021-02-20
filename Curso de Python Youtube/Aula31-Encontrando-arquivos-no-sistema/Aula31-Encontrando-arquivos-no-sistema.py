import os


def converte_tamanho(tamanho_bytes):
    base = 1000
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    tamanho_convertido = tamanho_bytes
    prefixo = 'B'
    if tamanho_bytes >= tera:
        tamanho_convertido = tamanho_bytes / tera
        prefixo = 'TB'
    elif tamanho_bytes >= giga:
        tamanho_convertido = tamanho_bytes / giga
        prefixo = 'GB'
    elif tamanho_bytes >= mega:
        tamanho_convertido = tamanho_bytes / mega
        prefixo = 'MB'
    elif tamanho_bytes >= kilo:
        tamanho_convertido = tamanho_bytes / kilo
        prefixo = 'KB'

    return f'{tamanho_convertido} {prefixo}'.replace('.', ',')


caminho_procura = r'C:\Users\Rafae\Downloads'
termo_procura = input('Termo buscado: ').strip().lower()

numero_arquivo = 1
for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        try:
            if termo_procura.lower() in arquivo.lower():
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print()
                print('='*50)
                print()
                print(f'Arquivo número: {numero_arquivo}')
                print(f'Caminho do arquivo: {caminho_completo}')
                print(f'Nome do arquivo: {nome_arquivo}')
                print(f'Extensão do arquivo: {extensao_arquivo}')

                print('Tamanho do arquivo:', converte_tamanho(tamanho_arquivo))
                numero_arquivo += 1
        except PermissionError as erro:
            print('Erro de permissão.')
        except Exception as erro:
            print('Erro desconhecido: ', erro)
