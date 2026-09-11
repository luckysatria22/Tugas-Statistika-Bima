import pandas as pd
import matplotlib.pyplot as plt

# 1. Muat dataset
df = pd.read_csv('transaksi_elektronikprima.csv')

# --- 5 Baris Pertama & Tabel Frekuensi ---
print("--- 5 Baris Pertama ---")
print(df.head())

print("\n--- Tabel Frekuensi Cabang ---")
print(df['cabang'].value_counts())

print("\n--- Tabulasi Silang Cabang x Kategori ---")
print(pd.crosstab(df['cabang'], df['kategori_produk']))

# --- LANGKAH 3: Bar Chart ---
df.groupby('cabang')['total_penjualan'].sum().sort_values(ascending=False).plot(
    kind='bar', title='Total Penjualan per Cabang')
plt.ylabel('Total Penjualan (Rp)')
plt.tight_layout()
plt.show()  # Akan memunculkan jendela grafik pertama

df.groupby('kategori_produk')['total_penjualan'].sum().sort_values(ascending=False).plot(
    kind='bar', title='Total Penjualan per Kategori Produk')
plt.ylabel('Total Penjualan (Rp)')
plt.tight_layout()
plt.show()  # Akan memunculkan jendela grafik kedua

# --- LANGKAH 4: Pie Chart ---
df['metode_pembayaran'].value_counts().plot(
    kind='pie', autopct='%1.1f%%', title='Proporsi Metode Pembayaran')
plt.ylabel('')
plt.tight_layout()
plt.show()  # Akan memunculkan jendela grafik ketiga

# --- LANGKAH 5: Histogram ---
df['harga_satuan'].plot(kind='hist', bins=8, edgecolor='white',
                        title='Sebaran Harga Satuan Produk')
plt.xlabel('Harga Satuan (Rp)')
plt.tight_layout()
plt.show()  # Akan memunculkan jendela grafik keempat

# --- LANGKAH 6: Line Chart ---
df['tanggal'] = pd.to_datetime(df['tanggal'])
df['bulan'] = df['tanggal'].dt.to_period('M')

df.groupby('bulan')['total_penjualan'].sum().plot(
    kind='line', marker='o', title='Tren Total Penjualan per Bulan')
plt.ylabel('Total Penjualan (Rp)')
plt.xlabel('Bulan')
plt.tight_layout()
plt.show()  # Akan memunculkan jendela grafik kelima