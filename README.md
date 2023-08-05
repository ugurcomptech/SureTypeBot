# SureTypeBot

SureTypeBot, belirli bir yazma hızı testi sitesindeki kelimeleri otomatik olarak algılayan ve Selenium'u kullanarak daha hızlı bir şekilde yazan bir Python betiğidir.

## Gereksinimler

- Python 3.x
- Selenium kütüphanesi (`pip install selenium`)
- Google Chrome tarayıcısı
- Google Chrome Driver (https://sites.google.com/a/chromium.org/chromedriver/downloads)


## Kurulum

1. Sisteminizde Python yüklü olmalıdır. Python'u indirmek için https://www.python.org/downloads/ adresini ziyaret edebilirsiniz.

2. Projeyi çalıştırmak için gerekli kütüphaneleri yüklemek için aşağıdaki komutu terminalde çalıştırın:

 ```Python
  pip install -r requirements.txt
   ```

## Nasıl Çalışır?

1. Sisteminizde Python yüklü olduğundan ve `selenium` kütüphanesinin yüklendiğinden emin olun (kurulum için `pip install selenium` komutunu kullanabilirsiniz).

2. Sisteminizde Google Chrome tarayıcısının yüklü olduğundan ve Google Chrome Driver'ın indirilip PATH'e eklediğinizden emin olun.

3. `bot_hizli_yaz.py` adlı Python betiğini indirin veya oluşturun.

4. Terminal veya Komut İstemi'ni açın ve dosya dizinini çalışma dizini olarak ayarlayın.

5. Betiği çalıştırın:

```Python
python app.py
```

6. Chrome tarayıcı açılacak ve belirtilen yazma hızı testi sitesine girecektir.

7. Site yüklendikten sonra, bot kelimeleri otomatik olarak algılayacak ve daha hızlı bir şekilde yazmaya başlayacaktır.

8. Bot yazmayı tamamladığında, terminalden çıkmak için herhangi bir tuşa basın.

**Not:** Yazma hızını `time.sleep()` süresini değiştirerek ayarlayabilirsiniz. Ancak, çok hızlı yazma siteye cevap verememesine veya botun doğru çalışmamasına neden olabilir. Dikkatli olun.

## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.


