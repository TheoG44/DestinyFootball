API Club : https://www.football-data.org/

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

.gitignore
__main__.py
notes.md
requierements.txt

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

- Rajouter colonne tier + renseigner colonne
- Enrichir BDD Events
- Creer script pour traduire effets
- Rajouter comment_1, comment_2 (texte suite au réponse choisi) 
