# 🚀 Configuration SSH avec un Raspberry Pi

---

## 🖥️ Pré-requis

- Un **Raspberry Pi** avec Raspberry Pi OS installé.
- Un ordinateur sous Windows avec **PowerShell**.
- Une connexion réseau entre les deux appareils.

---

## 📋 Instructions

### 🎯 Étape 1 : Configuration du Raspberry Pi

1. **Obtenir l'adresse IP du Raspberry Pi :**  
   ```bash
   hostname -I
   ```

2. **Installer SSH et le serveur OpenSSH (si non installé) :**  
   ```bash
   sudo apt install -y ssh
   sudo apt install -y openssh-server
   ```

---

### 🎯 Étape 2 : Configuration sur Windows (PowerShell)

1. **Connexion initiale via SSH :**  
   Remplacez les valeurs :  
   - `<mot_de_passe>` : Mot de passe du Raspberry Pi.  
   - `<adresse_IP>` : Résultat de la commande `hostname -I`.  
   ```powershell
   ssh <mot_de_passe>@<adresse_IP>
   ```

2. **Génération d'une clé SSH :**  
   Lancez la commande suivante pour générer une paire de clés :  
   ```powershell
   ssh-keygen
   ```

3. **Copie de la clé publique vers le Raspberry Pi :**  
   Modifiez les informations :  
   - `super` : Nom de l'utilisateur sur le Raspberry Pi.  
   - `10.5.57.91` : Adresse IP du Raspberry Pi.  
   ```powershell
   scp C:\Users\Admin\.ssh\id_ed25519.pub super@10.5.57.91:.ssh/authorized_keys
   ```

4. **Connexion sans mot de passe :**  
   Une fois la clé configurée, utilisez simplement la commande :  
   ```powershell
   ssh super@10.5.57.91
   ```

---

## ✅ Résultat attendu

Vous pouvez désormais vous connecter à votre Raspberry Pi sans entrer de mot de passe. 
