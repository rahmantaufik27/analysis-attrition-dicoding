# Proyek Akhir: Menyelesaikan Permasalahan Human Resource

## Business Understanding

Perusahaan Jaya Jaya Maju menghadapi tingginya tingkat attrition karyawan, melebihi 10%, yang secara signifikan mengganggu stabilitas operasional dan efisiensi. Fenomena ini mengindikasikan adanya ketidakpuasan atau faktor pendorong lain yang menyebabkan karyawan memutuskan untuk meninggalkan perusahaan. Tingginya attrition rate ini berpotensi menyebabkan kerugian finansial akibat biaya rekrutmen dan pelatihan karyawan baru yang tinggi, penurunan produktivitas tim, serta hilangnya keahlian dan pengetahuan institusional. Oleh karena itu, perusahaan perlu secara mendesak mengidentifikasi akar penyebab dari tingginya attrition ini agar dapat merumuskan strategi retensi yang efektif.

## Permasalahan Bisnis

Proyek ini bertujuan untuk mengatasi beberapa tantangan bisnis utama yang dihadapi oleh perusahaan Jaya Jaya Maju terkait tingkat *attrition* yang tinggi:

* **Mengidentifikasi Akar Penyebab Attrition**: Mendapatkan pemahaman mendalam tentang faktor-faktor krusial—baik dari aspek demografi karyawan, status karyawan, maupun indikator finansial—yang berkontribusi pada keputusan karyawan untuk *resign*.
* **Menganalisis Kepuasan Karyawan**: Menilai dan memahami tingkat kepuasan karyawan berdasarkan dimensi-dimensi penting seperti _Monthly Salary Income_, _Monthly Rate_, dan lain-lain.
* **Mengungkap Pola Perilaku Karyawan yang Berisiko Resign**: Mengidentifikasi karakteristik dan kebiasaan umum pada karyawan yang cenderung meninggalkan perusahaan, termasuk dampak dari faktor seperti jarak tempat tinggal ke kantor, kebiasaan lembur (_OverTime_), dan lain-lain.
* **Menyediakan Solusi Analisis Berkelanjutan**: Mengembangkan sebuah _business dashboard_ interaktif yang akan menjadi alat esensial bagi manajemen HR untuk memantau, menganalisis, dan memahami dinamika _attrition_ secara visual dan _real-time_.

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

6.  **Menjalankan Skrip Python (.py) (Opsional)**
    Python script untuk memprediksi attrtion dijalankan secara terpisah, gunakan perintah berikut di terminal:

    ```bash
    python3 prediction.py
    ```

## Business Dashboard

- Business Dashboard dikembangkan menggunakan Google Looker Studio dan data hasil pemodelan ML sebelumnya
- Business Dashboard meliputi fitur filter attrition, informasi yang disampaikan dalam bentuk summary, diagram, dan table
- Visualisasi data yang bisa diexplore dan dianalisis data meliputi hubungan attrition dengan monthly income, over time, years at company, total working years, number company worked, marital status, age, dan lain-lain
- Dashboard bisa diakses di [Business Dashboard - Attrition Analysis](https://bit.ly/attrition_analysis_dashboard)
- Penjelasan dashboard bisa dilihat di [Video Attrition Analysis Explanation](https://youtu.be/qTeWGMTanJQ?si=o-OubsdlY3PMGBFY)

## Conclusion

Proyek ini telah berhasil mengatasi tantangan bisnis utama perusahaan Jaya Jaya Maju terkait attrition rate yang tinggi melalui serangkaian analisis komprehensif. Melalui proses eksplorasi data dan analisis mendalam, kami berhasil **mengidentifikasi akar penyebab attrition, menganalisis kepuasan karyawan, dan mengungkap pola perilaku karyawan yang berisiko resign**. Ditemukan bahwa faktor-faktor paling berpengaruh terhadap attrition meliputi:

- **Lama bekerja di perusahaan saat ini (Years at company)**: Karyawan dengan masa kerja yang relatif singkat, lebih rentan mengalami attrition. Hal ini bisa disebabkan oleh ketidakcocokan awal, kurangnya ikatan emosional dengan perusahaan, atau pencarian peluang yang lebih baik.
- **Total pengalaman kerja secara keseluruhan (Total working years)**: Karyawan dengan total pengalaman kerja yang lebih sedikit cenderung memiliki tingkat attrition yang lebih tinggi. Mereka mungkin masih dalam tahap eksplorasi karier atau belum menemukan "rumah" profesional yang cocok.
- **Lembur (overtime)**: Beban kerja lembur yang sering dan tidak seimbang secara signifikan meningkatkan risiko attrition. Hal ini berdampak negatif pada work-life balance dan dapat menyebabkan burnout.
- **Jumlah perusahaan sebelumnya (Numbers company worked)**: Karyawan dengan riwayat berpindah-pindah perusahaan (memiliki jumlah perusahaan sebelumnya yang lebih tinggi) mungkin memiliki kecenderungan lebih tinggi untuk resign lagi, karena mereka terbiasa dengan perubahan lingkungan kerja.
- **Pendapatan bulanan (Monthly Income)**: Pendapatan yang dirasa tidak adil atau tidak kompetitif menjadi pendorong utama attrition. Karyawan cenderung mencari peluang dengan kompensasi yang lebih baik jika merasa gajinya tidak sesuai dengan nilai atau kontribusi mereka.
- **Usia**: Karyawan yang lebih muda (terutama di awal karier) seringkali memiliki tingkat attrition yang lebih tinggi karena mereka aktif mencari pengalaman dan peluang baru, atau belum memiliki komitmen jangka panjang.
- **Status pernikahan**: Status pernikahan (misalnya, single atau divorced) dapat memengaruhi keputusan attrition, mungkin karena perbedaan tanggung jawab finansial atau kebutuhan akan stabilitas.

Selain itu, proyek ini juga menyertakan pengembangan Business Dashboard sebagai solusi analisis berkelanjutan, yang memungkinkan manajemen HR untuk memantau tren attrition dan faktor-faktor pendorongnya secara real-time dan visual.

### Rekomendasi Action Items (Optional)

1) **Fokus pada Karyawan Loyal dan Matang**: Saat rekrutmen, utamakan kandidat dengan riwayat kerja yang stabil (lama di perusahaan sebelumnya), usia yang lebih matang, dan kondisi pribadi yang stabil. Terutama untuk posisi penting seperti riset atau strategis.
2) **Ciptakan Lingkungan Kerja yang Seimbang**: Kurangi beban lembur. Data menunjukkan lembur berkontribusi besar terhadap keputusan karyawan untuk keluar. Budaya kerja yang menghargai work-life balance bisa menurunkan angka attrition.
3) **Perhatikan Kompensasi dan Kepuasan Karyawan**:Pendapatan yang terlalu rendah, atau tidak sesuai dengan pengalaman, bisa menjadi pemicu resign. Pertimbangkan review berkala terhadap struktur gaji dan kepuasan kerja.
