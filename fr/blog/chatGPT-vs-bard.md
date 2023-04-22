---
author: Paillat
title: ChatGPT vs Bard - Quel est le meilleur assistant au code?
description: Dans cet article, nous allons comparer deux IA génératives, ChatGPT et Bard, et voir laquelle est la meilleure pour l'assistance au code.
image: REPLACE_WITH_IMAGE_URL
static: true
template: post_fr
lang: fr
image: /images/chatGPT-vs-bard/En-avant.png
type: post
---

<img src="<!-- image -->" alt="post main image" class="post-main-image">

# ChatGPT vs Bard - Quel est le meilleur assistant au code?

ChatGPT et Bard sont deux modèles d’IA génératifs qui ont récemment fait leur apparition sur le marché. ChatGPT, développé par OpenAI, a été introduit en novembre 2022 et a rapidement gagné en popularité grâce à ses capacités de génération de texte de type humain1. Bard, quant à lui, est le concurrent de Google à ChatGPT et a été mis à jour pour générer du code dans plus de 20 langages de programmation2. Dans cet article, nous allons comparer ces deux modèles d’IA et voir lequel est le meilleur pour l’assistance au code.

## Challenge 1: Bot Discord économique

Pour ce premier challenge, nous allons créer un bot Discord qui répond à des commandes simples. Nous allons utiliser le langage Python et le framework py-cord pour créer ce bot. les instructions données sont:
> Give me an example discord bot in python with pycord. It should have a basic economy system with an sqlite database.
qui se traduit par:
> Donne moi un exemple de bot discord en python avec pycord. Il devrait avoir un système économique basique avec une base de données sqlite.

