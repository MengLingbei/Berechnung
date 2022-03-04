import math
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
#from matplotlib import pyplot as plt

#fig = plt.figure()
#ax = Axes3D(fig)


m1 = 3700
m2 = 1600
Fl = 25
z11_x = 65
z11_y = -65/1000
z12_x = 2588/1000
z12_y = -440/1000
z21_x = 6037/1000
z21_y = -234/1000
z22_x = 690/1000
z22_y = -93/1000
g2_x = 8600/1000
g3_x = 5975/1000
g = 9.8


#fai1=math.radians(fai1)

#fai2=math.radians(fai2)
fai1=np.arange(10,70,1)
fai2=np.arange(0,30,1)
fai1=(fai1/180)*np.pi

fai2=(fai2/180)*np.pi
#fai1,fai2=np.meshgrid(fai1,fai2)

def cal(fai1, fai2):
     # F2 berechnen
     F2_1_1 = z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y
     F2_1_2 = g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2)
     F2_2 = (m2 * g * 0.5 * g3_x + Fl * g3_x) * np.cos(fai1 - fai2)

     F2 = round(F2_2 / (np.sin(fai2 - np.arctan(F2_1_1 / F2_1_2)) * z22_x), 4)

     F1_1 = (m1 * g * 0.5 * g2_x + (m2 * g + Fl) * g2_x) * np.cos(fai1)
     F1_2 = (m2 * g * 0.5 * g3_x + Fl * g3_x) * np.cos(fai1 - fai2)
     F1_3 = F2 * np.sin((np.arctan((z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y) / (g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2))))) * z21_x

     F1_4 = z12_x * np.sin(fai1) + z12_y * np.cos(fai1) - z11_y
     F1_5 = z12_x * np.cos(fai1) - z12_y * np.sin(fai1) - z11_x

     F1 = round((F1_1 + F1_2 ) / (np.sin(fai1 - np.arctan(F1_4 / F1_5)) * z12_x), 4)
     #- F1_3
     # L1 berechnen
     L1_1 = (z12_x * np.sin(fai1) + z12_y * np.cos(fai1) - z11_y) ** 2
     L1_2 = (z12_x * np.cos(fai1) - z12_y * np.sin(fai1) - z11_x) ** 2
     L1 = round(np.sqrt(L1_1 + L1_2), 4)

     # L2 berechnen
     L2_1 = (z22_x * np.sin(fai2) - z22_y * np.cos(fai2) + z21_y) ** 2
     L2_2 = (g2_x - z21_x + z22_x * np.cos(fai2) + z22_y * np.sin(fai2)) ** 2
     L2 = round(np.sqrt(L2_1 + L2_2), 4)


     print("fai1 = ", fai1)
     print("fai2 = ", fai2)
     print("F1 = ", F1)
     print("F2 = ", F2)
     print("L1 = ", L1)
     print("L2 = ", L2)
for i in range(0,50):
     cal(fai1[i],fai2[i])

#plt.xlabel('fai1')
#plt.ylabel('fai2')
#ax.plot_surface(fai1,fai2,L1,rstride=1,cstride=1,cmap='rainbow')
#plt.show()
