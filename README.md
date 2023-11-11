# Tubes-Pemlan
Chatting App with Django
**#requirement **
1. Virtual environtment -> dibuat di directory file disimpan 
2. Django -> setelah membuat v env, lanjut install django (pip install Django)
3. Channels -> pip install Channels
4. daphne -> pip install daphne

Setelah semua siap, lakukan migrate untuk mengupdate database (py manage.py migrate)
Kemudian buat akun baru (py manage.py createsuperuser) -> buat email address kosongin aja gpp alias pencet enter langsung

Setelah itu, jalankan server (py manage.py runserver)

Nah setelah server berhasil berjalan, buka browser lalu ketik localhost:8000
Login pake akun yang dibuat tadi 

Nah pas masuk pasti masih kosongan kan, untuk membuat grupchat tinggal ketik localhost:8000/admin/
tinggal atur-atur ajaa 

terus untuk fitur personal chatnya, pasti masih kosong kan. itu tu karena harus ada >=2 user. Jadinya harus buat user baru pake createsuperuser tadi 


