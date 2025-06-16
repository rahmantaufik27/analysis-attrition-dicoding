# Proyek Akhir: Menyelesaikan Permasalahan Human Resource

## Business Understanding

Perusahaan Jaya Jaya Maju menghadapi tingginya tingkat attrition karyawan, melebihi 10%, yang secara signifikan mengganggu stabilitas operasional dan efisiensi. Fenomena ini mengindikasikan adanya ketidakpuasan atau faktor pendorong lain yang menyebabkan karyawan memutuskan untuk meninggalkan perusahaan. Tingginya attrition rate ini berpotensi menyebabkan kerugian finansial akibat biaya rekrutmen dan pelatihan karyawan baru yang tinggi, penurunan produktivitas tim, serta hilangnya keahlian dan pengetahuan institusional. Oleh karena itu, perusahaan perlu secara mendesak mengidentifikasi akar penyebab dari tingginya attrition ini agar dapat merumuskan strategi retensi yang efektif.

## Permasalahan Bisnis

Proyek ini bertujuan untuk mengatasi beberapa tantangan bisnis utama yang dihadapi oleh perusahaan Jaya Jaya Maju terkait tingkat *attrition* yang tinggi:

* **Mengidentifikasi Akar Penyebab Attrition**: Mendapatkan pemahaman mendalam tentang faktor-faktor krusial—baik dari aspek demografi karyawan, tingkat kepuasan kerja, maupun indikator finansial—yang berkontribusi pada keputusan karyawan untuk *resign*.
* **Menganalisis Kepuasan Karyawan**: Menilai dan memahami tingkat kepuasan karyawan berdasarkan dimensi-dimensi penting seperti _Job Satisfaction_, _Work-Life Balance_, dan _Environment Satisfaction_.
* **Mengungkap Pola Perilaku Karyawan yang Berisiko Resign**: Mengidentifikasi karakteristik dan kebiasaan umum pada karyawan yang cenderung meninggalkan perusahaan, termasuk dampak dari faktor seperti jarak tempat tinggal ke kantor, kebiasaan lembur (_OverTime_), dan tingkat pendapatan.
* **Menyediakan Solusi Analisis Berkelanjutan**: Mengembangkan sebuah _business dashboard_ interaktif yang akan menjadi alat esensial bagi manajemen HR untuk memantau, menganalisis, dan memahami dinamika _attrition_ secara visual dan _real-time_.

Dengan berhasil menyelesaikan poin-poin permasalahan di atas, perusahaan diharapkan dapat:

* **Menekan Attrition Rate**: Mengambil tindakan pencegahan yang lebih tepat sasaran untuk mengurangi jumlah karyawan yang *resign*.
* **Meningkatkan Efektivitas Program Retensi**: Merancang dan menerapkan inisiatif retensi karyawan yang didasarkan pada data dan wawasan yang akurat.
* **Meningkatkan Kesejahteraan Karyawan**: Berkontribusi pada peningkatan kepuasan kerja dan, pada akhirnya, produktivitas karyawan secara keseluruhan.

## Cakupan Proyek

1) Data undestanding, Explorasi data analysis, Data Preprocessing/Preparation (`notebook.ipynb`)
2) Membuat model machine learning (ML) untuk memprediksi attrition (`prediction.py`)
3) Membuat business dashboard (berdasarkan hasil pemodelan ml) untuk mengeksplore dan menganalisis data secara visual (`rtaufik_27-video.txt`)
4) Menjawab permasalahan bisnis

## Persiapan

Sumber data: [Dataset Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

### _Setup Environment_

Untuk menjalankan proyek ini, pastikan Anda memiliki **Python** terinstal di sistem Anda. Ikuti langkah-langkah di bawah ini untuk menyiapkan lingkungan pengembangan yang terisolasi dan menginstal semua dependensi yang diperlukan:

1.  **Buka Terminal atau Command Prompt**
    Navigasikan ke direktori proyek (`Eksperimen SML`) tempat file `requirements.txt` berada.

    ```bash
    cd <path_ke_direktori_proyek_anda>/Eksperimen SML
    ```

2.  **Membuat Virtual Environment (_venv_)**
    Buat lingkungan virtual baru untuk proyek ini. Ini akan mengisolasi dependensi proyek agar tidak bentrok dengan proyek Python lainnya di sistem Anda.

    ```bash
    python -m venv venv
    ```

3.  **Mengaktifkan Virtual Environment**
    Setelah `venv` berhasil dibuat, aktifkan lingkungan virtual tersebut:

    * **Di Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **Di macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    Anda akan melihat `(venv)` di awal *prompt* terminal Anda, menandakan bahwa *virtual environment* sudah aktif.

4.  **Menginstal Dependensi Libraries**
    Setelah *virtual environment* aktif, instal semua pustaka Python yang diperlukan dari file `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Menjalankan Notebook Jupyter (EDA & ML Modeling)**
    Setelah semua dependensi terinstal, Anda dapat menjalankan notebook Jupyter:

    * Pastikan Anda berada di direktori `Eksperimen SML`.
    * Mulai server Jupyter Notebook:
        ```bash
        jupyter notebook
        ```
    * Sebuah tab *browser* akan terbuka, menampilkan antarmuka Jupyter. Navigasikan ke `Preprocessing/Eksperiment_rtaufik27.ipynb` dan buka file tersebut untuk melihat hasil eksplorasi data analisis serta pemodelan *machine learning* (ML). Ikuti instruksi di dalam *notebook* untuk menjalankan setiap sel.

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

1) Fokus pada Karyawan Loyal dan Matang:Saat rekrutmen, utamakan kandidat dengan riwayat kerja yang stabil (lama di perusahaan sebelumnya), usia yang lebih matang, dan kondisi pribadi yang stabil. Terutama untuk posisi penting seperti riset atau strategis.
2) Ciptakan Lingkungan Kerja yang Seimbang:Kurangi beban lembur. Data menunjukkan lembur berkontribusi besar terhadap keputusan karyawan untuk keluar. Budaya kerja yang menghargai work-life balance bisa menurunkan angka attrition.
3) Perhatikan Kompensasi dan Kepuasan Karyawan:Pendapatan yang terlalu rendah, atau tidak sesuai dengan pengalaman, bisa menjadi pemicu resign. Pertimbangkan review berkala terhadap struktur gaji dan kepuasan kerja.
