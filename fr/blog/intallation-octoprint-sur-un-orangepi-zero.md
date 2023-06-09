---
title: "Installation d'Octoprint sur un Orangepi zero"
date: 19 octobre 2022
unformat-date: 2022.10.19
categories: electronique,fdm,impression-3d,octoprint
image: /images/installation-octoprint-sur-un-orangepi-zero/En-avant.png
static: true
type: post
template: post_fr
author: Paillat
lang: fr
---

<img src="<!-- image -->" alt="post main image" class="post-main-image">

# Installation d'Octoprint sur un Orangepi zero

L'inflation et la pénurie de composants électroniques ont engendré ces deux dernières années un forte augmentation des prix des cartes raspberry et pénurie de ces micro-ordinateurs. C'est pourquoi aujourd'hui nous allons voir comment installer octoprint, le célèbre système de gestion d'imprimantes 3d à distance, sur une carte Orangepi, moins chère, telle que l'orange pi zero dans notre cas.

## Prérequis matériel

Comme matériel il vous faudra:

- Un orangepi Zero
- Un cable ethernet
- Une carte microSD de 8 GO au minimum
- Une alimentation USB C de **3A** minimum c'est très important
- Un câble d'alimentation
- Un câble usb A vers la connectique de votre imprimante

## Prérequis logiciel

Pour performer l'installation, vous aurez besoin de multiples logiciels et fichier, que nous allons voir un par un de suite:

### Installation de Angry IP scanner

Un premier logiciel qu'il nous faudra installer est [Angry IP scanner](https://angryip.org). Il s'agit d'un logiciel qui permettra de scanner votre réseau internet pour trouver son adresse ip.

