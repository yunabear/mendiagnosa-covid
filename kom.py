# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Modul ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from colorama import Fore, Style
from datetime import datetime
import os
now = datetime.now()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Data Gejala dan Penyakit ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
gejala = {
    "demam" : "1. Demam (suhu tubuh di atas 38 derajat Celsius)", 
    "batuk" : "2. Batuk", 
    "sesak" : "3. Sesak Nafas ", 
    "kelelahan" : "4. Kelelahan", 
    "pegal" : "5. Pegal-Pegal", 
    "tdk_nfsu" : "6. Tidak Nafsu Makan", 
    "hilang_indra" : "7. Kehilangan Indra Penciuman dan Rasa", 
    "bingung" : "8. Keadaan Bingung / Melamun Sesaat", 
    "pusing" : "9. Sakit Kepala dan Pusing",
    "kejang": "10. Kejang-Kejang", 
    "diare" : "11. Diare dan Mual", 
    "dingin" :"12. Rasa Kedinginan / Menggigil", 
    "terbakar" : "13. Kulit terasa terbakar / Tersengat Listrik"
}
penyakit = {
    "flu" : "Menurut diagnosa Anda Terkena Penyakit Flu",
    "covid" : "Menurut diagnosa Anda positif virus Corona (COVID-19)",
    "pneunomia" : "Menurut diagnosa Anda Terkena Radang paru-paru (pneunomia)",
    "kejang_demam" : "Menurut diagnosa Anda mengalami penyakit Kejang Demam",
    "ayan" : "Menurut diagnosa Anda mengalami penyakit ayan",
    "diare" : "Menurut Diagnosa Anda Mengalami Penyakit Diare",
    "migrain" : "Menurut Diagnosa Anda Mengalami Penyakit Migrain",
    "asam_urat" : "Menurut Diagnosa Anda Mengalami Penyakit Asam Urat",
    "gagal_jantung" : "Menurut Diagnosa Kemungkinan Anda Mengalami Gejala Gagal Jantung",
    "kanker" : "Menurut Diagnosa Anda kemungkinan terkena kanker paru-paru",
    "asma" : "Menurut Diagnosa Anda Kemungkinan terkena penyakit Asma",
    "anemia" : "Menurut hasil dari diagnosa. Anda Mengalami Penyakit Anemia",
    "sinusitis" : "Menurut hasil dari diagnosa. Anda Mengalami Penyakit Sinusitis",
    "TBC" : "Menurut hasil dari diagnosa. Anda Mengalami Penyakit Tuberkulosis",
    "g_tipes" : "Menurut Hasil dari Diagnosa, Anda Mengalami gejala tipes",
    "demam" : "Menurut Hasil dari diagnosa, Anda mengalami demam",
    "batuk" : "Menurut hasil dari diagnosa, Anda mengalami batuk",
    "pegal" : "Menurut Hasil dari diagnosa, Anda mengalami pegal linu",
    "maag" : "Menurut Diagnosa, Anda Terkena Maag",
    "anosmia" : "Menurut Diagnosa, Anda Terkena Anosmia"
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Opening Program ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print(Fore.GREEN +"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("|\t                                                                                  |")
print("|\tHalo, Selamat datang di Program Mendiagnosa Penyakit COVID-19 dengan Gejala       |")
print("|\t                                                                                  |")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print("Apakah Anda Ingin Melakukan Test?                              ")
pilihan = input("Jawab [y/t]: ")
os.system("cls")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Looping ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
while pilihan == "y":
    deco = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    nama = input(Fore.CYAN+"Masukan Nama Anda : ")
    usia = int(input("Masukan Usia Anda : "))
    jenis = input("Jenis Kelamin [l/p] : ")
    if jenis == "p" or jenis == "P":
        wanita_h = input("Apakah Anda sedang hamil? [y/t] : ")
    riwayat = input("Apakah anda memiliki riwayat penyakit kronis? [y/t]: ")
    perokok = input("Apakah Anda seorang perokok? [y/t] : ")
    os.system("cls")
    print(Fore.BLUE+"Apakah Anda Memiliki Gejala-Gejala Berikut?")
    print(gejala["demam"])
    d1 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["batuk"])
    d2 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["sesak"])
    d3 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["kelelahan"])
    d4 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["pegal"])
    d5 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["tdk_nfsu"])
    d6 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["hilang_indra"])
    d7 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["bingung"])
    d8 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["pusing"])
    d9 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["kejang"])
    d10 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["diare"])
    d11 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["dingin"])
    d12 = input("Jawab [y/t]: ")
    os.system("cls")
    print(gejala["terbakar"])
    d13 = input("Jawab [y/t]: ")
    os.system("cls")
    print()
    os.system("cls")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Biodata ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    DA = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]
    print(Fore.CYAN+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    current_time = now.strftime("%H:%M:%S")
    print("Waktu            : ",current_time+"")
    print("Nama             : ",nama)
    print("Usia             : ",usia)
    if jenis == "l" or jenis == "L":
        print("Jenis Kelamin    :  Laki-Laki")
    elif jenis == "p" or jenis == "P":
        print("Jenis Kelamin    :  Perempuan")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Hasil Gejala ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("|Gejala yang Anda Alami :                                                              |")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("|"+gejala["demam"] + " : " + (DA[0])+"|".center(70))
    print("|"+gejala["batuk"] + " : " + (DA[1])+"|".center(149))
    print("|"+gejala["sesak"] + " : " + (DA[2])+"|".center(135))
    print("|"+gejala["kelelahan"] + " : " + (DA[3])+"|".center(142))
    print("|"+gejala["pegal"] + " : " + (DA[4])+"|".center(138))
    print("|"+gejala["tdk_nfsu"] + " : " + (DA[5])+"|".center(126))
    print("|"+gejala["hilang_indra"] + " : " + (DA[6])+"|".center(90))
    print("|"+gejala["bingung"] + " : " + (DA[7])+"|".center(95))
    print("|"+gejala["pusing"] + " : " + (DA[8])+"|".center(113))
    print("|"+gejala["kejang"] + " : " + (DA[9])+"|".center(132))
    print("|"+gejala["diare"] + " : " + (DA[10])+"|".center(130))
    print("|"+gejala["dingin"]+ " : " + (DA[11])+"|".center(103))
    print("|"+gejala["terbakar"] + " : " + (DA[12])+"|".center(75))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Hasil diagnosa ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if DA == ["y","y","y","y","y","y","y","y","y","y","y","y","y"] or DA == ["y","y","y","y","y","y","y","y","y","y","y","y","t"] or DA == ["y","y","y","y","y","y","y","y","y","y","t","y","t"] or DA == ["y","y","y","y","y","y","y","y","y","t","t","y","t"] or DA == ["y","y","y","y","y","y","y","y","y","y","t","y","y"]:
        print(penyakit["covid"])
        print()
        print("Solusi : Segera melakukan swab test di rumah sakit terdekat")
    elif DA == ["y","y","t","t","y","t","t","t","t","t","t","y","t"] or DA == ["y","y","t","t","t","t","t","t","t","t","t","y","t"] or DA == ["y","y","t","t","t","y","t","t","t","t","t","y","t"] or DA == ["y","y","t","y","t","t","t","t","t","t","t","y","t"] or DA == ["y","y","y","t","t","t","t","t","y","t","t","y","t"]:
        print(penyakit["flu"])
        print()
        print("Solusi : Segera pergi ke dokter untuk di periksa dan ambil resep obat dari dokter")
    elif DA == ["y","y","y","t","t","y","t","t","t","t","t","y","t"] or DA == ["y","y","y","t","t","y","t","t","t","t","t","t","t"] or DA == ["y","y","t","t","t","y","t","t","t","t","t","t","t"] or DA == ["y","y","y","y","t","y","t","t","t","t","y","y","t"] or DA == ["y","y","t","y","t","y","t","t","t","t","t","t","t"]:
        print(penyakit["pneunomia"])
        print()
        print("Solusi : Minum Teh herbal dan perbanyak minum air hangat atau jika terasa parah segera berobat ke dokter")
    elif DA == ["y","t","t","t","t","t","t","t","y","t","y","t","t"] or DA == ["y","t","t","t","t","t","t","t","y","t","t","t","t"]:
        if usia <= 5:
            print(penyakit["kejang_demam"])
            print()
            print("Solusi : Letakkan anak di tempat yang datar. Tempat tersebut sebaiknya luas dan bebas,")
            print("sehingga anak tidak akan terbentur atau tertimpa benda tertentu saat kejang.")
            print("Posisikan anak tidur menyamping, untuk mencegahnya tersedak saat kejang")
        else:
            print(penyakit["kejang_demam"])
            print()
            print("Solusi : Segera pergi ke rumah sakit untuk berobat")
    elif DA == ["t","t","y","t","t","t","t","t","t","y","t","t","t"] or DA == ["t","t","y","y","t","t","t","t","t","y","t","t","t"] or DA == ["t","t","t","y","t","t","y","t","t","y","t","t","t"] or DA == ["t","t","y","y","t","t","y","t","t","y","t","t","t"]:
        print(penyakit["ayan"])
        print()
        print("Solusi : Minum Air kelapa, susu, jus buah atau air putih")
    elif DA == ["y","t","t","t","t","y","t","t","t","t","y","t","t"] or DA == ["t","t","t","t","t","t","t","t","t","t","y","t","t"] :
        print(penyakit["diare"])
        print()
        print("Solusi : Minum Air putih untuk menambah asupan cairan, dan menjaga pola makan yang baik")
    elif DA == ["y","t","t","t","t","t","t","t","y","t","y","y","t"] or DA == ["t","t","t","t","t","t","t","t","y","t","y","y","t"] or DA == ["y","t","t","t","t","t","t","t","t","t","y","y","t"] or DA == ["t","t","t","t","t","t","t","t","y","t","y","t","t"]:
        print(penyakit["migrain"])
        print()
        print("Solusi : Minum obat acetaminophen dan aspirin atau ibu profen")
    elif DA == ["t","t","t","t","y","t","t","t","t","t","t","t","y"] :
        print(penyakit["asam_urat"])
        print()
        print("Solusi : Segera minum obat asam urat dari dokter, selalu pantau kadar asam urat anda dan rajin melakukan olahraga secara teratur")
    elif DA == ["t","t","y","y","t","y","t","t","y","t","t","t","t"] :
        print(penyakit["gagal_jantung"])
        print()
        print("Solusi : Menjalani gaya hidup sehat merupakan tindakan paling efektif dalam mencegah gagal jantung"/
        +"Seperti Konsumsi makanan sehat dan bergizi seimbang dan Lakukan pemeriksaan tekanan darah, serta kadar gula dan kolesterol darah secara berkala")
    elif DA == ["t","y","y","y","t","y","t","t","t","t","t","t","t"] or DA == ["t","y","y","t","t","t","t","t","t","t","t","t","t"] or DA == ["t","t","y","t","t","t","t","t","t","t","t","t","t"]:
        if riwayat == "t":
            if perokok == "y":
                print(penyakit["kanker"])
                print()
                print("Solusi : Berhenti Merokok. dan segera melakukan kemoterapi")
            elif perokok == "t":
                print(penyakit["kanker"])
                print()
                print("Solusi : Hindari Asap Rokok, Polusi dan bahan kimia seperti asbes dan radon ")
        elif riwayat == "y":
            if perokok == "y":
                print(penyakit["asma"])
                print()
                print("Solusi : Berhenti Merokok. dan segera melakukan pengecekan ke dokter sebelum melakukan terapi oksigen")
            elif perokok == "t":
                if usia <=5 :
                    print(penyakit["asma"])
                    print()
                    print("Solusi : Melakukan Terapi Oksigen dan pergi ke dokter untuk melakukan pengecekan lebih lanjut"
                    + "untuk mendapatkan obat dari dokter")
                else:
                    print(penyakit["asma"])
                    print()
                    print("Solusi : Melakukan Akupuntur dan Terapi pernapasan")
    elif DA == ["t","t","y","y","t","t","t","t","y","t","y","y","t"] :
        print(penyakit["anemia"])
        if wanita_h == "y":
            print("Solusi : Makan makanan bernutrisi khusus (Daging (sapi atau unggas) rendah lemak yang dimasak matang"
                +"Makanan laut seperti ikan, cumi, kerang, dan udang yang dimasak matang, Telur yang dimasak matang ,Sayuran hijau, misalnya bayam dan kangkung"
                +"Kacang polong, Produk susu yang telah dipasteurisasi, Kentang, dan Gandum)"
                +"Minum Suplemen") 
        elif wanita_h == "t": 
            print()
            print("Solusi : Periksakan diri Anda ke dokter apabila merasa cepat lelah atau mengalami gejala anemia yang makin lama makin memburuk.")
    elif DA == ["y","y","t","y","t","t","t","t","t","t","t","t","t"] :
        print(penyakit["sinusitis"])
        print()
        print("Solusi : Anda disarankan untuk berkosultasi dengan dokter jika mengalami gejala sinusitis."/
        +"Dokter biasanya akan melakukan pemeriksaan lanjutan jika Anda diduga menderita sinusitis.")
    elif DA == ["y","y","y","y","t","y","t","t","t","t","t","t","t"] :
        print(penyakit["TBC"])
        print()
        print("Solusi : Prinsip utama pengobatan TBC (tuberkulosis) adalah patuh untuk minum obat selama jangka waktu yang dianjurkan oleh dokter (minimal 6 bulan).")
    elif DA == ["y","y","t","y","t","t","t","t","y","t","t","t","t"] or DA == ["y","t","t","y","y","t","t","t","y","t","t","t","t"]:
        print(penyakit["g_tipes"])
        print()
        print("Solusi : Istirahat yang cukup dan jangan melakukan pekerjaan yang berat")
    elif DA == ["y","t","t","t","t","t","t","t","t","t","t","t","t"] or DA == ["y","y","t","t","t","t","t","t","t","t","t","t","t"]:
        print(penyakit["demam"])
        print("Solusi : Kompres dengan air hangat, gunakan pakaian tipis dan nyaman")
    elif DA == ["t","y","t","t","t","t","t","t","t","t","t","t","t"]:
        print(penyakit["batuk"])
        print()
        print("Solusi : Meminum campuran air jeruk lemon dengan madu")
    elif DA == ["t","t","t","y","y","t","t","t","t","t","t","t","t"]:
        print(penyakit["pegal"])
        print()
        print("Solusi : Melakukan Peregangan otot dan Kompres atau berendam air hangat")
    elif DA == ["t","t","t","y","t","t","t","t","t","t","t","t","t"] or DA == ["t","t","t","t","y","t","t","t","t","t","t","t","t"]:
        print("Menurut hasil diagnosa, Mungkin Anda Banyak Pekerjaan atau Tugas dan tidur yang tak teratur")
        print()
        print("Solusi : Istirahat yang cukup dan tidur yang teratur")
    elif DA == ["t","t","t","t","t","y","t","t","t","t","t","t","t"] :
        if usia >=60 :
            print("Menurut diagnosa, anda kehilangkan nafsu makan karena faktor penuaan")
            print()
            print("Solusi : Makan makanan yang lunak atau cair dan juga mengandung tinggi protein dan karbohidrat kompleks")
        else:
            print(penyakit["maag"])
            print()
            print("Solusi : Batasi konsumsi makanan pedas, asam, dan berlemak dan jangan langsung rebahan setelah makan")
    elif DA == ["t","t","t","t","t","t","y","t","t","t","t","t","t"] :
        print(penyakit["anosmia"])
        print()
        print("Solusi : Memberikan Antibiotik dan anosmia dapat terdeteksi Virus COVID-19 maka segera melakukan Swab test dan PCR")
    elif DA == ["t","t","t","t","t","t","t","t","t","t","t","t","t"] :
        print("Hasil : Mungkin Anda Butuh Liburan")
    else:
        print("Hasil : Mungkin anda terkena penyakit ringan, Segera Periksa Ke Dokter")


    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Test Ulang ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Style.RESET_ALL)
    print("Apakah Anda Ingin Melakukan Test Kembali?")
    kembali = input("Jawab [y/t]: ")
    print()
    os.system("cls")
    if kembali == "y":
        continue
    elif kembali == "t":
        print()
        print("Terima Kasih!, " + nama)
        print()
        break
    else:
        break
else:
    print("Sampai Jumpa Lagi!")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Akhir Program ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━