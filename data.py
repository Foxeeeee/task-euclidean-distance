import pandas as pd

# Data
data = [
    {
    "nama_produk": "jeruk bali",
    "senin": 230,
    "selasa": 235,
    "rabu": 267,
    "kamis": 300,
    "jumat": 267,
    "sabtu": 210,
    "kategori": "sedang"
    },
    {
    "nama_produk": "salak",
    "senin": 109,
    "selasa": 120,
    "rabu": 110,
    "kamis": 130,
    "jumat": 180,
    "sabtu": 123,
    "kategori": "kurang"
    },
    {
    "nama_produk": "anggur",
    "senin": 89,
    "selasa": 90,
    "rabu": 95,
    "kamis": 100,
    "jumat": 101,
    "sabtu": 98,
    "kategori": "kurang"
    },
    {
    "nama_produk": "apel",
    "senin": 300,
    "selasa": 290,
    "rabu": 398,
    "kamis": 299,
    "jumat": 301,
    "sabtu": 330,
    "kategori": "laku"
    },
    {
    "nama_produk": "manggis",
    "senin": 450,
    "selasa": 430,
    "rabu": 410,
    "kamis": 420,
    "jumat": 405,
    "sabtu": 460,
    "kategori": "laku"
    },
    {
    "nama_produk": "durian",
    "senin": 235,
    "selasa": 269,
    "rabu": 299,
    "kamis": 278,
    "jumat": 298,
    "sabtu": 250,
    "kategori": "sedang"
    },
    {
    "nama_produk": "dukuh",
    "senin": 130,
    "selasa": 90,
    "rabu": 86,
    "kamis": 102,
    "jumat": 101,
    "sabtu": 110,
    "kategori": "kurang"
    },
    {
    "nama_produk": "jambu air",
    "senin": 95,
    "selasa": 90,
    "rabu": 101,
    "kamis": 92,
    "jumat": 95,
    "sabtu": 99,
    "kategori": "kurang"
    },
    {
    "nama_produk": "alpukat",
    "senin": 190,
    "selasa": 210,
    "rabu": 280,
    "kamis": 245,
    "jumat": 230,
    "sabtu": 290,
    "kategori": "laku"
    },
    {
    "nama_produk": "semangka",
    "senin": 200,
    "selasa": 203,
    "rabu": 210,
    "kamis": 221,
    "jumat": 219,
    "sabtu": 204,
    "kategori": ""
    },
]

# Mengubah data menjadi DataFrame
df = pd.DataFrame(data)

