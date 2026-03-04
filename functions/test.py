from controler import predict_image

IMG_PATH = "../reconhecimentoImagem/assets/minha_imagem.jpg"

classe, accuracy = predict_image("../reconhecimentoImagem/assets/minha_imagem.jpg")

print(f"Classe: {classe}, Precissão: {accuracy:.2f}%")