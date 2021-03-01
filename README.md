# ProjectNSI_Flouret_Bernacki
1 Mars

poke v luc récente obsolète
Il faut désormais lancer Menu_accueil2.py ou Pokemon_Interface_GénésisTrue.py dans le dossier PokemonCombat; en effet, j'ai créé une animation de début de combat
qui m'a pris énormément de temps, j'ai réalisé toutes les nouvelles animations, et sprites, j'ai changé la musique, et j'en ai rajouté une lorsque l'on gagne.
(2 légers soucis: cette amélioration du programme s'accompagne de vraiment beaucoup de nouveaux objets sur la fenêtre, des images et animations. Pour réaliser une suite d'action qui se suivent toutes seules, j'ai du créer aussi beaucoup d'évènements, et donc beaucoup de nouveau booléens, pour une raison qui m'est inconnue, lorsque l'on peut finalement combattre, les actions sont plus lentes, l'ennemi met plus de temps à attaquer; en soit ce n'est pas un problème puisque le combat est seulement un petit peu ralenti, mais j'aimerais comprendre pourquoi. 2ème petit soucis: la nouvelle musique (qui avouons-le est meilleure que la précédente) couvre beaucoup plus les autres sons (attaques etc...) que la précédente musique et je ne sais pas pourquoi non-plus. Tous les fichiers sont maintentant dans PokemonCombat. En raison d'un nombre maximum de fichiers uploadés en une seule fois, j'ai du uploader les fichiers en plusieurs fois, il faut donc aussi impérativement prendre les fichiers de PokemonCombat1 et PokemonCombat2 aussi, situés dans PokemonCombat.
En second temps, j'ai rajouté une section Mapping pour que vous puissiez nous éclairer sur ce qui ne vas pas pour la Map. En l'état pour moi, aucun des deux programmes ne fonctionnent: JeuMap.py et JeuMap copie.py, ils affichent tout deux en erreur: Unsupported image format (erreur assez étonnante puisque les deux programmes sont conçus en partie pour  que le .tmx puisse être supporté, et d'une autre partie pour qu'il puisse être affiché.) De plus, après avoir sondé internet, la façon dont j'ai codé les deux programmes (les deux programmes font la même chose mais j'ai essayé deux manières différentes) est censé être la bonne. Un point important est qu'il semble que l'erreur vienne d'un programme lancé par le module .pytmx, et non pas mon programme, j'ai pu l'observer mais je ne vois pas comment résoudre l'erreur. J'éspère chez vous que vous puissiez ouvrir les programmes lancés par des modules car cela s'avère très utile pour moi, pour comprendre la source des erreurs. P.S: il faut installer le module pytmx, et mettre sa version de python à 3.7; car 3.9 ne supporte visiblement pas .pytmx











16 Février



William:

Code:
-Création système fondamental du jeu: système affichage, attaque et tours  
-Création système des vies (fonctions et variables)  
-Création du système d'animation des pokemons(code permettant de passer d'une image à l'autre)  
-Création du système de tours (maitrise du temps sur pygame)  
-Création du système des potions, allié et ennemi 
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








MISE A JOUR: La version du projet le plus récente se trouve dans le dossier Poke v luc recente, dans lequel il faut lancer le programme Menu accueil (pour avoir une version avec le menu principal), sinon on peut directement lancer VersionBonSac, sans menu. Concernant notre avancement, nous en sommes aux trois quart et plus, de notre interface graphique. Encore quelques éléments, et elle sera tout à fait complète. Luc, a créé la musique et les sons du combat, et a redisgné les boutons. William a aussi rajouté la possibilité que le pokemon ennemi fasse une attque plus puissante, mais qu'il est une chance de la rater, comme le pokemon allié peut le faire. Le pokemon ennemi peut aussi se soigner 2 fois lors d'un combar s'il n'a plus beaucoup de points de vie. De manière plus générale, l'interface est beaucoup plus propre, et les vrais graphismes sont présents (à part le vrai pokemon ennemi, qui sera dessiné par Luc). Nous allons de ce pas nous lancer dans le mapping d'une carte en parallèle du fignolage de notre interface graphique. Si toute fois, cette "map" ce révélait infructueuse pour quelque raison que ce soit, notre interface graphique de combat sera à la hauteur des attentes des fins de projet, d'ici la fin du temps imparti. Nous sommes toutefois convaincu que tout reste possible. En ce qui concerne le "background"du jeu, nous pensons qu'il n'est pas indispensable, et nous prévoyons de ne pas y passer de temps, pour entièrement nous concentrer sur le mapping.



Voici notre projet, il faut pygame, tous les png et les fichiers son (.wav) pour l'executer.
Nous avons utilisé le module pygame, subprocess, os, sys et random.
Les animations des pokemons sont faites grace a des classes rajoutées dans un groupe "all_sprites", de cette facon il suffit de constamment mettre a jour le groupe et l'afficher et tous les pokemons se mettent a bouger a l'ecran.
Dans la boucle principale du jeu, qui dure aussi longtemps que la fenetre est ouverte, c'est a dire que le programme tourne, se trouve toutes les possibilités d'attaques, les systemes qui affichent les boutons ou pas, bref, toute la partie technique du projet. En dehors de cette boucle on va trouver la création de toutes les fonctions utilisées, les classes de sprite, la creation de toutes les variables, et l'importation des toutes les images en png.
Le but final est d'avoir un jeu type pokemon en 2D, avec un personnage qui se deplace sur une carte et une interface de combat ou il peut affronter des creatures par un systeme de tour par tour.
Pour le moment, nous n'avons qu'une interface de combat. Il y a un background et des sprites animés ainsi qu'une barre de vie modifiée au click d'un bouton (les sprites sont notres, dessinés par Luc l'artiste). Plusieurs attaques sont disponibles, chacune avec des caracteristiques differentes. Un prototype de sac pour recuperer des objets est en cours dans la version "VersionBonSac". Vous pouvez accedez a un trello pour voir notre avancement et plus de details.

Luc se concentre sur les graphismes et la musique, qui sont presque tous finis! Tandis que William s'occupe d'ajouter de nouvelles fonctionnalités au combat (comme affichage de texte, nouvelles attaques et animations, potions, attaques qui permettent au pokemon de se defendre, etc...)

Nous avons divisé notre projet en 4 parties,toutes très longues et imposantes, dans l'ordre chronologique où nous les réaliserons (Si nous avons le temps bien sûr):

1-La création d'une interface graphique de combat

2-La création et l'affichage d'une carte, principale plateforme du jeu

3-La possibilité de déplacer son personnage sur cette carte, d'avoir des interactions avec des éléments de cette carte (La partie la plus dure selon nous)

4-La création de l'histoire, du background de notre jeu (Vraiment à la fin fin si nous avons le temps) Cette etape risque d'etre abandonnée pour faute de temps.

Nous situons pour l'instant vers la fin de la realisation de l'interface de combat, un peu moins loin si nous voulons vraiment qu'elle soit réussie. Luc se penche sur la carte, il y rencontre quelques soucis mais bientot elle devrait etre fonctionnelle, on se concentrera donc tous les deux bientot sur le deplacement du personnage et les liens a faire avec l'inetrface de combat.

Lien vers le Trello: https://trello.com/b/D7J5lvRh/pok%C3%A9mon-fan-game-%F0%9F%91%8D (le trello n'est plus trop utilisé, les infos dessus sont donc surement obsoletes).