Vous pouvez le télecharger en cliquant [ici](https://angryip.org/download/#windows), en choisissant la version Windows installer.

### Installation de Balena Etcher

Le logiciel [Balena Etcher](https://www.balena.io/etcher/) vous permettera de préparer votre carte microSD pour l'orangePI.

Vous pouvez le télecharger en cliquant [ici](https://www.balena.io/etcher/).

### Télechargement de Armbian

[Armbian](https://www.armbian.com) sera le système d'exploitation que nous allons installer sur notre carte microSD. Il vous faut télecharger l'image disque de Armbian pour orangepi Zero [ici](https://www.armbian.com/orange-pi-zero/#:~:text=Torrent%20download-,Direct%20download,-Check%20other%20download) en choisissant bien Direct download.

## Installation d'Armbian

### Préparation de la carte microSD

Vous allez maintenant ouvrir logiciel Balena Etcher et brancher votre carte microSD à votre ordinateur.

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/Etcher-1.0.png" alt="Etcher-1.0">
<blockquote class="image-caption">Vue du logiciel Etcher</blockquote>
</div>
</div>

Le logiciel Etcher

Vous allez cliquer sur Select image et ouvrir le fichier Armbian précedemment télechargé, puis choisir Select drive et choisir votre carte microSD et enfin pressez Flash! et attendez que l'operation se términe.

Une fois cette opération terminée vous pourrez débrancher votre carte microSD de votre ordinateur.

### Préparation de l'orangePI

Nous allons tout d'abord brancher notre carte microSD dans son emplacement dédie au dessous de notre orangePI.

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/Orangepi-schematic-up.png" alt="Orangepi-schematic-up">
<blockquote class="image-caption">Vue du dessus d'un orangePI zero</blockquote>
</div>
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/Orangepi-schematic-down.png" alt="Orangepi-schematic-down">
<blockquote class="image-caption">Vue du dessous d'un orangePI zero</blockquote>
</div>
</div>

Ensuite, vous allez brancher votre orangePI à votre box internet au moyen du câble ethernet puis brancher l'alimentation.

### Recherche de l'addresse IP

Vous allez maintenant ouvrir le logiciel Angry Ip Scanner et démarrer un balayage de votre réseau local en cliquant sur démarrer .

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/ipscan_1.png" alt="Ip scanner view">
<blockquote class="image-caption">Vue du logiciel Angry Ip Scanner</blockquote>
</div>
</div>

Une fois le scan terminé, trouvez dans la colonne hostame le nom qui s'apparente à orangePI. Si il n'y apparait pas, relancez un second scan.

Notez l'addresse ip marquée dans la colonne IP.

### Configuration d'Armbian

Maintenant pressez la combinaison de touches Windows + R, tapez `cmd` dans le champ ouvrir puis pressez ok.

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/winr_cmd.png" alt="Winr cmd">
<blockquote class="image-caption">La fenêtre exécuter</blockquote>
</div>
</div>

Dans la fenêtre qui va s'ouvrir vous taperez la commade suivante: `ssh root@**votre_addresse_ip**` puis comme mot de passe vous taperes `1234` . Vous devriez normalement voir un texte ressemblant au suivant s'afficher à l'écran:

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/ssh_root.png" alt="Ssh root">
<blockquote class="image-caption">La session ssh root</blockquote>
</div>
</div>

Vous allez taper un nouveau mot de passe pour l'utilisateur root, qui est l'administrateur du système. A noter que **ce que vous tapez n'est pas visible** pour des raisons de sécurité.

Une fois cela terminé, poursuivez avec le étapes suivantes comme indiqué sur l'image suivante.

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/ssh_root_2.png" alt="Ssh root 2">
<blockquote class="image-caption">La session ssh root</blockquote>
</div>
</div>

Vous devrez créer un nouvel utilisateur, nommé pi, et lui définir un mot de passe, que nous appelleront par la suite **mot de passe pi**. Lorsque vous serez ivites à choisir le pays, veillez à bien choisir fr\_FR.UTF-8.

Une fois l'installation terminée tapez la commande exit.

## Installation d'octoprint

Dans votre terminal, tapez la commande suivante `ssh pi@**votre_adresse_ip**` vous pouvez aussi coller les commandes dans le terminal en cliquant droit. Lors des étapes suivantes, si l'on vous demande à un moment donné de confirmer avec un Oui ou un Yes, faites-le.

Tapez ensuite le **mot de passe pi** et une fois connecté executez la commande suivante:

`sudo apt-get update && sudo apt-get upgrade -y`

Vous serez invités à taper votre mot de psse. Tapez le **mot de passe pi**.

Une fois ces commandes terminées, tapez celle-ci:

`sudo apt-get install -y python-pip python-dev python-setuptools python-virtualenv git libyaml-dev build-essential libffi-dev virtualenv`

Maintenant executez la commande suivante pour crées un dossier OctoPrint et y accéder.

`mkdir OctoPrint && cd OctoPrint`

Puis cette commande ci:

`virtualenv venv`

Et celle la:

`source venv/bin/activate`

Puis en suite cette commande

`pip install pip --upgrade`

Et enfin celle ci. Elle va prendre un moment, et c'est normal.

`pip install octoprint`

Tapez ces deux dérnières commanes:

`sudo usermod -a -G tty pi`

`sudo usermod -a -G dialout pi`

Une fois cette dernière commande terminée, rendez vous dans votre navigateur internet et tapez **votre\_adresse\_ip**:5000 les deux points sont importants.

Lors de la configuration d'octoprint, il vous sera demandé d'indiquer les commandes permettant de gérer le système, les voici:

Redémarrer OctoPrint: `sudo service octoprint restart`

Redémarrer le système: `sudo reboot now`

Eteindre système: `sudo shutdown -h now`

Vous pourrez alors configurer Octoprint.

Une fois la configuration terminée, vous pouvez retourner dans le terminal et taper le raccourci clavier ctrl+c.

### Activation du démarrage automatique d'Octoprint

Vous allez maintenant éxecuter les commandes suivantes:

`wget https://github.com/Paillat-dev/OctoPrint-Orangepi-scripts/raw/master/scripts/octoprint.init && sudo mv octoprint.init /etc/init.d/octoprint`

`wget https://github.com/Paillat-dev/OctoPrint-Orangepi-scripts/raw/master/scripts/octoprint.default && sudo mv octoprint.default /etc/default/octoprint`

Et ces deux autres:

`sudo chmod +x /etc/init.d/octoprint`

`sudo chmod +x /etc/default/octoprint`

Ensuite cette commande pour confirmer les changements:

`sudo update-rc.d octoprint defaults`

Voilà, votre octoprint est désormais installé et pret à être utilisé.

### Facultatif - Installation du wifi

Pour installer le wifi vous devrez exécuter quelques commandes supplémentaires.

La première est: `nmtui-connect **SSID**` ou **SSID** est le nom de votre réseau WiFi.

Vous devrez ensuite taper votre mot de passe WiFi et enfin sélectionner ok, puis entrée.

### Définir une adresse IP statique

Pour défiir l'adressse ip comme statique, tapez la commande suivante:

`sudo armbian-config`

Dans le menu, naviquez avec les fleches et sélectionnez Networking

<div class="images">
<div class="image">
<img src="/images/installation-octoprint-sur-un-orangepi-zero/armbian-wifi.webp" alt="Armbian wifi">
<blockquote class="image-caption">Le menu Networking</blockquote>
</div>
</div>

Choisissez votre connexion WiFi, puis Static, tapez entrée, puis vous pouvez quitter le menu.

Voilà, j'espère que cet article vous aura plu, n'hésitez pas à laisser un commentaire, et à la prochaine!
