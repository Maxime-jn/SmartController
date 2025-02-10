# Diffusion d'une vidéo via VLC sur Raspberry Pi avec RTP

Nous utilisons **VLC** pour diffuser une vidéo depuis un **Raspberry Pi** et la récupérer sur **VLC sous Windows**.

## Diffusion avec HTTP (problème rencontré)

Initialement, nous essayons de diffuser via **HTTP**, mais nous décidons de tester **RTP** avec la commande suivante :

```bash
cvlc -vvv video.avi --sout '#rtp{dst=239.255.255.250,port=5004,mux=ts}'


Cependant, cette commande ne fonctionne pas, car l'adresse 239.255.255.250 est réservée pour SSDP (Service Discovery Protocol).

Nous modifions l'adresse et utilisons la commande suivante :
cvlc -vvv video.avi --sout '#rtp{dst=239.255.12.42,port=5004,mux=ts}'


Cette fois-ci, la diffusion fonctionne et nous pouvons récupérer le flux sur VLC sous Windows avec l'URL suivante :
rtp://239.255.12.42:5004


Nous pouvons également observer le flux en continu sur Wireshark.
