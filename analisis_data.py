import pandas as pd
import matplotlib.pyplot as plt

# 1. Muat dataset transaksi Elektronik Prima
df = pd.read_csv('transaksi_elektronikprima_2.csv')

# ==========================================
# LATIHAN 1: Bar Chart Total Penjualan per Kategori (Khusus Cabang Surabaya)
# ==========================================
print("--- HASIL LATIHAN 1 ---")
surabaya_df = df[df['cabang'] == 'Surabaya']
latihan_1_result = surabaya_df.groupby('kategori_produk')['total_penjualan'].sum().sort_values(ascending=False)
print(latihan_1_result)

# Membuat Bar Chart Latihan 1
latihan_1_result.plot(kind='bar', title='Total Penjualan per Kategori - Cabang Surabaya', color='teal')
plt.ylabel('Total Penjualan (Rp)')
plt.xlabel('Kategori Produk')
plt.tight_layout()
plt.show() # Screenshot grafik ini untuk Latihan 1


# ==========================================
# LATIHAN 2: Distribusi Frekuensi Bergolong Usia Pelanggan
# ==========================================
print("\n--- HASIL LATIHAN 2 ---")
bins = [0, 20, 40, 60, 80]
labels = ['0-20', '20-40', '40-60', '60-80']
df['kelompok_usia'] = pd.cut(df['usia_pelanggan'], bins=bins, labels=labels, right=False)

latihan_2_result = df['kelompok_usia'].value_counts().sort_index()
print(latihan_2_result)


# ==========================================
# LATIHAN 3: Histogram Harga Satuan Khusus Smartphone
# ==========================================
print("\n--- HASIL LATIHAN 3 ---")
smartphone_df = df[df['kategori_produk'] == 'Smartphone']
print(smartphone_df['harga_satuan'].describe())

# Membuat Histogram Latihan 3
smartphone_df['harga_satuan'].plot(kind='hist', bins=6, edgecolor='white', color='orange',
                                    title='Sebaran Harga Satuan - Khusus Smartphone')
plt.xlabel('Harga Satuan (Rp)')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.show() # Screenshot grafik ini untuk Latihan 3