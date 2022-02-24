import copy

bus = {
	"immtriculation" : "aucun",
	"nbrePlace" : 0,
	"nbrePlaceDispo" : 0,
	"capaciteKgTotal" : 0.0,
	"capaciteKgDispo" : 0.0,
	"listePassagers" : []
}

passager = {
	"cni" : "aucun",
	"nomEtPrenom" : "aucun",
	"poidsBagages" : 0.0,
	"numPhone" : "aucun"
}

listeBusFlotte = []
listePassagerFlotte = []


#Fonctions relatives à la gestion des bus 
def verifierExistanceBus(immatriculation_b):
	#Vérifie si un bus existe déjà
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			return True
		else:
			return False

def verifierSiBusPlein(immatriculation_b):
	#Verifier si un bus a encore des places libres
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			if bus["nbrePlaceDispo"] > 0:
				return False
			else:
				return True

def verifierEspaceBagageSuffisant(immatriculation_b, poidsBagages_p):
	#Verifier si la soute à bagage du bus peut recevoir les bagages d'un passager
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			if bus["capaciteKgDispo"] >= poidsBagages_p:
				return True
			else:
				return False

def creerBus():
	#Creation de bus
	bus_p = copy.deepcopy(bus)
	bus_p["immtriculation"]=input("Entrer le numéro d'immatriculation du bus: ")
	bus_p["nbrePlace"]=int(input("Entrer le nombre de places maximal du bus: "))
	bus_p["nbrePlaceDispo"]=bus_p["nbrePlace"]
	bus_p["capaciteKgTotal"]=float(input("Entrer la capacité maximale en kg de bagages de ce bus: "))
	bus_p["capaciteKgDispo"]=bus_p["capaciteKgTotal"]
	listeBusFlotte.append(bus_p)

def getNbrePlaceDispoBus(immatriculation_b):
	#Renvoie le nombre de places disponible dans un bus
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			return bus["nbrePlaceDispo"]

def getNbreKgDispoBus(immatriculation_b):
	#Renvoie le nombre de Kilogrammes disponible dans un bus
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			return bus["capaciteKgDispo"]

def verifierTransfertBus(imm_bus_depart, imm_bus_destination):
	pass
	#verifier le nombre de place dispo
	#verifier les bagages

def peutAccueillirPassager(cni_p, poidsBagages, immatriculation_b):
	pass
	#verifier le nombre de place dispo
	#verifier les bagages

def deplacerPassager(imm_bus_depart, imm_bus_destination):
	pass


def getListePassagerBus(immatriculation_b):
	pass
	#afficher la liste des passagers d'un bus et leur infos

def verifierPassagerDansBus(cni_p, immatriculation_b):
	#Verifier l'existance d'un passager dans un bus
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			for passager in bus["listePassagers"]:
				if passager["cni"] == cni_p:
					return True
				else:
					return False
		else:
			return False


#Fonctions relatives à la gestion des passagers
def verifierExistancePassager(cni_p):
	#Vérifie si un passager existe déjà
	for passager in listePassagerFlotte:
		if passager["cni"] == cni_p:
			return True
		else:
			return False

def enregistrerPassager():
	#verifier que le passager n'existe pas déjà
	passager_p = copy.deepcopy(passager)
	passager_p["cni"]=input("Entrer le numéro de la CNI du passager: ")
	passager_p["nomEtPrenom"]=input("Entrer le nom et le prénom du passager: ")
	passager_p["poidsBagages"]=float(input("Entrer le poids des bagages du passager en Kg: "))
	passager_p["numPhone"]=input("Entrer le numéro de téléphone du passager: ")
	listePassagerFlotte.append(passager_p)


def ajouterPassagerBus(cni_p, imm_bus_destination):
	for passager in listePassagerFlotte:
		if passager["cni"] == cni_p:
			for bus in listeBusFlotte:
				if bus["immtriculation"] == imm_bus_destination:
					if verifierSiBusPlein(imm_bus_destination) == False:
						if verifierEspaceBagageSuffisant(imm_bus_destination, passager["poidsBagages"]) == True:
							bus["listePassagers"].append(passager)
							bus["nbrePlaceDispo"] -= 1							
							bus["capaciteKgDispo"] -= passager["poidsBagages"]							
						else:
							print("La soute à bagage de ce bus ne peut pas accueillir les bagages de ce passager!")
					else:
						print("Ce bus est déjà plein, il ne peut pas accueillir de passager supplementaire!")

	#Verifier que le bus n'est pas plein
	#Verifier que le passager n'est pas deja enregistré dans le bus
	#Verifier qu'on peut ajouter les bagages du passager

