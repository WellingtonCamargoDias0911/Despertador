# Alarme Pythonico

Este é um simples aplicativo de alarme desenvolvido em Python usando a biblioteca `tkinter` para a interface gráfica e a função `datetime` para controlar a hora de disparo do alarme. O programa permite ao usuário definir uma hora, minuto e segundo para que um som de alarme seja reproduzido quando o horário selecionado for atingido.

## Funcionalidades

- Definir o horário do alarme (hora, minuto, segundo).
- Disparar o alarme tocando um arquivo de áudio (`Alarm.wav`) quando o horário definido for alcançado.
- Interface gráfica simples utilizando `tkinter`.

## Como funciona

1. O usuário define o horário desejado para o alarme através de três menus suspensos (hora, minuto e segundo).
2. Após pressionar o botão "Definir", o programa entra em um loop infinito verificando o horário atual.
3. Quando o horário atual do sistema corresponde ao horário definido, o alarme é disparado, tocando o arquivo `Alarm.wav`.
4. O programa usa `sleep` para aguardar um segundo entre as verificações de horário.

## Como usar

1. Clone ou baixe este código.
2. Salve um arquivo de áudio `Alarm.wav` na mesma pasta do script ou altere o caminho do arquivo no código.
3. Execute o script. A janela será aberta permitindo que você defina o horário para o alarme.
4. Defina a hora, minuto e segundo desejados e pressione o botão "Definir".
5. O alarme será disparado quando o horário configurado for atingido.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (geralmente já instalada com o Python).
- Um arquivo de áudio `Alarm.wav` para o alarme.

## Como executar

Para executar o programa, basta rodar o seguinte comando no terminal ou prompt de comando:

```bash
python nome_do_arquivo.py
