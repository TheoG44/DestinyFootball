API Club : 
https://www.football-data.org/
https://www.api-football.com/ 
https://www.thesportsdb.com/

────────────────────────────────────────────────
envdes/

data/
└── clubs.db
└── events.db

tools/
└── add_clubs.py
└── add_events.py

utils/
└── events.py
└── player.py

clubs.db
└──leagues
└── clubs

events.db
│
├── event_types
│
├── media_events
├── training_events
├── career_events
├── transfer_events
└── ...

──────────────────────────────────────────────────────

Eléments :
- Joueur
- Club
- Événement
- Saison
- statistique saison précédentes
- Palmares
- salaire
- gain globaux
- Notes générale -> relier aux stats
- contrat restant avc le club

──────────────────────────────────────────────────────
BUG a PATCH

- choix aleatoire de 2x le mm club


──────────────────────────────────────────────────────
To Do List

-/ Rajouter colonne tier + renseigner colonne + affichage tier
-/ Creer script pour traduire effets de Events
-/ Rajouter comment_1, comment_2 (texte suite au réponse choisi) 
- Enrichir BDD Events (Avec nv type d'event)
-/ rajouter année de contrat a joueur et mettre a jour a club de depart et nv club
-/ Creer event Mercato (nv salaire, club, prime signature)
- creer fonction pour bilan de fin saison saison.py
- creer historique de saison (stats, trophe de chaque saison)
- comment le joueur influence les resultat de son club
- ajouter des logs (import loggings)
- ajouter system d'historique
-/ armoniser nom effet des tables events
-/ rajouter année de contrat restant et gain totaux de player

- créer events blessure (+ plus probabilité arriver si forme -50)
- Creer events de s'entrainer pour gagner stats

Faire si le joueur est dans un club S et fais un saison au dessus de 7/10, 80% gagner sa league


Ajouter systeme de classement dans la saison du club du joueur, 
les choix de FootballMoment influent les classement,
1 footballMoment par match et 10 match par saison.
+ ajouter fonction affiche classment de la ligue

Ajouter event de selection. Systeme coupe du monde.



tier d2, (c, b, a, S) = D1