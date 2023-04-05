import pandas as pd   # 'pandas' kütüphanesi, verileri işlemek ve analiz etmek için kullanılır.
import re             # 're' kütüphanesi, düzenli ifadeleri kullanarak metin işleme işlemleri için kullanılır.

def clean_sentence(sentence):  # clean_sentence adlı bir fonksiyon tanımlanır ve sentence adında bir parametre alır.
    output_str = re.sub(r'[-,.&=?_<>|}#^;:£$½%*+/@]+', ' ', sentence).strip()  # sentence içindeki özel karakterler output_str içindeki özel karakterlerden temizlenir.
    output_str = re.sub(r'\s+', ' ', output_str)  # Ardışık boşluk karakterleri tek bir boşluk karakterine dönüştürülür.
    output_str = output_str.lower()  # Tüm karakterler küçük harfe dönüştürülür.
    return output_str  # İşlenmiş metin, output_str olarak döndürülür.
