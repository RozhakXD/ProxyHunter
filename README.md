# ProxyHunter - Proxy Checker and Scraper
![ProxyHunter Images](https://github.com/user-attachments/assets/94136f6c-445d-44fa-ad50-d65f0830f13e)

## Deskripsi
[ProxyHunter](https://github.com/RozhakXD/ProxyHunter) adalah sebuah alat yang dirancang untuk memudahkan proses scraping proxy dan validasi proxy secara otomatis. Dengan fitur threading dan dukungan untuk berbagai jenis proxy, program ini dapat digunakan untuk mendapatkan proxy yang berkualitas dan valid dengan cepat dan efisien.

Program ini menampilkan hasil dengan antarmuka yang interaktif menggunakan modul `rich`, memberikan tampilan yang menarik dan user-friendly saat digunakan.

## Fitur
- **Antarmuka Pengguna yang Intuitif**: Menampilkan informasi IP dan kota pengguna, serta menampilkan opsi menu yang jelas dan mudah digunakan.
- **Validasi Proxy**: Mengecek keaktifan proxy yang telah di-scrape untuk memastikan proxy tersebut masih dapat digunakan.
- **Scraping Proxy**: Mendukung scraping proxy dari berbagai situs seperti Proxyscrape, Freeproxy, Spys-Me, dan banyak lagi.
- **Penggunaan Multithreading**: Menggunakan multithreading untuk proses scraping yang lebih cepat dan efisien.

## Instalasi
1. Clone repository ini:
    ```bash
    git clone https://github.com/RozhakXD/ProxyHunter.git
    ```
2. Masuk ke direktori ProxyHunter:
    ```bash
    cd ProxyHunter
    ```
3. Install dependencies yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Penggunaan
1. Jalankan program dengan perintah berikut:
    ```bash
    python Run.py
    ```
3. Anda akan disajikan berbagai pilihan menu untuk melakukan scraping dan validasi proxy.
4. Ikuti petunjuk yang muncul di layar untuk memilih sumber scraping dan simpan hasilnya ke file yang Anda inginkan.
5. Gunakan opsi validasi untuk memastikan proxy yang telah di-scrape masih aktif.

## Contoh Penggunaan
Misalnya, untuk melakukan scraping proxy dari Proxyscrape dan menyimpannya dalam file `Penyimpanan/Proxy.txt`:

- Pilih opsi `01` dan masukkan nama file `Penyimpanan/Proxy.txt`.
- Tunggu hingga proses scraping selesai.
- Proxy yang aktif akan disimpan di file yang telah Anda tentukan.

## Opsi Menu
- **01 - 10**: Scraping proxy dari berbagai sumber seperti Proxyscrape, Freeproxy, Proxy-Org, dan lainnya.
- **11**: Memeriksa apakah proxy dalam daftar Anda masih aktif atau tidak.
- **12**: Keluar dari program.

## Masalah Umum dan Solusi
1. **Koneksi Terputus atau Lambat**
    - **Masalah**: Jika koneksi internet Anda lambat atau tidak stabil, proses pengumpulan atau pengecekan proxy bisa gagal atau memakan waktu lama.
    - **Solusi**: Pastikan koneksi internet Anda stabil. Anda juga dapat mengurangi jumlah `max_workers` dalam `ThreadPoolExecutor` untuk mengurangi beban pada koneksi.
2. **Tidak Ada Proxy yang Valid Ditemukan**
    - **Masalah**: Setelah menjalankan scraper, tidak ada proxy yang valid ditemukan.
    - **Solusi**: Coba gunakan sumber lain untuk scraping atau cek apakah sumber tersebut masih aktif dan menyediakan proxy yang valid.
3. **Pemblokiran IP oleh Situs Penyedia Proxy**
    - **Masalah**: Terlalu banyak permintaan dalam waktu singkat dapat menyebabkan pemblokiran IP Anda oleh situs penyedia proxy.
    - **Solusi**: Tambahkan jeda waktu (delay) antara setiap permintaan atau gunakan proxy yang berbeda untuk setiap permintaan scraping.

## Dukungan
Jika Anda merasa proyek ini bermanfaat dan ingin mendukung pengembangan lebih lanjut, Anda bisa memberikan dukungan melalui:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Peringatan
**Penggunaan bandwidth**: Menggunakan aplikasi ini untuk mengumpulkan dan memeriksa proxy dalam jumlah besar dapat mengkonsumsi bandwidth yang signifikan. Pastikan Anda memiliki koneksi internet yang cukup cepat dan stabil.

## Tangkapan Layar
![FunPic_20240901-1](https://github.com/user-attachments/assets/e43aab98-ecc9-49f9-be7a-b2de92dec447)

![FunPic_20240901-2](https://github.com/user-attachments/assets/90492b39-6630-479e-9f6e-e97c4aa106f1)

## Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki saran, perbaikan, atau fitur baru yang ingin ditambahkan, silakan buat pull request atau buka issue di repository ini.

## Lisensi
Proyek ini dilisensikan di bawah lisensi [MIT License](https://github.com/RozhakXD/ProxyHunter?tab=GPL-3.0-1-ov-file).

##
Dikembangkan dengan ❤️ oleh [Rozhak](https://github.com/RozhakXD). Nikmati pengumpulan proxy yang cepat dan mudah dengan ProxyHunter!
