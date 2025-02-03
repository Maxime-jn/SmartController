## Projet Controlleur de Voiture 

### Nom du Projet : SmartControlleur

### Chronologie du Projet

---

#### **13.01.2025**  
**Choix de l'idée du projet et création du cahier des charges**  


#### **20.01.2025**  
**Installation du software pour les Raspberry et création du Github**  


#### **27.01.2025**  

Test de connexion au raspberry avec une connexion ssh. Nous avons reussi à nous connecter avec le pc de Maxime mais pas celui de Timoléon.
Essaie de diffusion de video avi depuis le vlc du raspberry et de la récupérer.

**commande pour diffuser en http:**
cvlc /chemin/vers/video.avi --sout '#http{mux=ts,dst=:8080/}' --sout-all --sout-keep
https://www.aranacorp.com/fr/configurer-un-raspberry-pi-en-point-dacces-wifi/

#### **03.02.2025**  

La connexion au raspberry avec une connexion ssh marche.
On a crée un point d'accès Wi-Fi sur Raspberry Pi 4.
Tout marche mais par contre impossible de s'y connecter. 
le réseau de déconecte au bous de 5 secondes



Au lieu d'utiliser du http on essaie le rtp avec la commande suivante pour diffcuser depuis la raspberry en ligne de commande:

cvlc -vvv video.avi --sout '#rtp{dst=239.255.255.250,port=5004,mux=ts}'

la commande ne marche pas car l’adresse 239.255.255.250 est réservée pour SSDP (Service Discovery Protocol) donc on essaie la suivante :

cvlc -vvv video.avi --sout '#rtp{dst=239.255.12.42,port=5004,mux=ts}'

Ca fonctionne et on arrive à recuperer le flux sur vlc avec rtp://239.255.12.42:5004

On peut aussi voir le flux sur Wireshark en continue


