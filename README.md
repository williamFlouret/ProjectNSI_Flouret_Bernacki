# ProjectNSI_Flouret_Bernacki
16 Février



William:

Code:
-Création système fondamental du jeu: système affichage, attaque et tours  
-Création système des vies (fonctions et variables)  
-Création du système d'animation des pokemons(code permettant de passer d'une image à l'autre)  
-Création du système de tours (maitrise du temps sur pygame)  
-Création du système des potions  
-Création mouvement des pokemon lors des attaques  
-Résolution de nombreux bugs  





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
En Cours:
-Recherche approfondie et nombreux essais de création et affichage de map pour notre jeu (design et création de la map déjà réalisé, en revanche probleme d'affichage.)  




Fait en commun:

-Les Pokemon s'en vont lorsqu'ils perdent  
-Choix du nombre de vies et valeurs des attaques  
-Création d'une toute première fenetre fonctionnelle (au tout début du projet)  
-Système de souris  








MISE A JOUR: La version du projet le plus récente se trouve dans le dossier Poke v luc recente, dans lequel il faut lancer le programme Menu accueil (pour avoir une version avec le menu principal), sinon on peut directement lancer VersionBonSac, sans menu. Concernant notre avancement, nous en sommes aux trois quart et plus, de notre interface graphique. Encore quelques éléments, et elle sera tout à fait complète. Luc, a créé la musique et les sons du combat, et a redisgné les boutons (un nouveau bouton sac est aussi présent, mais ne fonctionne pas encore très bien). William a aussi rajouté la possibilité que le pokemon ennemi fasse une attque plus puissante, mais qu'il est une chance de la rater, comme le pokemon allié peut le faire. De manière plus générale, l'interface est beaucoup plus propre, et les vrais graphismes sont présents (à part les vrais barres de vie). Nous allons de ce pas nous lancer dans le mapping d'une carte en parallèle du fignolage de notre interface graphique. Si toute fois, cette "map" ce révélait infructueuse pour quelque raison que ce soit, notre interface graphique de combat sera à la hauteur des attentes des fins de projet, d'ici la fin du temps imparti. Nous sommes toutefois convaincu que tout reste possible, puisque nous n'en sommes qu'à la moitié de ce temps imparti. En ce qui concerne le "background"du jeu, nous pensons qu'il n'est pas indispensable, et nous prévoyons de ne pas y passer de temps, pour entièrement nous concentrer sur le mapping.



Voici notre projet, il faut pygame, tous les png et les fichiers son (.wav) pour l'executer. Ne pouvant pas mettre plus de 100 fichiers dans un dossier github, les fichierts sont separés. Il faut aller chercher des images dans le fichier animation, et le reste est dans la version luc v recente. De meme, manque de place, il faut aller chercher les png nommés "tile-000", "tile-001" et ainsi de suite dans la version son et musique. Normalement il devrait tout y avoir une fois cela fait. Nous corrigerons ces defauts de place et de dossiers :)
Le but final est d'avoir un jeu type pokemon en 2D, avec un personnage qui se deplace sur une carte et une interface de combat ou il peut affronter des creatures par un systeme de tour par tour.
Pour le moment, nous n'avons qu'une interface de combat. Il y a un background et des sprites animés ainsi qu'une barre de vie modifiée au click d'un bouton (les sprites sont notres, dessinés par Luc l'artiste). Plusieurs attaques sont disponibles, chacune avec des caracteristiques differentes. Un prototype de sac pour recuperer des objets est en cours dans la version "VersionBonSac". Vous pouvez accedez a un trello pour voir notre avancement et plus de details.

Luc se concentre sur les graphismes et la musique, il a aussi commencé le systeme de sac. Tandis que William s'occupe d'ajouter de nouvelles fonctionnalités au combat (comme affichage de texte, nouvelles attaques et animations)

Nous avons divisé notre projet en 4 parties,toutes très longues et imposantes, dans l'ordre chronologique où nous les réaliserons (Si nous avons le temps bien sûr):

1-La création d'une interface graphique de combat

2-La création et l'affichage d'une carte, principale plateforme du jeu

3-La possibilité de déplacer son personnage sur cette carte, d'avoir des interactions avec des éléments de cette carte (La partie la plus dure selon nous)

4-La création de l'histoire, du background de notre jeu (Vraiment à la fin fin si nous avons le temps) Cette etape risque d'etre abandonnée pour faute de temps.

Nous situons pour l'instant vers la fin de la realisation de l'interface de combat, un peu moins loin si nous voulons vraiment qu'elle soit réussie.
Lorsque nous l'auront terminée, nous commencerons à nous intéresser à la création de la carte, et ainsi de suite...

Lien vers le Trello: https://trello.com/b/D7J5lvRh/pokémon-fan-game-👍
