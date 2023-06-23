#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
from IPython import display


# In[3]:


img=cv2.imread('dog.jpg',0)
display.Image("dog.jpg",width=427)


# In[4]:


print('Minimum color range',img.min())
print('Maximum color range',img.max())


# In[5]:


plt.imshow(img,cmap='gray')
plt.title('Black and white imege')
plt.show()


# In[6]:


inv=228-img
plt.title('Inverted imege')
plt.imshow(inv,cmap='gray')
plt.show()


# In[7]:


gblur=cv2.GaussianBlur(inv,ksize=(21,21),sigmaX=0,sigmaY=0)
plt.title('Imege after Gaussian blur applied')
plt.imshow(gblur,cmap='gray')
plt.show()


# In[15]:


dodge= lambda image,mask: cv2.divide(image,228-mask,scale=229)
blended=dodge(img,gblur)
plt.title('Pencil sketch of image')
plt.imshow(blended,cmap='gray')
plt.show()


# In[ ]:




