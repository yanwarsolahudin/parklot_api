# ParkLot API

Adalah API sistem menejemen parkir pada suatu istansi. Aplikasi ini dibuat
sebagai online test yang diberikan oleh `Sigma`.


## Persyaratan
Pada saat API ini dibuat saya menggunakan:

- Python 3.6
- Django
- Django Rest Framework
- Ubuntu (optional)
- Database bisa diatur pada file `mysite/settings.py`. Untuk saat ini demi kemudahan, 
saya menggunakan database default yakni `SQLite`.

## Diagram
Anda bisa melihat diagram rancangan database schema dan use case di:

https://drive.google.com/open?id=1gDFVpVaN_Rj0sIEHidA77WJqS0oGDyZ6

## Langkah Instalasi

Pastikan Python 3.6 sudah Anda instal. Pertama-tama clone project ini lalu
masuk ke direktori project. 

Buat terlebih dahulu Virtual Environment dan aktifkan:

```
$ python .venv -p python3.6
$ source .venv/bin/activate
```

Jalankan perintah berikut untuk menginstal paket-paket yang diperlukan:

```
$ pip install -r requirements.txt
```

Jalankan perintah berikut untuk melakukan migrate tabel:

```
$ python manage.py makemigrations
$ python manage.py migrate
```


## Membuat Admin

Jalankan perintah berikut pada terminal di dalam project root:

```
$ python manage.py createsuperuser
```

Isi data yang diperintahkan oleh Django.


## Menjalankan Development Server

Jalankan perintah berikut untuk menjalankan server development:

```
$ python manage.py runserver
```


## Playground API

Anda bisa menggunakan dan mencoba API ini dengan 2 cara:

1. Menggunakan Browsable API milik Django Rest
2. Menggunakan Aplikasi `Insomnia`.

### Insomnia

Unduh dan instal Insomnia di url berikut:

https://insomnia.rest/

Selanjutnya export data Insomnia untuk ParkLot. Anda bisa mengunduhnya di:

https://drive.google.com/open?id=1gDFVpVaN_Rj0sIEHidA77WJqS0oGDyZ6


### Browsable API

Anda hanya perlu menjalankan server dan membuka url `http://localhost:8000/`. Untuk 
API yang membutuhkan credential, sebaiknya setelah Anda membuat user baru sebagai admin,
Anda diharapkan login terlebih dahulu di `http://localhost:8000/admin`.

