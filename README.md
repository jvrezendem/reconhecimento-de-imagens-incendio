# Reconhecimento de Imagens de incêncio com TensorFLow

Este repositório apresenta um projeto de **classificação de imagens utilizando Deep Learning**, com o objetivo de identificar se uma imagem contém ou não sinais visuais de incêndio.
O projeto utiliza **Python**, **TensorFlow** e **Keras** para treinamento e teste de um modelo de rede neural convolucional, também conhecida como **CNN — Convolutional Neural Network**.

---

## Objetivo do Projeto

O objetivo principal deste projeto é desenvolver um modelo capaz de classificar imagens em duas categorias:

- **Incêndio**
- **Não incêndio**

A proposta é demonstrar uma aplicação prática de visão computacional para reconhecimento de padrões visuais em imagens, utilizando uma arquitetura simples de rede neural convolucional.

Esse tipo de solução pode servir como base para aplicações futuras em:

- Monitoramento ambiental;
- Detecção automática de focos de incêndio;
- Sistemas de alerta;
- Análise de imagens por inteligência artificial;
- Projetos acadêmicos de visão computacional.

---

## Sobre o Modelo

O modelo utilizado foi baseado em uma arquitetura sequencial com camadas convolucionais.

A estrutura segue uma abordagem comum em problemas de classificação de imagens:

- Camadas de convolução `Conv2D`;
- Camadas de agrupamento `MaxPooling2D`;
- Camada de achatamento `Flatten`;
- Camada densa intermediária com ativação ReLU;
- Camada final para classificação.

A arquitetura foi inspirada no tutorial oficial de classificação de imagens do TensorFlow:

[Classificação de imagens com TensorFlow](https://www.tensorflow.org/tutorials/images/classification?hl=pt-br)

O modelo contém três blocos principais de convolução, cada um acompanhado por uma camada de agrupamento máximo. Em seguida, há uma camada totalmente conectada com **128 unidades** e função de ativação **ReLU**.

> Observação: este modelo não foi projetado inicialmente para máxima precisão. O foco principal é demonstrar uma abordagem padrão de classificação de imagens com TensorFlow/Keras.

---

## Aumento de Dados

Durante o treinamento do modelo, foi aplicada a técnica de **aumento de dados** (*data augmentation*), que consiste em gerar variações artificiais das imagens originais para tornar o modelo mais robusto.

Essa técnica é muito utilizada em projetos de visão computacional, principalmente quando o conjunto de imagens é limitado ou quando se deseja melhorar a capacidade de generalização da rede neural.

Na prática, o aumento de dados permite que o modelo veja diferentes versões de uma mesma imagem durante o treinamento, como:

- rotações leves;
- espelhamento horizontal;
- zoom;
- pequenas alterações de enquadramento.

Dessa forma, a rede neural aprende a reconhecer padrões importantes relacionados à presença de incêndio, sem depender da posição exata da imagem.

---

### Benefícios

O uso de aumento de dados traz vantagens importantes:

- Reduz o **overfitting**;
- Melhora a capacidade de generalização;
- Torna o modelo mais resistente a variações reais;
- Aumenta a eficiência do treinamento sem precisar de mais dados reais.

---

### Aplicação no projeto

No contexto deste projeto, o aumento de dados ajuda o modelo a identificar incêndios em diferentes condições, como:

- variação de iluminação;
- diferentes ângulos da imagem;
- presença de fumaça em posições variadas;
- tamanhos diferentes de focos de incêndio;
- cenários ambientais distintos.

---

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
