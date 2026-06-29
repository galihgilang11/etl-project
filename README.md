# etl-project

Project ini melakukan penyeragaman data menggunakan teknik ETL dengan python

#Langkah-Langkah

###1. Extract (Ambil)

proses ini merupakan sebuah proses dimana seorang programmer mengambil data mentah untuk dibaca seperti apa data yang akan diolah

###2. Transform

proeses ini mengolah data dengan cara menyeragamkan data yang ada supaya mudah dibaca oleh sistem sehingga proses analisa menjadi lebih mudah, dan prosesnya dengan cara seperti:
- mengubah kolom date dari teks ke format tanggal
- menghapus data yang berada di sebuah baris dengan nilai kosong

##3. Load
menyimpan data yang sudah bersih ke dalam:
- File csv yang baru
- Database SQLite

##Cara menjalankan

'''bash
python3 extract.py
python3 transform.py
python3 load.py
'''