def retirerPassagerBus(cni_p, immatriculation_b):
	status = False
	for bus in listeBusFlotte:
		if bus["immtriculation"] == immatriculation_b:
			for passager in bus["listePassagers"]:
				if passager["cni"] == cni_p:
					bus["listePassagers"].remove(passager)
					status = True
	return status

#Fonction pour la gestion globale de la flotte
def getListeBus():
	pass
	#Affiche le liste de tous les bus avec les details

def getListePassagerFlotte():
	pass
	#Liste tous les passagers de la flotte

#Fonctions supplementaires
def messageBadInput():
	print("Entrée non valide, veuillez réessayer avec un choix valide s'il vous plait!")


#debut du programme
choix="9"
while choix=="9":
	choix=0
	while choix not in ["1", "2", "3"]:
		print("*****************************************")
		print("||GESTION DE LA FLOTTE ET DES PASSAGERS||")
		print("*****************************************")
		print("Choissisez un menu")
		print("1- Gérer les passagers")
		print("2- Gérer les bus")
		print("3- Informations générales")
		choix=input("Votre choix : ")
		if choix not in ["1", "2", "3"]:
			messageBadInput()
			print("")

	if choix=="1":
		print("")
		print("MENU DE GESTION DES PASSAGERS")
		print("-----------------------------")
		print("1- Créer un passager")
		print("2- Ajouter un passager dans un bus")
		print("3- Retirer un passager d'un bus")
		print("4- Deplacer un passager vers un autre bus")
		print("5- Rechercher un passager")
		choix=input("Votre choix : ")

		if choix=="1":
			#Création d'un passager
			print("")
			print("MENU DE GESTION DES PASSAGERS -- Creation de passager")
			print("-----------------------------------------------------")
			enregistrerPassager()

		elif choix=="2":
			#Ajout de passager dans un bus
			print("")
			print("MENU DE GESTION DES PASSAGERS -- Ajout de passager dans un bus")
			print("--------------------------------------------------------------")
			cniPassager=input("Entrer le numéro de CNI du passager: ")
			#On verifie que le passager est enregistré
			estPassagerEnregistre = verifierExistancePassager(cniPassager)
			if estPassagerEnregistre == True:
				#On verifie que le bus est enregistré
				immatriculationBus = input("Veuillez entrer l'immatriculation du bus: ")
				estBusEnregistre = verifierExistanceBus(immatriculationBus)
				if estBusEnregistre == True:
					ajouterPassagerBus(cniPassager, immatriculationBus)
				else:
					print("Ce bus n'est pas encore enregistré. Veuillez l'enregistrer au préalable!")
			else:
				print("Ce passager n'est pas encore enregistré. Veuillez l'enregistrer au préalable!")

		elif choix=="3":
			#Retirer un passager d'un bus
			print("")
			print("MENU DE GESTION DES PASSAGERS -- Retirer un passager d'un bus")
			print("-------------------------------------------------------------")
			cniPassager=input("Entrer le numéro de CNI du passager: ")
			#On verifie que le passager est enregistré
			estPassagerEnregistre = verifierExistancePassager(cniPassager)
			if estPassagerEnregistre == True:
				#On verifie que le bus est enregistré
				immatriculationBus = input("Veuillez entrer l'immatriculation du bus: ")
				estBusEnregistre = verifierExistanceBus(immatriculationBus)
				if estBusEnregistre == True:
					if verifierPassagerDansBus(cniPassager, immatriculationBus) == True:
						pass
						retirerPassagerBus(cniPassager, immatriculationBus)
				else:
					print("Ce bus n'est pas encore enregistré. Veuillez l'enregistrer au préalable!")
			else:
				print("Ce passager n'est pas encore enregistré. Veuillez l'enregistrer au préalable!")


		elif choix=="4":
			#Deplacer un passager vers un autre bus
			print("")
			print("MENU DE GESTION DES PASSAGERS -- Deplacer un passager vers un autre bus")
			print("-----------------------------------------------------------------------")
			print("Cette fonctionnalité est en cours de developpement. Revenez plutard!!!")

		elif choix=="5":
			#Rechercher un passager
			print("")
			print("MENU DE GESTION DES PASSAGERS -- Rechercher un passager")
			print("-------------------------------------------------------")
			print("Cette fonctionnalité est en cours de developpement. Revenez plutard!!!")

		else:
			messageBadInput()

	elif choix=="2":
		print("")
		print("MENU DE GESTION DES BUS")
		print("-----------------------")
		print("1- Ajouter un bus à la flotte")
		print("2- Nombre de place disponible dans un bus")
		print("3- Nombre de Kg disponible dans un bus")
		print("4- Verifier le transfert des passagers et bagages d'un bus vers un autre")
		choix=input("Votre choix : ")
		print("")

		if choix=="1":
			#Ajouter un bus à la flotte
			print("")
			print("MENU DE GESTION DES BUS -- Ajouter un bus à la flotte")
			print("-----------------------------------------------------")
			creerBus()
			print(listeBusFlotte)

		elif choix=="2":
			#Nombre de place disponible dans un bus
			print("")
			print("MENU DE GESTION DES BUS -- Nombre de place disponible dans un bus")
			print("-----------------------------------------------------------------")
			#On verifie que le bus est enregistré
			immatriculationBus = input("Veuillez entrer l'immatriculation du bus: ")
			estBusEnregistre = verifierExistanceBus(immatriculationBus)
			if estBusEnregistre == True:
				nombrePlace = getNbrePlaceDispoBus(immatriculationBus)
				print(f'Le bus immatriculé {immatriculationBus} a {nombrePlace} place(s) disponible!')
			else:
				print("Ce bus n'est pas encore enregistré!")

		elif choix=="3":
			#Nombre de Kg disponible dans un bus
			print("")
			print("MENU DE GESTION DES BUS -- Nombre de Kg disponible dans un bus")
			print("--------------------------------------------------------------")
			#On verifie que le bus est enregistré
			immatriculationBus = input("Veuillez entrer l'immatriculation du bus: ")
			estBusEnregistre = verifierExistanceBus(immatriculationBus)
			if estBusEnregistre == True:
				nombreKg = getNbreKgDispoBus(immatriculationBus)
				print(f'Le bus immatriculé {immatriculationBus} a {nombreKg} Kg disponible!')
			else:
				print("Ce bus n'est pas encore enregistré!")

		elif choix=="4":
			#Verifier le transfert des passagers et bagages d'un bus vers un autre
			print("")
			print("MENU DE GESTION DES BUS -- Verifier transfert Bus A ver Bus B")
			print("-------------------------------------------------------------")
			#On verifie que le bus est enregistré
			immatriculationBus = input("Veuillez entrer l'immatriculation du bus: ")
			estBusEnregistre = verifierExistanceBus(immatriculationBus)
			if estBusEnregistre == True:
				# nombreKg = getNbreKgDispoBus(immatriculationBus)
				# print(f'Le bus immatriculé {immatriculationBus} a {nombreKg} Kg disponible!')
				print("Cette fonctionnalité est en cours de developpement. Revenez plutard!!!")
			else:
				print("Ce bus n'est pas encore enregistré!")
		else:
			messageBadInput()

	elif choix=="3":
		print("")
		print("INFORMATIONS GENERALE SUR LA FLOTTE")
		print("-----------------------------------")
		print("1- Afficher la liste de tous les bus")
		print("2- Afficher la liste de tous les passagers")
		choix=input("Votre choix : ")
		print("Cette fonctionnalité est en cours de developpement. Revenez plutard!!!")

	print("")
	# print(listeBusFlotte)
	# print(listePassagerFlotte)
	print("Opération terminée. Voulez-vous effectuer une autre opération?")
	print("9: Oui    autre touche: Non")
	choix=input("Votre choix : ")

print("********************************")
print("||Fin du programme -- Aurevoir||")
print("********************************")

# print(listeBusFlotte)