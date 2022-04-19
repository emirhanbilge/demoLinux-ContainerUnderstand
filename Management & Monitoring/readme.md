


cpuusage.sh :

Buradaki cpu usage ile aslında basit ve temel linux kodlarını pipelinelar ile birleştirerek istediklerimizi ne kadar rahat elde ettiğimizi görüyoruz.
Burada cpu usage kontrol ederek karar vermemize olanak verebilmektedir.

instanceWriter.sh: 
    Burada pod sayımızı arttırıp azaltmak için kullanıcağımız bilgileri yazmak için
    Podların canlı mı yoksa kapanmış mı olduklarını process idlerinden takip edebiliriz.
    Bu amaçla pidleri çekilerek bilgi elde ediyoruz


genericserver: 
    Yeni pod ayağa kaldıracğımız sırada port sayısını alarak onun oluşması lazımdır
    bu amaçla tek parametre alan ve o da port numarası olan instance oluşturucudur


demoContandLinuxManagerandMonitoring:
    Podların sayısını bilgisini kontrol eden yapıdır
    Sistemin durumu hakkında bilgi verir
