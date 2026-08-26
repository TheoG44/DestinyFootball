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
- Creer event Mercato (nv salaire, club, prime signature)
- rajouter fortune joueur dans param joueur
- Creer un choix de s'entrainer pour gagner stats
- creer fonction pour bilan de fin saison saison.py
- creer historique de saison (stats, trophe de chaque saison)
- comment le joueur influence les resultat de son club
- ajouter des logs (import loggings)
- ajouter system d'historique


tier d2, (c, b, a, S) = D1