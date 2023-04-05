# Pistachio Formes Türkçe Doğal Dil İşleme Takımı  #acikhack2023

Türkçe Doğal Dil İşleme Yarışması için BERT Modeli - PyTorch

Bu projede, Türkçe Doğal Dil İşleme Yarışması için bir BERT modeli oluşturduk. PyTorch kütüphanesini kullanarak BERT modelini başarılı bir şekilde eğittik ve optimize ettik. Olabilecek en yüksek doğruluk ve performansı sağlamak için özenle seçilmiş verilerle çalıştık.

Projenin GitHub platformuna yüklenmesiyle birlikte, kullandığımız ekstra verileri "cleaned_data" klasöründe, eğitim modelini ise "train" adlı dosyada yayınlayacağız. 

## İçindekiler
- [Veri Seti](#veri-seti)
- [Veri Temizleme](#veri-temizleme)
- [Veri Bölme](#veri-bölme)
- [Tokenizasyon](#tokenizasyon)
- [Model Eğitimi](#model-eğitimi)
- [Fine-Tuning](#fine-tuning)
- [Model Testi](#model-testi)
- [Kullanım & Lisans](#kullanım-lisans)

## Veri Seti
Projede kullanılan Türkçe veri seti birkaç kaynaktan elde edilmiştir. Bu kaynaklar ana veri setimize eklenerek daha geniş ve kapsamlı bir veri seti oluşturulmuştur. . Bu sayede modelin geniş bir yelpazede metinleri daha etkili bir şekilde analiz etmesine ve sınıflandırmasına olanak tanıdık.

## Veri Temizleme
Veri seti üzerinde önemli bir temizleme süreci gerçekleştirdik. Regex kodumuzla verileri düzenledik ve modeli yanıltabilecek tüm veri kaynaklı sorunları ortadan kaldırdık. Bu temizleme işlemi, modelin doğru ve hassas tahminler yapmasına yardımcı oldu.

## Veri Bölme
Veri seti %80 eğitim ve %20 test olacak şekilde rastgele olarak ayrılmıştır. Bu yapı, modelin öğreneceği ve değerlendirileceği verilerin doğru bir dağılım içinde olmasını sağlar. Ayrıca daha sonraki süreçlerde modelin performansını değerlendirmeye ve optimize etmeye yardımcı oldu.

## Tokenizasyon
Eğitim verilerini ön işleyerek Multi-Language Tokenizer kullanarak tokinize ettik. Bu, BERT modelinin veriler üzerinde doğru bir şekilde çalışmasına ve metni etkili şekilde işlemesine yardımcı oldu. Bu işlem, metin verilerinin modelin anlamlandırabileceği ve öğrenebileceği tokenlere dönüştürülmesidir.

## Model Eğitimi
BERT modelini, girilen verilerin önce "is_offensive" ardından
"target" sütununu tahmin edecek şekilde multi-label text classification (çok etiketli metin sınıflandırma) şekline ayarladık. Bu, belge analizinde ve doğru sınıflandırma yapmada önemli bir adımdır. 
PyTorch kütüphanesini kullanarak, modelimizi başarılı bir şekilde tamamlayacak şekilde ayarladık ve BERT ile eğitim sürecini tamamladık. Bu, modelin daha sonraki testlerde ve gerçek zamanlı kullanımda yüksek doğruluk ve performans elde etmesini sağladı.

## Fine-Tuning
Eğitim süreci tamamlanmış olan BERT modeli, fine-tuning işlemine tabi tutularak daha iyi sonuçlara ulaşması amaçlanmıştır. Fine-tuning, modelin başlangıç öğrenme sürecinden sonra özelleştirilmesi adımıdır.

## Model Testi
Model, önceden ayrılan test veri seti ile doğruluk ve performans ölçümleri yapılarak değerlendirilmiştir. Bu adımdan sonra, model kullanıma hazır hale getirilmiştir.

## Kullanım & Lisans
Bu BERT modeli, Türkçe doğal dil işleme projelerinde kullanılmak üzere geliştirilmiştir. Özellikle sosyal medya verilerinin analizi ve sınıflandırılması gibi uygulamalarda yararlı olabilir. Modelin kullanımı oldukça basittir, sadece eğitilmiş modeli indirerek kullanabilirsiniz.
Bu proje, Türkçe doğal dil işleme alanında gelişim sağlamak için hazırlanmıştır. 
Şeffaf ve açıklayıcı bilgilerle paylaşılan bu modelin, sektördeki diğer araştırmacılara ve profesyonellere de fayda sağlaması ümidiyle.

#acikhack2023
