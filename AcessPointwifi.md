# Configuration de Hostapd pour un point d'accès Wi-Fi sur Raspberry Pi 4

## Étape 1 : Copier le fichier de configuration par défaut

Exécute la commande suivante pour copier le fichier de configuration exemple de Hostapd dans le répertoire de configuration :

```bash
sudo cp /usr/share/doc/hostapd/examples/hostapd.conf /etc/hostapd/
```

## Étape 2 : Modifier le fichier de configuration

Vérifie que l'interface Wi-Fi est bien définie sur `wlan0` et ajuste les paramètres d'authentification et de mot de passe Wi-Fi :

```bash
interface=wlan0
auth_algs=1
wpa_passphrase=motdepasseWiFi
```

## Étape 3 : Modifier le fichier de démarrage de Hostapd

Ouvre et modifie le fichier `/etc/default/hostapd` pour spécifier le fichier de configuration :

```bash
sudo nano /etc/default/hostapd
```

Modifie la ligne suivante :

```bash
# DAEMON_CONF=""
```

Pour qu'elle devienne :

```bash
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

## Étape 4 : Démarrer Hostapd

Lance Hostapd avec la commande suivante :

```bash
sudo systemctl start hostapd
```

## Étape 5 : Démarrer Hostapd automatiquement au démarrage

Si tu veux que Hostapd se lance automatiquement au démarrage, exécute la commande suivante :

```bash
sudo systemctl enable hostapd
```

## Étape 6 : Vérifier que Hostapd fonctionne

Pour vérifier que Hostapd fonctionne correctement, utilise la commande suivante :

```bash
sudo systemctl status hostapd
```

## Étape 7 : Configurer un DHCP (Optionnel)

Si tu souhaites que ton point d'accès attribue des adresses IP aux clients, installe et configure `dnsmasq` :

```bash
sudo apt install dnsmasq
```

Ensuite, configure le fichier `/etc/dnsmasq.conf` pour attribuer des adresses IP sur l'interface `wlan0`.

## Étape 8 : Résolution des problèmes

Si tu rencontres des problèmes, consulte les logs de Hostapd avec la commande suivante :

```bash
journalctl -xe | grep hostapd
```
```

Tu peux adapter les paramètres comme le mot de passe Wi-Fi ou l'interface en fonction de tes besoins spécifiques.
