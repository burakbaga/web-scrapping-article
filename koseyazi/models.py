from django.db import models
from bs4 import BeautifulSoup
import requests

class Hurriyet(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()

    def __str__(self):
        return self.baslik

while False:
    sayfa_yazarlar = requests.get("http://www.hurriyet.com.tr/yazarlar/")
    soup_yazarlar = BeautifulSoup(sayfa_yazarlar.content, "html.parser")
    kose_links1 = soup_yazarlar.find(class_="row a-row")
    kose_links = [i['href'] for i in kose_links1.select(".col-xs-4.author-box-title a")]

    for k in range(len(kose_links)):

        link = "http://www.hurriyet.com.tr" + kose_links[k]

        sayfa_kose_yazisi = requests.get(link)

        soup_kose_yazisi = BeautifulSoup(sayfa_kose_yazisi.content, "html.parser")

        hbaslik = soup_kose_yazisi.find(class_="article-title")

        article_content = soup_kose_yazisi.find(class_="article-content news-description")

        article_text = soup_kose_yazisi.find(class_="article-content news-text")

        hyazar = soup_kose_yazisi.find(class_="name")

        if article_text:
            hyazi = article_content.get_text() + article_text.get_text()

        else:
            continue

        h = Hurriyet(yazar=hyazar.get_text(), baslik=hbaslik.get_text(), yazi=hyazi)
        h.save()

class Milliyet(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()

    def __str__(self):
        return self.baslik

while False:
    yazarlar_sayfasi=requests.get("http://www.milliyet.com.tr/yazarlar/")

    soup_yazarlar=BeautifulSoup(yazarlar_sayfasi.content,'html.parser')

    kose=soup_yazarlar.find(class_="yList")

    soyazar=soup_yazarlar.find_all(class_="yName")

    sobaslik=soup_yazarlar.find_all(class_="yYazi")



    kose_linkler=["http://www.milliyet.com.tr"+i['href'] for i in kose.select(".yYazi a")]


    for j in range(len(kose_linkler)):

        myazar=soyazar[j].get_text()
        mbaslik=sobaslik[j].get_text()

        kose_sayfasi=requests.get(kose_linkler[j])

        soup_kose=BeautifulSoup(kose_sayfasi.content,'html.parser')

        paragraf=soup_kose.find_all('p')


        myazi=list()

        for x in range(len(paragraf)):
            myazi.append(paragraf[x].get_text())

        m = Milliyet(yazar=myazar, baslik=mbaslik, yazi=myazi)
        m.save()

class Cumhuriyet(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()

    def __str__(self):
        return self.baslik

while False:

    page_yazarlar = requests.get("http://www.cumhuriyet.com.tr/BugununKoseleri")
    csoup = BeautifulSoup(page_yazarlar.content, 'html.parser')
    print(page_yazarlar.status_code)
    koseler = csoup.find(id="gunun-yazarlari")
    cyazar = [i for i in koseler.select('.author a')]
    link_yazi=list()


    for i in range(len(cyazar)):


        link_yazi.append("http://www.cumhuriyet.com.tr" + cyazar[i]['href'])

        page_kose_yazisi = requests.get(link_yazi[i])

        soup2 = BeautifulSoup(page_kose_yazisi.content, "html.parser")

        cyazi = soup2.find(id="article-body")

        cbaslik=soup2.find(id="article-title")


        c = Cumhuriyet(yazar=cyazar[i].get_text(), baslik=cbaslik.get_text(), yazi=cyazi.get_text())
        c.save()



class Birgun(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()

    def __str__(self):
        return self.baslik

while False:


    page=requests.get("https://www.birgun.net/yazarlar")
    soup=BeautifulSoup(page.content,'html.parser')

    koseler=soup.find(class_="td_block_inner td-mc1-wrap")
    kose_link=[i for i in koseler.select(".td-module-meta-info .entry-title.td-module-title a")]



    for i in range(len(kose_link)):

        kosere=requests.get(kose_link[i]['href'])

        soup2=BeautifulSoup(kosere.content,'html.parser')

        byazar=soup2.find(class_="tdb-author-name")

        bbaslik=soup2.find(class_="tdb-title-text")

        kose_yazi = soup2.find_all('p')
        byazi=list()
        for j in range(len(kose_yazi)):
            byazi.append(kose_yazi[j].get_text())

        b = Birgun(yazar=byazar.get_text(), baslik=bbaslik.get_text(), yazi=byazi)
        b.save()