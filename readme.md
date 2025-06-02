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

Nom réseau : Rasp
MDP : secret1234


Au lieu d'utiliser du http on essaie le rtp avec la commande suivante pour diffcuser depuis la raspberry en ligne de commande:

cvlc -vvv video.avi --sout '#rtp{dst=239.255.255.250,port=5004,mux=ts}'

la commande ne marche pas car l’adresse 239.255.255.250 est réservée pour SSDP (Service Discovery Protocol) donc on essaie la suivante :

cvlc -vvv video.avi --sout '#rtp{dst=239.255.12.42,port=5004,mux=ts}'

Ca fonctionne et on arrive à recuperer le flux sur vlc avec rtp://239.255.12.42:5004

On peut aussi voir le flux sur Wireshark en continue

#### **10.02.2025**  

Création et recherche pour l'application pour controller le rasberry à distance

#### **17.02.2025**  

Cours sur le projet led

#### **03.03.2025**  

Avancé sur la PWA qui controle le raspberry à distance

#### **14.04.2025**  

Avancé sur la recherche et la caméra, elle fonctionne il suffit de la relier à notre application

#### **12.05.2025**  

Avancé sur notre application avec les différents boutons pour deplacer la voiture


#### **19.05.2025**  

Recherche sur un nouveau système pour le stream de la caméra car l'ancien système n'est plus opérationnel 

#### **26.05.2025**  

Utilisation de mediamtx et essaie d'insertion sur notre application mais impossible du au format rtsp

#### **02.06.2025**  

Changement du format au format WebRTC





