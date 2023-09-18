# ihaWebApp

Bu proje, hem yerel geliştirme ortamında hem de Docker ortamında çalıştırılabilir.

Proje, aşağıdaki komutlarla başlatılabilir:
- Yerel ortamda: `python manage.py runserver` .Uygulama, varsayılan olarak http://127.0.0.1:8000/ adresinde çalışır.
- Docker ortamında: `docker-compose build` + `docker-compose up` .Uygulama, varsayılan olarak http://localhost:8000 adresinde çalışır.


Birim testleri şu komutlarla çalıştırabilirsiniz:
- iha uygulaması için: `python manage.py test iha`
- users uygulaması için: `python manage.py test users`

Projeyi kullanabilmek için öncelikle bir kullanıcı hesabı oluşturmanız gerekmektedir. Ardından oluşturduğunuz kullanıcı bilgileriyle giriş yapabilirsiniz. İHA ekranından yeni İHA'lar ekleyebilir ve eklenen İHA'lar ana sayfada listelenir. Ana sayfadan ilgili İHA'yı güncelleyebilir, silebilir veya kiralama işlemi yapabilirsiniz. Kiralama ekranında, tarih ve adet gibi detayları belirterek (bitiş tarihinin başlangıç tarihinden önce olduğundan emin olmalısınız) kiralama talebi oluşturabilirsiniz. Oluşturulan kiralama talepleri ana sayfada listelenir ve silinebilir. Kiralama Geçmişi sekmesinde ise kiralama işlemlerinin kayıtları tutulur.

## Kullanılan Teknolojiler

- Python
- Django
- Postgresql
- Rest Framework
- Docker
- DataTable
- HTML, CSS, JavaScript
- AJAX, Bootstrap, jQuery
- Django TestCase

## Proje Genel Bakışı

Bu Django projesi, insansız hava araçlarının (İHA) kiralama işlemlerini yönetmek için tasarlanmıştır. Proje iki ana Django uygulaması içerir:

### iha Uygulaması

- İHA'ların (insansız hava araçları) listesini görüntüleme
- İHA'ların özelliklerini görüntüleme
- Kiralama talebi oluşturma
- Kiralama geçmişini görüntüleme işlevselliği sağlar.

### users Uygulaması

- Kullanıcı kaydı, girişi ve çıkışını yönetir.

## Veritabanı Modelleri (Postgresql)

### iha Modeli

- İHA'ların temel özelliklerini saklar.
- İHA'nın markası, modeli, faydalı yük kapasitesi, havada kalma süresi, kanat açıklığı ve maksimum kalkış ağırlığı gibi özellikleri içerir.
- İHA görsel resimlerini depolamak için bir alan içerir.

### Kira Modeli

- İHA kiralama işlemlerini temsil eder.
- Başlangıç tarihi, başlangıç saati, bitiş tarihi, bitiş saati, kira adedi, kiralayan üye ve kiralanmış İHA gibi özellikleri içerir.
- Her bir kira işlemi, bir kullanıcı tarafından bir İHA için talep edilen bir kira işlemini temsil eder.

### RentalHistory Modeli

- Kiralama geçmişini kaydeder.
- Kiralanan İHA'nın başlangıç ve bitiş tarihleri, saatleri, kira adedi, kiralayan üye ve İHA gibi özellikleri içerir.

## Views (iha)

- **index:** İHA'ların listesini görüntüler ve kullanıcının kiralama geçmişini görüntüler. Kullanıcının oturum açmış olması gerekmektedir.
- **iha_view:** Belirli bir İHA'nın ayrıntılarını ve kiralamak için bir formu görüntüler. Kullanıcının oturum açmış olması gerekmektedir.
- **add_rental:** Bir İHA'yı kiralamak için bir form görüntüler ve kullanıcının formu doldurmasına izin verir. Kiralama işlemi başarıyla tamamlandığında, geçmişe eklenir ve ana sayfaya yönlendirilir.
- **cancel_rental:** Bir kiralama işlemini iptal eder.
- **rental_history:** Kullanıcının kiralama geçmişini görüntüler.
- **delete_rental_history:** Kullanıcının kiralama geçmişini temizler.
- **add_iha:** Yeni bir İHA ekler.
- **edit_iha:** Bir İHA'nın özelliklerini günceller.
- **delete_iha:** Bir İHA'yı siler (AJAX yardımıyla).

## Views (users)

- **index:** Kullanıcı bilgilerini görüntüler.
- **login_view:** Kullanıcı girişini kontrol eder.
- **logout_view:** Kullanıcı çıkışını kontrol eder.
- **register:** Kullanıcı kaydını sağlar.
