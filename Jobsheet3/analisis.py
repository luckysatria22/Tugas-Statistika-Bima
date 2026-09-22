import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
df = pd.read_csv('transaksi_elektronikprima.csv') 

df.boxplot(column='total_penjualan', by='cabang', figsize=(8,5))
plt.title('Sebaran Total Penjualan per Cabang')
plt.suptitle('')
plt.ylabel('Total Penjualan (Rp)')
plt.savefig('boxplot_output1.png', bbox_inches='tight')
print("Grafik berhasil disimpan sebagai boxplot_output.png")
