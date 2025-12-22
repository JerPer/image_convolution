import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mtx = np.array([[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]])

img_object = Image.open("picture.png")

img = np.array(img_object)

img_pad = np.pad(img, pad_width=((1, 1),), mode='edge')[:,:,1:5]

img_conv = np.empty(shape=(100,100,4))
for i in range(1,101):
    for j in range(1,101):
        img_conv[i-1, j-1, 0] = np.sum(img_pad[i-1:i+2, j-1:j+2, 0]*mtx)
        img_conv[i-1, j-1, 1] = np.sum(img_pad[i-1:i+2, j-1:j+2, 1]*mtx)
        img_conv[i-1, j-1, 2] = np.sum(img_pad[i-1:i+2, j-1:j+2, 2]*mtx)

img_conv[:,:,3] = 255

fig, axs = plt.subplots(1, 2, figsize = (10, 5))
axs[0].imshow(img_pad/255)
axs[0].axis('off')
axs[1].imshow(img_conv/255)
axs[1].axis('off')
plt.show()