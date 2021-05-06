# ProjectNSI_Flouret_Bernacki

AFIN DE JOUER AU JEU: telecharger tous les fichiers en zip à l'aide du gros bouton vert "code", extraire les fichiers et lancer Menu_accueilNew.py. Veuillez installer avec un pip install les modules requis (pygame, sys, random) et vous assurer que tous les fichiers du jeu sont bien dans le meme repertoire. Si vous avez le launcher python vous pouvez directement double cliquer sur le fichier et le jeu se lancera, sinon, ouvrez le avec un editeur python comme PyZo et executez le programme. Bon jeu!


Il faut désormais lancer Menu_accueilNew.py dans le dossier PokemonCombat; en effet, j'ai créé une animation de début de combat
qui m'a pris énormément de temps, j'ai réalisé toutes les nouvelles animations, et sprites, j'ai changé la musique, et j'en ai rajouté une lorsque l'on gagne.
(léger souci: cette amélioration du programme s'accompagne de vraiment beaucoup de nouveaux objets sur la fenêtre, des images et animations. Pour réaliser une suite d'action qui se suivent toutes seules, j'ai du créer aussi beaucoup d'évènements, et donc beaucoup de nouveau booléens). Tous les fichiers sont maintentant dans PokemonCombat. Le probleme de taille et de nombre de fichier maximum a été réglé.




William:

Code:
-Création système fondamental du jeu: système affichage, attaque et tours  
-Création système des vies (fonctions et variables)  
-Création du système d'animation des pokemons(code permettant de passer d'une image à l'autre)  
-Création du système de tours (maitrise du temps sur pygame)  
-Création du système des potions, allié et ennemi 
-Création mouvement des pokemon lors des attaques  
-Résolution de nombreux bugs
-Depot des fichiers volumineux (>25Mb) dans le Github à l'aide de Git Bash.
-Correction du deplacement du personnage et des transitions de partie de map --> plus fluides
-Course du personnage
-Systeme d'obstacles (un peu lourd mais fonctionnel)



Luc:

Design:
- Design et Création des Pokemon  
-Design et création des barres de vies  
-Design et création de tous les boutons (versions survol aussi, et choix des noms des boutons.)  
-Design et création de la barre de texte  
-Design et création du Titre, et animation: POKEMON dans le menu  
-Création sons et musique (pas celle du menu)  
-Création des animations des Pokemon, découpage en sprite pour fonctionnement sur pygame  
-Création police d'écriture  
-Choix des deux backgrounds (combat et menu)  
-Choix et applications des positions et dimensions des éléments sur l'écran (position et dimensions: du texte, des boutons, des pokemons des barres de vies..., résolution de certains bug d'affichage aussi)  
Code:
-Création du système de menu et sous-programme  
-Création du système du sac (avec un bug corrigé par William, le sac ne s'ouvrait que lorsque la souris restait appuyée sur le bouton)  
-Création du système de texte dynamique (ex: le nombre de vies qui descendent et le nombre de potions qui baissent)  
-Design de la Map et du personnage
-Systeme de deplacement du personnage et ses animations




Fait en commun:

-Les Pokemon s'en vont lorsqu'ils perdent  
-Choix du nombre de vies et valeurs des attaques  
-Création d'une toute première fenetre fonctionnelle (au tout début du projet)  
-Système de souris
-Ajout des nombreuses collisions de la Map








MISE A JOUR: La version du projet le plus récente se trouve dans le dossier Pokemon Combat, dans lequel il faut lancer le programme Menu_accueilNew (pour avoir une version avec le menu principal), sinon on peut directement lancer Poke_true_version, sans menu.



Voici notre projet, il faut pygame, tous les png et les fichiers son (.wav) pour l'executer.
Nous avons utilisé le module pygame, pygame.mixer, subprocess, os, sys et random.
Les animations des pokemons sont faites grace a des classes rajoutées dans un groupe "all_sprites", de cette facon il suffit de constamment mettre a jour le groupe et l'afficher et tous les pokemons se mettent a bouger a l'ecran, comme pygame ne supporte pas les fichiers GIF, on a du afficher chaque frame de l'animation à la suite, c'est pour cela qu'il y a autant d'images dans les fichiers du jeu. Chaque frame est affichée à l'aide d'une boucle qui va les passer en revue et les afficher une par une à une certaine vitesse.
Dans la boucle principale du jeu, qui dure aussi longtemps que la fenetre est ouverte, c'est a dire que le programme tourne, se trouve toutes les possibilités d'attaques, les systemes qui affichent les boutons ou pas, bref, toute la partie technique du projet ainsi que les actions possibles sur la Map. En dehors de cette boucle on va trouver la création de toutes les fonctions utilisées, les classes de sprite et de deplacement, la creation de toutes les variables, et l'importation des toutes les images en png.
Le but final est d'avoir un jeu type pokemon en 2D, avec un personnage qui se deplace sur une carte et une interface de combat ou il peut affronter un adversaire rival par un systeme de tour par tour.

Nous avons divisé notre projet en 4 parties,toutes très longues et imposantes, dans l'ordre chronologique où nous les réaliserons (Si nous avons le temps bien sûr):

1-La création d'une interface graphique de combat (fait)

2-La création et l'affichage d'une carte, principale plateforme du jeu (fait)

3-La possibilité de déplacer son personnage sur cette carte, d'avoir des interactions avec des éléments de cette carte (La partie la plus dure selon nous, mais faite!)

4-La création de l'histoire, du background de notre jeu (Vraiment à la fin fin si nous avons le temps) Cette etape risque d'etre abandonnée pour faute de temps. (pas faite)


Lien vers le Trello: https://trello.com/b/D7J5lvRh/pok%C3%A9mon-fan-game-%F0%9F%91%8D (le trello n'est plus trop utilisé, les infos dessus sont donc surement obsoletes).
