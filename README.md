# 🎵 LouvorJA API Exporter

Ferramenta para exportar músicas do banco de dados do LouvorJA e gerar arquivos .vbs compatíveis com o Holyrics, permitindo abrir músicas automaticamente via API.

## 📌 Descrição

O LouvorJA API Exporter lê o banco de dados (database.db) do LouvorJA e gera scripts .vbs organizados por álbum.

Esses arquivos podem ser utilizados dentro do Holyrics, permitindo abrir músicas do LouvorJA diretamente pelo sistema, como se fossem mídias locais.

Quando uma música possui versão instrumental, o sistema também gera automaticamente um segundo arquivo com a versão PLAYBACK.

## 🎯 Principal uso

A principal finalidade é integrar o LouvorJA com o Holyrics.

Após a geração, os arquivos devem ser copiados para:
```
C:\Holyrics\Holyrics\files\media\file
```
Assim, as músicas passam a aparecer no Holyrics e podem ser executadas diretamente por lá.

## ⚙️ Requisitos
Python 3 instalado
Banco de dados do LouvorJA (database.db)

## 📍 Local padrão do banco:
```
C:\Program Files (x86)\Louvor JA\config
```
## 📁 Estrutura do projeto

O arquivo main.py deve estar na mesma pasta do banco de dados:
```
/config
│-- main.py
│-- database.db
```
## 🚀 Como usar
1. Configure as variáveis no main.py
>ip = "SEU_IP"

>port = "SUA_PORTA"

>token = "SEU_TOKEN"
2. Execute o script
python main.py
3. Saída gerada

Será criada a pasta:
```
/vbs/
```
Com estrutura organizada por álbum:
```
vbs/
└── Nome do Álbum/
    ├── Nome da Música.vbs
    └── Nome da Música - PLAYBACK.vbs
```
4. Copie para o Holyrics

Copie o conteúdo da pasta vbs para:
```
C:\Holyrics\Holyrics\files\media\file
```

## 🔗 Funcionamento dos arquivos VBS

Cada arquivo .vbs executa uma requisição HTTP para abrir a música no LouvorJA:
```
http://IP:PORTA/api/open-song?id=ID&token=TOKEN
```
Versão playback:
```
http://IP:PORTA/api/open-song?id=ID&token=TOKEN&tag=2
```
## 💡 Observações

>Os nomes de arquivos e pastas são tratados automaticamente para evitar caracteres inválidos

>Arquivos existentes podem ser sobrescritos
