---
author: Paillat
title: Il vous faut cette extension gratuite pour Klipper
static: true
image: /images/you-need-this-klipper-extension/En-avant.png
description: Si vous avez déjà utilisé Klipper, vous savez à quel point c'est utile. Mais il peut être encore meilleur avec cette extension gratuite.
template: post_fr
category: Klipper
lang: fr
type: post
---
# Il vous faut cette extension gratuite pour Klipper

<img src="<!-- image -->" alt="post main image" class="post-main-image">

Si vous avez déjà utilisé Klipper, vous savez à quel Klipper est utile et permet de booster les capacités de votre imprimante 3D. Mais il peut être encore meilleur avec cette extension gratuite, qui vous permettra de gagner du temps et de l'argent, en stoppant automatiquement votre impression en cas d'échec d'impression, vous permettant ainsi de ne pas gaspiller de filament, ni de temps.

Cette extension fonctionne grâce à une caméra qui va surveiller votre impression et détecter les échecs d'impression par le biais d'un modèle d'IA. Elle est compatible avec les caméras Raspberry Pi, mais aussi avec les caméras USB standard.

## Installation

### Prérequis
Pour installer cette extension, vous aurez deux possibilités : soit vous utilisez les serveurs de Obico, l'entreprise ayant développé cette extension, mais les possibilités seront limitées et il vous faudra payer un abonnementpour débloquer ces fonctionnalités, soit vous installez votre propre serveur. Dans les deux cas, vous aurez besoin d'un Raspberry Pi avec une caméra et Klipper installé au préalable. Si vous utilisez votre propre serveur, vous aurez aussi besoin d'un ordinateur pour l'installer, un Raspberry Pi ne suffira pas pour ce faire, à titre d'éxemple un vieil ordinateur avec un processeur Intel intel de génération 4 ou plus avec au moins 4gb de ram fera l'affaire. Vous pouvez trouver [ici](https://obico.io/docs/server-guides/hardware-requirements/) les spécifications recommandées par Obico. Cet ordinateur devra être connecté au même réseau que votre Raspberry Pi, et devra avoir Linux installé dessus. Nous vous recommandons d'utiliser Ubuntu 22.04, mais vous pouvez utiliser n'importe quelle distribution Linux. VOus pouvez trouver [ici](https://lecrabeinfo.net/installer-ubuntu-22-04-lts-le-guide-complet.html) un guide pour installer Ubuntu 22.04.
Donc, pour résumer, vous aurez besoin de :
- Un **Raspberry Pi** avec **Klipper** installé
- Un **ordinateur** avec Linux installé (FACULTATIF si vous utilisez les serveurs de Obico)
- Une **caméra** Raspberry Pi ou USB

### Installation du serveur (FACULTATIF si vous utilisez les serveurs de Obico)
Nous allons directement utiliser le script d'installation de Obico, qui va installer le serveur pour nous. Pour ce faire, il vous suffit de copier les commandes suivante dans votre terminal de votre serveur une à une  **N'EXECUTEZ PAS CES COMMANDES SUR VOTRE RASPBERRY PI** :

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker docker-compose git -y
git clone -b release https://github.com/TheSpaghettiDetective/obico-server.git
cd obico-server && sudo sudo docker compose up -d
```

Si la dernière commande ne fonctionne pas, vous pouvez essayer celle-ci :
```bash
sudo docker-compose up -d
```

Vous devez ensuite définir une IP fixe. Vous pouvez trouver [ici](https://encause.fr/comment-configurer-une-adresse-ip-statique-sur-ubuntu-22-04-lts-et-22-10/) un guide pour le faire sous Ubuntu 22.04. Vous touverez facilement des guides pour le faire sous d'autres distributions Linux.

Maintenant, vous devez vous rendre sur l'adresse `VOTRE_IP:3334/admin/` (remplacez `VOTRE_IP` par l'adresse IP de votre serveur) et vous connecter avec le compte `root@example.com` et le mot de passe `supersecret`. Vous devriez voir une page comme celle-ci :

<div class="images">
<div class="image">
<img src="/images/you-need-this-klipper-extension/DJANGO_LOGIN.png" alt="Django login page">
<blockquote class="image-caption">Page de connexion</blockquote>
</div>
</div>

Rendez-vous ensuite sur `VOTRE_IP:3334/admin/app/user/1/password/` et changez le mot de passe. Vous pouvez maintenant vous connecter avec votre nouveau mot de passe à l'inérface d'administration.

Maintenant, rendez-vous sur `VOTRE_IP::3334/admin/sites/site/1/change/` et modifiez les deux champs présents pour y insérer votre adresse IP. **N'oubliez pas de sauvegarder!**.

Et voilà, vous avez terminé!

### Installation de l'extension

Tout d'abrd connectez vous à votre Raspberry PI en `SSH`.

Une fois cela effectué, tapez la commande suivante dans votre terminal:

```bash
    cd ~ && git clone https://github.com/TheSpaghettiDetective/moonraker-obico.git && cd moonraker-obico && ./install.sh
```

Vous pourrez accepter les messages et insérer votre mot d passe sudo si nécessaire.

Lorsque le message suivant apparsitra:
```bash
Now tell us what Obico Server you want to link your printer to.
You can use a self-hosted Obico Server or the Obico Cloud. For more information, please visit: https://obico.io.
For self-hosted server, specify "http://server_ip:port". For instance, http://192.168.0.5:3334.
```

Vous pourrez simplement appuyer sur `Entrée` pour utiliser les serveurs de Obico, ou insérer l'adresse IP de votre serveur si vous en avez installé un auparavant, en spécifiant le port (par défaut 3334), exemple: `http://VOTRE_IP:3334`.

On vous demandera ensuite de spécifier un code d'accès. Dans le cas ou vous utilisez le serveur installé aupravant, rendez vous dans votre navigateur sur `http://VOTRE_IP:3334` et connectez vous avec le compte admin et le mot de passe specifié auparavant. Au contraire, si vous voulez utiliser les serveurs d'Obico, rendez-vous sur leur site web [ici](https://app.obico.io/accounts/signup/) et créez un compte si nécessaire, sinon connectez vous avec votre compte.

Vous verrez dans les deux cas une page comme celles-ci:

<div class="images">
<div class="image">
    <img src="https://www.obico.io/assets/images/welcome-web-0df98f779b3afdaf66556e3fbce5f386.jpg" alt="Obico welcome page">
    <blockquote class="image-caption">Page de bienvenue si vous créez un compte</blockquote>
</div>
<div class="image">
    <img src="https://www.obico.io/img/user-guides/setupguide/select-platform-web.jpg" alt="Obico select platform page">
    <blockquote class="image-caption">Page de sélection de Klipper</blockquote>
</div>
</div>

Sélectionnez Link printer, Klipper puis cliquez sur Next. Vous verrez alors une page comme celle-ci avec un code d'accès:

<div class="images">
<div class="image">
    <img src="https://www.obico.io/img/user-guides/setupguide/klipper-verification-code-web.jpg" alt="Obico verification code page">
    <blockquote class="image-caption">Page de code d'accès</blockquote>
</div>
</div>

Copiez le code d'accès et collez le dans votre terminal, puis appuyez sur `Entrée`.

C'est terminé! Vous pouvez maintenant vous rendre sur `http://VOTRE_IP:3334` si vous utilisez votre propre serveur, ou sur `https://app.obico.io` si vous utilisez les serveurs de Obico, et vous connecter avec votre compte. Vous devriez voir votre imprimante dans la liste des imprimantes, et pouvoir la connecter. Vous pourrez alors activer les services de détection par IA dans les paramètres de votre imprimante.

# Conclusion

Nous avons maintenant terminé! Vous pouvez maintenant utiliser les services de détection par IA de Obico pour surveiller vos impressions. Si vous avez des questions, n'hésitez pas à les poser dans les commentaires, je vous répondrai dès que possible. En attendant, c'était Paillat et à la prochaine!