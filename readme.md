## Projet Controlleur de Voiture 

### Nom du Projet : SmartControlleur

### Chronologie du Projet

---

#### **13.01.2025**  
**Choix de l'idée du projet et création du cahier des charges**  


#### **20.01.2025**  
**Installation du software pour les Raspberry et création du Github**  


#### **27.01.2025**  

Test de connection au raspberry avec une connexion ssh. Nous avons reussi à nous connecter avec le pc de Maxime mais pas celui de Timoléon.
Essaie de diffusion de video avi depuis le vlc du raspberry et de la récupérer.

commande pour diffuser en http:
cvlc /chemin/vers/video.avi --sout '#http{mux=ts,dst=:8080/}' --sout-all --sout-keep
