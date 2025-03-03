# Configuration d'un serveur DHCP sur Raspberry Pi

## 1. Installation du serveur DHCP

```sh
sudo apt update && sudo apt install -y udhcpd
```

## 2. Sauvegarde et modification du fichier de configuration

```sh
sudo mv /etc/udhcpd.conf /etc/udhcpd.conf.back
sudo nano /etc/udhcpd.conf
```

### Contenu du fichier `/etc/udhcpd.conf`

```ini
start     192.168.10.100
end       192.168.10.254
interface       wlan0
opt    dns         192.168.10.1
option subnet   255.255.255.0
opt    router      192.168.10.1
opt    wins        192.168.10.1
option domain   local
option lease    864000
```

## 3. Configuration du réseau

```sh
sudo nano /etc/network/interfaces.d/default
```

### Contenu du fichier `/etc/network/interfaces.d/default`

```ini
auto lo
iface lo inet loopback

allow-hotplug eth0
iface eth0 inet manual

allow-hotplug wlan0
iface wlan0 inet static
    address 192.168.10.1
    netmask 255.255.255.0
```

## 4. Attribution de l'adresse IP à l'interface

```sh
ip addr
sudo ip addr add 192.168.10.1/24 dev wlan0
```

## 5. Démarrage du service DHCP

```sh
sudo systemctl start udhcpd
sudo systemctl status udhcpd
```

## 6. Vérification du service DHCP

```sh
ps -ef | grep dhcp
journalctl -f
```

## 7. Démarrage du service Hostapd

```sh
sudo systemctl start hostapd
sudo systemctl status hostapd
```

## 8. Activation du DHCP au démarrage

```sh
sudo sed -i "s/^DHCPD_ENABLED=\"no\".*/DHCPD_ENABLED=\"yes\"/" /etc/default/udhcpd
sudo systemctl enable udhcpd
```

## 9. Vérification de la connectivité

```sh
ping 192.168.10.163
ping 192.168.10.1
```

## 10. Hébergement d'un fichier HTML avec un serveur web simple

```sh
nano index.html
```

Ajoutez votre code HTML dans `index.html`, puis démarrez un serveur web léger :

```sh
sudo python3 -m http.server 80
```

