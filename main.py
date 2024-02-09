import pandas as pd
import time
import os


file = "C:/Users/gokhan.kaya/OneDrive - Aster Textile/Desktop/BELGELERİM/BANKA TRANSFER/2024/"
ödeme_tarihi = input("Lütfen ödeme tarihini giriniz...:")



def odeme_list(file, ödeme_tarihi):
    odemeler = ödeme_tarihi.split(",")
    txt_liste = list()
    for i in odemeler:
            txt_liste.append(i)
    return print(txt_liste)


odeme_list(file, ödeme_tarihi)



#
# path = "TEKSTIL_2023 Aralık Ayı %100 fm Ödemesi.txt"
#
# def data_frame(path):
#
#     data =  pd.read_csv(path, encoding='ISO-8859-1', sep=";")
#     liste = []
#     for i in range(len(data)-1):
#         liste.append([data.columns[0][30:38].strip(), data.columns[0][15:27].strip(),
#                       data.iloc[i,0][2:6].strip(), data.iloc[i,0][6:13].strip(),
#                         data.iloc[i,0][13:39].strip(), float(data.iloc[i,0][39:54].strip()),
#                             data.iloc[i,0][54:79].strip(), data.iloc[i,0][79:109].strip(),
#                                 data.iloc[i,0][109:120].strip()])
#     df = pd.DataFrame(data=liste, columns=["ÖdemeTarihi", "FirmaKodu", "Şube", "Hesap", "IBAN", "Tutar", "AdSoyad", "Açıklama", "TcNo"])
#
#     return df
#
#
# print(sum(data_frame(path)["Tutar"]))
#
