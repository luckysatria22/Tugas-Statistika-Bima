import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
df = pd.read_csv('transaksi_elektronikprima.csv') 
print(df.head())

mean_rating = df['rating_kepuasan'].mean() 
median_rating = df['rating_kepuasan'].median() 
modus_rating = df['rating_kepuasan'].mode()[0] 
print('Mean  :', mean_rating) 
print('Median:', median_rating) 
print('Modus :', modus_rating)
print()

mean_tp = df['total_penjualan'].mean() 
median_tp = df['total_penjualan'].median() 
print('Mean total_penjualan  :', mean_tp) 
print('Median total_penjualan:', median_tp)

variabilitas = df.groupby('kategori_produk')['harga_satuan'].agg(['mean', 'std', 'var'])
print(variabilitas) 
laptop = df[df['kategori_produk'] == 'Laptop']['harga_satuan'] 
q1 = laptop.quantile(0.25) 
q3 = laptop.quantile(0.75) 
iqr = q3 - q1 
batas_bawah = q1 - 1.5 * iqr 
batas_atas = q3 + 1.5 * iqr 
print('Q1 :', q1) 
print('Q3 :', q3) 
print('IQR:', iqr) 
print('Batas outlier:', batas_bawah, '-', batas_atas)

df.boxplot(column='harga_satuan', by='kategori_produk', figsize=(8,5)) 
plt.title('Sebaran Harga Satuan per Kategori Produk') 
plt.suptitle('') 
plt.ylabel('Harga Satuan (Rp)') 
plt.savefig('boxplot_output.png', bbox_inches='tight')
print("Grafik berhasil disimpan sebagai boxplot_output.png")