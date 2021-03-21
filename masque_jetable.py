#! /usr/bin/python
 
import binascii
 
#Code pour le principe
#a = input("saisir un mot: ")
#print a
#b = bin(int(binascii.hexlify(a))) #on convertie en binaire
#print b
#c = binascii.unhexlify(str(int(b, 2))) #on convertie en string hexa
#print c
 
#test effectue avec test/hell
#probleme si message et cle ont une taille differente
 
 
def ascii_to_binaire(chaine):
	"""
                Fonction permettant de convertir une chaine en binaire
        """
	binaire=bin(int(binascii.hexlify(chaine),16))
	return binaire  #chaine contient la conversion de mot en binaire
 
 
 
 
def binaire_to_ascii(binaire):
	"""
                Fonction permettant de convertir un binaire en chaine
        """
	tmp = "%X" % (int(binaire,2)) #creation d'un hexstring
	chaine=binascii.unhexlify(tmp)
	return chaine #chaine contient la conversion de mot en binaire
 
 
 
 
def encode(motbin,clebin):
	"""
                Fonction permettant de coder une chaine grace a une cle
                selon l'algorithme de masque jetable
        """
	chaine = "" #chaine est a declarer avant a cause du +=
	result = "" #idem
 
	mot_tmp = motbin.split('b')[1]
	cle_tmp = clebin.split('b')[1]
 
	for k in range (len(mot_tmp)): #probleme en fonction de la taille du message
		chaine+=str(int(mot_tmp[k],2) ^ int(cle_tmp[k],2)) # !!! probleme si taille differente !!!
		result+=str(int(chaine[k])%26)
 
	return result
 
 
 
 
def decode (motbin,clebin):
	"""
                Fonction permettant de decoder une chaine grace a une cle
                selon l'algorithme de masque jetable
        """
	chaine = "" #chaine est a declarer avant a cause du +=
	result = "" #idem
 
	mot_tmp = motbin
	cle_tmp = clebin.split('b')[1]
 
 
	for k in range (len(mot_tmp)): #probleme en fonction de la taille du message
		chaine+=str(int(mot_tmp[k],2) ^ int(cle_tmp[k],2)) # !!! probleme si taille differente !!!
		result+=str(int(chaine[k])%26)
 
	return result




if __name__ == "__main__":
	"""
                Fonction principale du module PYTHON
                    1-Selection de l'operation
                    2-Saisie du message et de la cle (encoder ou non) ou sortie
                    3-Recuperation du message encode ou non
        """
	choix = input("Desirez vous encoder(e) ou decoder(d) un message?")
	while choix.upper() not in ("Q", "D", "E"):
		choix = input("Desirez vous encoder(e) ou decoder(d) un message (quitter:q)?")

	if choix.upper() == "E":
		mot = input("Entrer votre message:")
		cle = input("Entrer la cle:")
 
		motbin= ascii_to_binaire(mot)
		clebin= ascii_to_binaire(cle)
		result = encode(motbin,clebin)
 
		print("Le message chiffre est: ", result)
 
	elif choix.upper() == "D":
		motbin = input("Entrer votre message:")
		cle = input("Entrer la cle:")

		clebin= ascii_to_binaire(cle)
		result_tmp = decode(motbin,clebin)
		result = binaire_to_ascii('0b'+result_tmp)
 
		print("Le message dechiffre est: ", result)
 
	else:
		print("Au revoir...")