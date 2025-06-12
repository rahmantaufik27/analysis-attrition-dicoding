# Proyek Akhir: Menyelesaikan Permasalahan Human Resource

## Business Understanding

Perusahaan Jaya Jaya Maju kesulitan dalam mengelola karyawan, yang berimbas terhadap tingginya attrition rate hingga lebih dari 10%. Untuk mencegah hal ini semakin parah, perlu mengidentifikasi dan menganalisis berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.

### Permasalahan Bisnis

1) Identifikasi Faktor Utama Penyebab Attrition (Karyawan Resign)
2) Rekomendasi Aksi untuk Mengurangi Attrition

### Cakupan Proyek

1) Explorasi data analysis (data understanding)
2) Membuat model machine learning (berdasarkan data preparation) untuk memprediksi attrition
3) Membuat business dashboard (berdasarkan hasil pemodelan ml) untuk mengeksplore dan menganalisis data secara visual
4) Menjawab permasalahan bisnis

### Persiapan

Sumber data: [Dataset Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

1) Buka Text Editor Programming kalian
2) Pastikan Bahasa Pemrograman Python sudah terinstall di lokal
3) Install dependecies libraries (bisa dilihat di requirements.txt) dengan menggunakan command `pip install -r requirements.txt.` di terminal
4) Running file `notebook.ipynb` untuk melihat hasil eksplorasi data analysis serta pemodelan machine learning (ML)

## Business Dashboard

- Business Dashboard dikembangkan menggunakan Google Looker Studio dan data hasil pemodelan ML sebelumnya
- Business Dashboard meliputi fitur filter attrition, informasi yang disampaikan dalam bentuk summary, diagram, dan table
- Visualisasi data yang bisa diexplore dan dianalisis data meliputi hubungan attrition dengan monthly income, over time, years at company, total working years, number company worked, marital status, age, dan lain-lain
- Dashboard bisa diakses di [Business Dashboard - Attrition Analysis](https://bit.ly/attrition_analysis_dashboard)
- Penjelasan dashboard bisa dilihat di [Video Attrition Analysis Explanation](https://youtu.be/qTeWGMTanJQ?si=o-OubsdlY3PMGBFY)

## Conclusion

Berdasarkan permasalahan bisnis terkait identifikasi faktor penyebab attrition, dilakukan pemodelan klasifikasi attrition menggunakan model ML dengan metode Random Forest serta pengembangan Business Dashboard untuk analisis lebih lanjut, hasilnya dapat disimpulkan untuk faktor-faktor yang paling berpengaruh terhadap attrition antara lain:
- Lama bekerja di perusahaan saat ini (Years at company)
- Total pengalaman kerja secara keseluruhan (Total working years)
- Lembur (overtime)
- Jumlah perusahaan sebelumnya (Numbers company worked)
- Pendapatan bulanan (Monthly Income)
- Usia
- Status pernikahan

### Rekomendasi Action Items (Optional)

1) Fokus pada Karyawan Loyal dan Matang: Saat rekrutmen, utamakan kandidat dengan riwayat kerja yang stabil (lama di perusahaan sebelumnya), usia yang lebih matang, dan kondisi pribadi yang stabil. Terutama untuk posisi penting seperti riset atau strategis.
2) Ciptakan Lingkungan Kerja yang Seimbang: Kurangi beban lembur. Data menunjukkan lembur berkontribusi besar terhadap keputusan karyawan untuk keluar. Budaya kerja yang menghargai work-life balance bisa menurunkan angka attrition.
3) Perhatikan Kompensasi dan Kepuasan Karyawan: Pendapatan yang terlalu rendah, atau tidak sesuai dengan pengalaman, bisa menjadi pemicu resign. Pertimbangkan review berkala terhadap struktur gaji dan kepuasan kerja.
