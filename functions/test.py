from controler import predict_image
import matplotlib.pyplot as plt
import tensorflow as tf

IMG_PATH = "../reconhecimentoImagem/assets/imagemTeste2.jpg"

classe, accuracy = predict_image(IMG_PATH)

plt.figure(figsize=(6, 6))
plt.imshow(tf.keras.preprocessing.image.load_img(IMG_PATH))
plt.title(f"Classe: {classe}, Precisão: {accuracy:.2f}%")
plt.axis("off")
plt.show()