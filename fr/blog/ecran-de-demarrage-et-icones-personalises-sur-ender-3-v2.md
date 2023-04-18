---
title: Ecran de démarrage et icônes personnalisées sur Ender 3 v2
date: 3 septembre 2022
static: true
template: post_fr
type: post
lang: fr
author: Paillat
categories: ender-3,impression-3d
coverImage: /images/ecran-de-demarrage-et-icones-personalises-sur-ender-3-v2/En-avant.png
---

Si vous possédez une imprimante 3d **Ender 3 V2** de chez **CREALITY**, sachez qu'il est très facilement possible de customiser l'interface graphique de celle ci. Pour ce faire vous n'aurez besoin uniquement d'une **carte micro SD** et du logiciel **PAINT.net**. Si vous voulez modifier aussi les icones, vous devrez télécharger **Dwin ICO Tools** (voir dans la rubrique installation) Nous allons maintenant voir étape par étape comment le faire:

## Installation du logiciel PAINT.net

Bien que ce nom laisse penser à un site web, il s'agit bel et bien d'un logiciel à installer sur votre pc. Pour ce faire rendez-vous sur [www.dotpdn.com](https://www.dotpdn.com/downloads/pdn.html), télechargez la dernière version, et enfin éxecutez le fichier présent dans le dossier .zip. Suivez les instructions puis c'est tout.

## Installation de Dwin ICO Tools

Pour installer cet utilitaire rendez vous [ici](https://github.com/NanMetal/dwin-ico-tools/releases) et téléchargez le fichier `DwinIcoTool.exe` uniquement en cliquant dessus. Il n'est pas nécessaire de lancer le fichier.

## Télechargement du firmware

Vous pouvez utiliser le firmware de votre choix. Si vous n'avez aucun firmware à votre disposition, vous pouvez utiliser le firmware officiel de creality que vous trouverez [ici](https://electronique.cc/wp-content/uploads/2022/09/DWIN_SET_ender_3_v2.zip). Une fois le firmware télechargé, dans le dossier `DWIN_SET` vous trouverez les différents fichiers que vous pourrez modifier.

## Modification de l'écran de démarrage

Vous trouverez l'écran de démarrage dans le dossier `DWIN_SET` que vous avez télechargé précedemment. L'image de démarrage s'appelle `0_start.jpg`. Notez bien quelque part la taille de l'image (géneralement quelque chose autour de 14 ko, mais cela peut changer selon le firmware que vous modifiez). Je vous conseille de la copier dans un autre dossier pour la modifier. L'image est modifiable dans n'importe quel logiciel de retouche photo tel que photoshop, paint, etc. Vous pouvez aussi utiliser le logiciel PAINT.net que vous avez installé précedemment. Une fois l'image modifiée, veillez à la sauveharder au format `.jpg`, puis ovrez-la dans PAINT.net et re-sauveguardez-la en vous assurant de choisir l' option **4:4:4** et de modifier la qualité pour que la taille soit plus petite ou egale de la taille originale. Il est important de garder l'image finale à l'**horizontale**.

Vous pouvez ensuite remplacer l'image originale par celle custom dans le dossier `DWIN_SET`.

## Modification des icones

Dans votre dossier `DWIN_SET` vous trouverez aussi un ou plusieurs fichiers `.ico`. Ces fichiers contiennent toutes les icones de l'interface. Pour les modifier, je vous conseille aussi de les copier dans un dossier séparé. Une fois copiés, glissez un des fichiers sur l'application `Dwin ICO tools.exe`. Une fenêtre d'alerte pourrais s'ouvrir. Vous pouvez l'ignorer en cliquant sur `en savoir plus` puis `exécuter quand même`. Un terminal va s'ouvrir. Vous devrez alors patienter quelques secondes, puis pourrez fermer ce dernier. Un dossier nommé `out` aura été créé. Il contient toutes les images potentiellement modifiables. Vous pourrez les modifier à votre guise, en suivant les mêmes précautions que pour la modification de l'écran de démarrage. Une fois cela terminé vous pouvez faire glisser le dossier out dans `Dwin ICO tools.exe`. Cela vas recompacter les images en un fichier `.ico` que vous veillerez à renommer comme le fichier d'origine en le remplaçant. Vous pouvez répéter ces passages pour autant de fichiers `.ico` que vous avez, en supprimant le dossier `out` à chaque fois.

<div class="images">
<div class="image">
<img src="/images/ecran-de-demarrage-et-icones-personalises-sur-ender-3-v2/screenshot_1.png" alt="La fenêtre d'alerte">
<blockquote class="image-caption">La fenêtre d'alerte de windows</blockquote>
</div>
</div>

## Formatage de la carte sd

Il est important de formater la carte sd avant l'utilisation en **fat32** **4096**. Sinon cela ne va pas marcher.

## Flashage du firmware

Pour flasher le firmware il faudra copier le dossier `DWIN_SET` dans votre carte sd. Vous devrez ensuite éteindre votre imprimante, déconnecter puis ouvrir l'arrière de votre écran en dévissant les quatre vis et en tirant gentiment sur les deux connectiques en métal. Vous y trouverez un emplacement pour votre carte micro sd. Après avoir inséré la carte micro sd, rebranchez l'écran et allumez l'imprimante. L'écran s'allumera en bleu. Attendez jusqu'à ce que l'écran s'allume en orange/rouge, puis éteignez l'imprimante, enlevez la carte sd et rallumez l'imprimante. Si tout fonctionne correctement, vous pouvez alors refermer définitivement l'écran. Sinon, vérifiez d'avoir bien suivi les étapes concernant le formatage de la carte sd et les critères des images/icones.

## Conclusion

Nous avons vu comment aujourd'hui comment customiser son ender 3 v2. J'espère que cet article vous aura plu, si c'est le cas n'hésitez as à le partager et à laisser un commentaire, vous pouvez nous retrouver sur [youtube](https://electronique.cc/youtube), [instagram](https://electronique.cc/instagram) ou [printables](https://electronique.cc/printables).

A+