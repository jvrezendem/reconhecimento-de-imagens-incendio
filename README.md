# Reconhecimento de Imagens de incêncio com TensorFLow

## Sobre o Modelo
Foi usado um modelo sequencial que consiste em três blocos de convolução (`tf.keras.layers.Conv2D`) com uma camada de agrupamento máximo (`tf.keras.layers.MaxPooling2D`) em cada um deles. Há uma camada totalmente conectada ( `tf.keras.layers.Dense`) com 128 unidades em cima dela que é ativada por uma função de ativação ReLU ( 'relu' ). Este modelo não foi ajustado para alta precisão - o objetivo deste tutorial é mostrar uma abordagem padrão. From: https://www.tensorflow.org/tutorials/images/classification?hl=pt-br


## Dados
O modelo foi treinado com o dataset criado em `datatest`, dividido em duas classes ***incendio***, e ***naoIncendio***. O dataset conta com mais de 4500 imagens divididas igualmente entre as classes.

## Como usar

### Estrutura do projeto

reconhecimentoImagem/
│
├── .venv/
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ └── share/
│
├── assets/
│
├── datatest/
│
├── **functions**/
│
├── model/
│
├── .gitignore
├── pyvenv.cfg
├── README.md
└── testeImg.ipynb

Escolha uma imagem qualquer e baixe ela. Entre na pasta `functions` e no arquivo `test.py` troque **IMG_PATH** para o caminho da sua imagem.

## Tecnologias

- Python 3.11.9
- TensorFlow
- Keras
- NumPy