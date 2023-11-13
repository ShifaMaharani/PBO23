#BALOK
def luas_balok(panjang,lebar,tinggi):
    L=(2*(panjang*lebar)+2*(panjang*tinggi)+2*(lebar*tinggi),2)
    return L
def volume_balok(panjang,lebar,tinggi):
    VB=panjang*lebar*tinggi
    return VB
#BOLA
def luas_bola (jari_jari):
    LBOLA= (4 * 3.14 * jari_jari ** 2 )
    return LBOLA
def volume_bola (jari_jari ):
    VBOLA=(4/3 * 3.14 * jari_jari ** 3)
    return VBOLA
#KERUCUT
def luas_selimutkerucut (jarijari, sisi, tinggi ):
    LSK=3.14*jarijari*sisi
    return LSK
def luas_permukaankerucut (jarijari, sisi, tinggi ):
    LPK=3.14*jarijari*sisi
    return LPK
def volume_kerucut  (jarijari, sisi, tinggi ):
    VK=1/3*3.14*jarijari**2*tinggi
    return VK
#kubus
def luas_kubus (R):
    LKUBUS=6 * R
    return LKUBUS
def volume_kubus (R):
    VKUBUS= R*R*R
    return VKUBUS
#limas segi empat
def luas_segiempat (tinggilimas,sisi, tinggisegitiga):
    LLSEGIEMPAT=(sisi*sisi)+(4*sisi*tinggisegitiga/2)
    return LLSEGIEMPAT
def volume_segiempat (tinggilimas,sisi, tinggisegitiga):
    VLSEGIEMPAT=1/3*(sisi*sisi)*tinggilimas
    return VLSEGIEMPAT
#limas segitiga
def luas_limassegitiga (alassegitiga, tinggilimas, tinggisegitiga):
    LLSEGITIGA =4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return LLSEGITIGA
def volume_limassegitiga(alassegitiga, tinggilimas, tinggisegitiga):
    VLSEGITIGA = 1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return VLSEGITIGA
#prisma segitiga
def luas_prismasegitiga (alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    LALASPRISMAS = (sisi1 + sisi2 + sisi3) * tinggiprisma
    return LALASPRISMAS 
def luas_sisi(alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    LSISIPRISMAS = (sisi1 + sisi2 + sisi3) * tinggiprisma + alas * tinggi
    return LSISIPRISMAS 
def volume_prismasegitiga(alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    VPRISMASEGI = (alas * tinggi) / 2 * tinggiprisma
    return VPRISMASEGI
    #silinder
def luas_selimut (jarijari, tinggi):
    LSSILINDER=2*3.14*jarijari*tinggi
    return LSSILINDER
def luas_permukaan (jarijari, tinggi):
    LPSILINDER=2*3.14*jarijari*tinggi+2*3.14*jarijari**2
    return LPSILINDER
def volume_silinder(jarijari, tinggi):
    VSILINDER=3.14*jarijari**2*tinggi
    return VSILINDER
#persegi panjang
def luas_persegip (p,l,t):
    LPSEGI=(2*p*l) + (2*p*t) + (2*l*t)
    return LPSEGI
def volume_persegip (p,l,t):
    VPERSEGI=p*l*t 
    return VPERSEGI


