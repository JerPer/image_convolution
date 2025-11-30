import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mtx = np.empty(shape=(3, 3, 3),dtype=float)
mtx[:,:] = 1/3

img_object = Image.open("picture.png")

img = np.array(img_object)

print(np.shape(img))
plt.imshow(img)
plt.show()

img_gs = np.array((img[:,:,0] + img[:,:,1] + img[:,:,2])/3)

plt.imshow(img_gs,cmap='gray',vmin=0, vmax=1)
plt.show()