Je ne vais pas lister la réponse complète ici, mais vous pouvez trouver ces dernières [sur le dépot GitHub](https://github.com/electronique-cc/chatgpt-vs-bard) de cet article.

Nous remarquons immédiatement après avoir copié le code dans un fichier, que celui géneré par bard comprend deux erreurs, nous informant que la librairie `datetime` n'a pas été importée. Il s'agit là d'une erreur mineure de la part de bard, mais toujours d'une erreur. Après lui avoir demandé de corriger son erreur, bard nous a donné une réponse correcte.

Nous pouvons toutefois noter un bon point pour bard, qui a importé le token discord depuis une [variable d'environnement](https://fr.wikipedia.org/wiki/Variable_d%27environnement) et non pas directement dans le code. Cela augmente la sécurité du code, car le token n'est pas visible dans le code source. De plus, le code de bard est nettement plus commenté que celui de ChatGPT, ce qui le rend plus facile à comprendre pour un débutant. 

Malheureusement pour Bard, lors de l'éxecution du code, la base de données n'est pas utilisée correctement, et aucue des trois commandes prposées par Bard ne fonctionnent. Le code de ChatGPT, quant à lui, est presque parfait, les seules erreurs provienent de la librairie `pycord` qui a été mise à jour depuis la génération du code. J'ai donc demandé à ChatGPT de corriger son code, pour qu'il fonctionne avec la dernière version de `pycord`, en lui donnant le code d'éxemple de la documentation de `pycord` comme référence. ChatGPT n'a toutefois pas réussi à corriger son code, et a généré un code qui ne fonctionne pas. 

Bien que tous les deux aient échoué à ce challenge, les erreurs de Bard sont plus difficiles à corriger que celles de ChatGPT, c'est pourquoi je considère ChatGPT comme le gagnant de ce challenge.

## Challenge 2: Résolution du problème du Cavalier
Pour ce deuxième challenge, nous allons demander à ChatGPT et Bard de résoudre le problème du cavalier, dans le language de leur choix. Toutefois, les conditions sont strictes, nous demandons d'avoir une intérface permettant de définir une position de départ, ainsi que si la position d'arrivée doive être la même que celle de départ. La requête donnée est:
> Give me a program that solves the knight's tour problem. It should have a cli GUI that allows you to set the starting position and whether the end position should be the same as the starting position. You can use any programming language you want.
qui se traduit par:
> Donne moi un programme qui résout le problème du cavalier. Il doit avoir une interface en ligne de commande qui permet de définir la position de départ et si la position d'arrivée doit être la même que celle de départ. Utilise le langage de programmation de ton choix.

A nouveau, le code de Bard est plus commenté que celui de ChatGPT, et il est plus facile à comprendre. Toutefois, le code de Bard ne fonctionne pas, et ne permet pas de résoudre le problème du cavalier. Le code de ChatGPT, quant à lui, fonctionne parfaitement, et permet de résoudre le problème du cavalier.

## Challenge 3: Somme d'entiers non adjacents
Pour ce troisième challenge, nous allons demander à ChatGPT et Bard de créer un programme qui calcule la somme maximale optensible en additionnant des entiers non adjacents d'une liste. La requête donnée est:

>Write a program that takes a list of integers as input, and returns the maximum sum that can be obtained by adding any non-adjacent integers in the list.
>
>Here are some additional constraints:
>
>The input list may be empty or contain up to 10^5 integers.
>The integers in the list may be negative, positive, or zero.
>The program should have a time complexity of O(n), where n is the length of the input list.

Qui se traduit par:

>Ecris un programme qui prend une liste d'entiers en entrée, et renvoie la somme maximale qui peut être obtenue en additionnant des entiers non adjacents dans la liste.
>
>Voici quelques contraintes supplémentaires:
>
>La liste d'entrée peut être vide ou contenir jusqu'à 10^5 entiers.
>Les entiers dans la liste peuvent être négatifs, positifs, ou nuls.
>Le programme doit avoir une complexité temporelle de O(n), où n est la longueur de la liste d'entrée.

En bref, le programme doit prendre une liste de [nombres entiers](https://fr.wikipedia.org/wiki/Entier_naturel) en entrée, et renvoyer la somme maximale qui peut être obtenue en additionnant des entiers non adjacents, c'est-à-dire non consécutifs, dans la liste. Les contraintes supplémentaires sont que la liste d'entrée peut contenir jusqu'à 10^5 entiers, et que le programme doit avoir une complexité temporelle de O(n), c'est-à-dire qu'il doit être capable de traiter une liste de 10^5 entiers en moins d'une seconde.

Les deux programmes générés par ChatGPT et Bard fonctionnent parfaitement, toutefois, le code de Bard ne résout pas le problème correctement, et n'est pas capable de renvoyer la somme maximale. Le code de ChatGPT, quant à lui, résout le problème correctement, et renvoie la somme maximale.

## Challenge 4: Création de site web
Pour ce quatrième et dernier challenge, nous allons demander à ChatGPT et Bard de créer un site web. Nous allons leur donner une liberté totale sur le contenu du site, et leur demander de le créer en utilisant le framework de leur choix, mais en le rendant le plus esthétique possible. La requête donnée est:
> Give me the full code for a website. The content of the website is up to you, if you want you can make it about yourself, or you can make it about something else. You can use any framework you want, but make it look as good as possible. The aesthetics are the most important part.
qui se traduit par:
> Crée un site web. Le contenu du site est à toi de choisir, tu peux le faire sur toi-même, ou sur quelque chose d'autre. Tu peux utiliser n'importe quel framework, mais fais en sorte qu'il soit le plus beau possible. L'esthétique est la partie la plus importante.

Les deux programmes générés par ChatGPT et Bard fonctionnent parfaitement, toutefois, le code de Bard n'est pas très esthétique. Le code de ChatGPT, quant à lui, est correct, il n'est pas extrêmement esthétique, mais il est correct et pourrait être utilisé pour créer un site web tel quel. Nous notons que Bard a ajouté un copyright à son site web, et dans le code de ChatGPT, les pseudo-liens vers les différentes sections du site web ne fonctionnent pas. Mais ces deux erreurs sont mineures, et ne changent pas le fait que le code de ChatGPT est bien plus esthétique que celui de Bard. A noter que les images nt été ajoutées par moi, et ne sont pas présentes dans le code généré par ChatGPT.

<div class="images" style="align-items: center;">
    <div class="image" style="width: 50%;">
        <img src="/images/chatGPT-vs-bard/bard-website.png" alt="Bard's website">
        <blockquote class="image-caption">Le site web créé par Bard</blockquote>
    </div>
    <div class="image" style="width: 50%;">
        <img src="/images/chatGPT-vs-bard/chatgpt-website.png" alt="ChatGPT's website">
        <blockquote class="image-caption">Le site web créé par ChatGPT</blockquote>
    </div>
</div>

# Conclusion
Nous avons donc pu voir que ChatGPT est bien plus performant que Bard, et qu'il est capable de générer du code beaucoup plus complexe que Bard. Cependant, Bard est parfois aussi capable de générer du code correct, bien qu'il ne soit pas à la hauteur de ChatGPT. En fin de compte, peut-être que Google devrait laisser tomber le projet Bard, et se concentrer sur d'autres services, comme [Google vision](https://cloud.google.com/vision?hl=fr). Vous pouvez tester les deux chatbots en cliquant [ici pour ChatGPT](https://chat.openai.com/), et [ici pour Bard](https://bard.google.com/). Bard est encore en phase de test, et vous devez donc vous inscrire pour pouvoir l'utiliser, toutefois vous ne devriez pas avoir de problème pour vous inscrire. Je vous rappele qu vous pouvez retrouver toutes les requêtes que j'ai utilisées et les codes générés par les deux chatbots [ici](https://github.com/electronique-cc/chatgpt-vs-bard). Si vous avez des questions, n'hésitez pas à laisser un commentaire, je vous répondrai avec plaisir. Si vous avez aimé cet article, n'hésitez pas à le partager, et en attendant, je vous souhaite une bonne journée, et à bientôt!