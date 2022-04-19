

Load Balancer 1 implemantasyonunda büyüme ve küçülme için bir yapı bulunmamaktadır.
Load Balancer 2'de implementasyon olarak yeni serverı da yük durumunda ekleme durumu eklenmiştir.

Her iki LB'da da Round Robin uygulanmıştır.

Load Balancer kendi içerisinde proxy barındırır fakat aşırı yük altında
LB durumunun da kontrol edilmesi gerekmektedir aksi halde çöker.

