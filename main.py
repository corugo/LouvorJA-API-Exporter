import sqlite3
import json
import os
import re

# CONFIGURAÇÕES
ip = "192.168.56.1"
port = "5136"
token = "z55ob"


def conectar_banco(caminho_db):
    try:
        return sqlite3.connect(caminho_db)
    except sqlite3.Error as e:
        print(f"Erro ao conectar: {e}")
        return None


def obter_musicas(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, album, url_instrumental FROM MUSICAS")
        resultados = cursor.fetchall()

        musicas = []
        for linha in resultados:
            musicas.append({
                "id": linha[0],
                "nome": linha[1],
                "album": linha[2],
                "url_instrumental": linha[3]
            })

        return musicas

    except sqlite3.Error as e:
        print(f"Erro ao buscar músicas: {e}")
        return []


def limpar_nome(nome):
    """Remove caracteres inválidos para nomes de arquivos/pastas"""
    return re.sub(r'[\\/*?:"<>|]', "", nome)


def criar_vbs(caminho, url):
    conteudo = f'''Set objHTTP = CreateObject("MSXML2.XMLHTTP")
objHTTP.Open "GET", "{url}", False
objHTTP.Send
'''
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)


def main():
    caminho_db = "database.db"

    conn = conectar_banco(caminho_db)
    if conn is None:
        return

    musicas = obter_musicas(conn)

    # salvar JSON (mantido)
    with open("musicas.json", "w", encoding="utf-8") as f:
        json.dump(musicas, f, ensure_ascii=False, indent=4)

    for m in musicas:
        album = limpar_nome(m["album"])
        nome = limpar_nome(m["nome"])

        pasta_album = os.path.join("vbs", album)
        os.makedirs(pasta_album, exist_ok=True)

        # URL normal
        url = f"http://{ip}:{port}/api/open-song?id={m['id']}&token={token}"

        caminho_arquivo = os.path.join(pasta_album, f"{nome}.vbs")
        criar_vbs(caminho_arquivo, url)

        # Se tiver instrumental -> criar playback
        if m["url_instrumental"]:
            nome_playback = f"{nome} - PLAYBACK"
            caminho_playback = os.path.join(pasta_album, f"{nome_playback}.vbs")

            url_playback = f"http://{ip}:{port}/api/open-song?id={m['id']}&token={token}&tag=2"

            criar_vbs(caminho_playback, url_playback)

    conn.close()


if __name__ == "__main__":
    main()