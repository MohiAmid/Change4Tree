import openfoodfacts
#print(brands)

import csv
import urllib2

url = 'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response,delimiter='\t')
#print(list(cr)[1][0])
#print(len(list(cr)))
#1 733 980

data = {7622210449283:'D',3229820129488:'B',3501890002152:'E',8001505005592:'C',7613035040823:'E',5410188031072:'C',7622210601988:'D',7622210713889:'C',3366321052331:'B',7300400481571:'A'}

def get_qualitearticle(ecoscore):

    if ecoscore=='A'| ecoscore=='B':
        print('Votre produit est respecteux de l\'environnemnt')
    else:
        print('Votre produit a un mauvaise impact sur l\'environnement')
        prixenplus=input('')
'''
def verifiercodebarre(codebarre):
    for article in range(1,len(list(cr))):
        print(list(cr)[article][0])
        if codebarre==list(cr)[article][0]:
            print('Le produit existe, nous allons verifier s\'il est respectuex de l\'environnement.')
            return 1
        else:
            print('Le produit n\'existe pas dans notre base.')
            return 0
#verifiercodebarre('3017620420009')
'''
def verifiercodebarre(codebarre):
        if codebarre in data.keys():
            print('Le produit existe, nous allons verifier s\'il est respectuex de l\'environnement.')
            return 1
        else:
            print('Le produit n\'existe pas dans notre base.')
            return 0


print('Bonjour, avez-vous effectue des achats ?')
print('1-oui')
print('2-non')
cpt=0
reponsebienvenue=input('')
if reponsebienvenue==1:
    print('Combien d\'articles avez-vous achetes ?')
    reponsearticle=input('')
    if reponsearticle>=1:
        print('Veuillez scanner les codes-barres des '+str(reponsearticle)+' articles.')
        list_cb=[]
        list_result=[]
        for cb in range(0,reponsearticle):
            cb=input('')
            list_cb.append(cb)
        for cb in list_cb:
            result=verifiercodebarre(int(cb))
            list_result.append(result)
        for i in list_result:
            cpt+=1
            if i==1:
                score=data[0]
                print(score)
            
    else: 
        if reponsearticle==0:
            print('Le nombre d\'article doit etre superieur ou egale a 1')
            
            
else:
    print('Voulez-vous scanner un article ?')
    print('1-oui')
    print('2-non')
    reponsescanner=input('')
    if reponsescanner==1:
        print('Combien de produits voulez-vous enregistrer ?')
        reponsearticle2=input('')
        if reponsearticle2>1:
            print('Veuillez scanner vos '+str(reponsearticle2)+' articles.')
        else:
            if reponsearticle2==1:
                print('Veuillez scanner votre article.')
            else:
                print('Le nombre de produit doit etre egale ou superieur a 1')
    else:
         print('Merci d\'avoir repondu, revenez lorsque que vous voudrez scanner des articles !')
