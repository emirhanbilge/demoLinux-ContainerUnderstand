
Pod similasyonu olarak aslında çok basit düzeyde webserverlar ayağa kaldırıyorum.
Bu web serverlar socket servera dönüştürülmesi yük altındaki ölçümlerde daha başarılı sonuç verir.

Burada podların yük altında olup olmadığı basit düzeyde CPU kullanımı ile ölçülmeye çalışılmıştır

Her bir podu sınırlama ve özelleştirme için /proc/pidNumber/ ve içerisinde limits dosyası configure edilerek sınırlanabilir