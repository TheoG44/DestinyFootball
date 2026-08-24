API Club : https://www.football-data.org/

data/
└── clubs.db
└── events.db

clubs.db
│
├── leagues
│
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

Joueur : 
- âge
- réputation (sur 5 étoiles)
- nationalité
- poste
- statistiques du joueur -> (frappes, vitesses, mental, defence, physique, discipline)
- club actuel
- Distinction individuelle (ex: Charismatique, Clutch,...)


Club :
- Tier Prestige (A,B,C puis D2,D3,N1,N2,..)
- Championnat
- Compétition auquel il participe (LDC, Europa, Conf)
- Effectif (Joueur dans le club)
- Couleur (ex: Rouge et Blanc)

Événement :
- Type (Proposition club, choix relation, choix de play pdt match,..)
- Positif ou Négatif




Saison :
- But, passee D, match joué, carton rouge & jaune
- note de la saison (0 a 10)
- Titre gagné
- gain de la saison (prime + salaire)
- objectif saison suivante


