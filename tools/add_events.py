import sqlite3

conn = sqlite3.connect("./data/events.db")
c = conn.cursor()

# ====================== CREATE TYPE EVENTS ====================== #
c.execute("""
    CREATE TABLE IF NOT EXISTS Media_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    type_event TEXT,
    type_effect TEXT,
    probability REAL
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Relationship_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    type_event TEXT,
    type_effect TEXT,
    probability REAL
    )
""")

# =============================================================== #




# ========================== ADD EVENT ========================== #

events_re = [

    {
        "id": 51,
        "title": "Le retard de trop",
        "description": "Vous arrivez encore en retard à l'entraînement. Le coach vous attend devant le vestiaire, bras croisés.",
        "answer_1": "Chercher une excuse",
        "effect_1": "reputation-3,mental-1",
        "comment_1": "Le coach n'est clairement pas convaincu par votre justification.",
        "answer_2": "Reconnaître votre erreur",
        "effect_2": "reputation-1,mental-1",
        "comment_2": "Votre honnêteté limite les dégâts, mais le retard reste mal vu.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 52,
        "title": "La dispute avec le capitaine",
        "description": "Le capitaine vous reproche votre attitude pendant le dernier match. Le ton monte rapidement.",
        "answer_1": "Lui répondre agressivement",
        "effect_1": "Locker room-4,mental-2",
        "comment_1": "La dispute attire plusieurs regards et crée un malaise dans le vestiaire.",
        "answer_2": "Quitter la discussion",
        "effect_2": "Locker room-2,mental-1",
        "comment_2": "Vous évitez l'affrontement, mais le problème reste entier.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 53,
        "title": "Le téléphone interdit",
        "description": "Le staff découvre que vous utilisez votre téléphone pendant une réunion tactique.",
        "answer_1": "Continuer discrètement",
        "effect_1": "reputation-3,Locker room-2",
        "comment_1": "Le coach finit par vous remarquer et vous rappelle à l'ordre.",
        "answer_2": "Ranger le téléphone sans rien dire",
        "effect_2": "reputation-1,mental-1",
        "comment_2": "Vous évitez une confrontation, mais votre manque d'attention a été remarqué.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 54,
        "title": "Le mauvais conseil",
        "description": "Un jeune coéquipier vous demande conseil avant un match. Vous lui donnez un conseil tactique qui s'avère catastrophique.",
        "answer_1": "Faire comme si de rien n'était",
        "effect_1": "mental-2,Locker room-2",
        "comment_1": "Le joueur comprend que votre conseil était mauvais et perd confiance en vous.",
        "answer_2": "Reconnaître votre erreur",
        "effect_2": "reputation-1,mental-1",
        "comment_2": "Vous assumez votre erreur, mais la confiance du joueur est déjà entamée.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 55,
        "title": "La mauvaise blague",
        "description": "Vous faites une blague sur un coéquipier devant tout le vestiaire. Vous pensiez qu'il allait rire.",
        "answer_1": "Continuer à plaisanter",
        "effect_1": "Locker room-4,reputation-2",
        "comment_1": "La blague va trop loin et votre coéquipier quitte le vestiaire.",
        "answer_2": "Vous excuser maladroitement",
        "effect_2": "Locker room-1,mental-1",
        "comment_2": "Vos excuses arrivent trop tard pour effacer complètement le malaise.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 56,
        "title": "La séance ratée",
        "description": "Vous réalisez l'une de vos pires séances depuis votre arrivée au club.",
        "answer_1": "Quitter rapidement le centre",
        "effect_1": "forme-2,mental-3",
        "comment_1": "La mauvaise séance vous reste dans la tête toute la soirée.",
        "answer_2": "Rester seul pour analyser vos erreurs",
        "effect_2": "mental-2,forme-1",
        "comment_2": "Vous ruminez tellement vos erreurs que vous en sortez épuisé.",
        "type_event": None,
        "type_effect": "-",
        "probability": 4
    },

    {
        "id": 57,
        "title": "Le vestiaire divisé",
        "description": "Une partie du vestiaire critique ouvertement une décision du coach. On vous demande de choisir un camp.",
        "answer_1": "Prendre position contre le coach",
        "effect_1": "reputation-3,Locker room-2",
        "comment_1": "Votre prise de position alimente encore davantage les tensions.",
        "answer_2": "Critiquer les joueurs qui contestent",
        "effect_2": "Locker room-3,mental-1",
        "comment_2": "Vous vous retrouvez au milieu d'un conflit qui dépasse largement le terrain.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 58,
        "title": "Le message de l'agent",
        "description": "Votre agent vous annonce qu'il a parlé de votre situation à la presse sans vous prévenir.",
        "answer_1": "L'appeler furieux",
        "effect_1": "mental-2,reputation-1",
        "comment_1": "Votre réaction risque d'alimenter encore davantage l'affaire.",
        "answer_2": "Ignorer son message",
        "effect_2": "mental-2,reputation-1",
        "comment_2": "Le silence ne règle rien et votre relation avec votre agent se dégrade.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 59,
        "title": "La soirée trop longue",
        "description": "Après une victoire, vos coéquipiers veulent prolonger la soirée alors qu'un entraînement est prévu tôt le lendemain.",
        "answer_1": "Rester jusqu'au bout",
        "effect_1": "forme-4,mental-1",
        "comment_1": "La soirée était mémorable, mais votre corps vous le fait payer le lendemain.",
        "answer_2": "Rester seulement quelques heures",
        "effect_2": "forme-2,mental-1",
        "comment_2": "Vous rentrez plus tôt, mais votre sommeil reste insuffisant.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 60,
        "title": "Le penalty manqué",
        "description": "Vous ratez un penalty décisif. Dans le vestiaire, personne ne parle.",
        "answer_1": "Vous isoler immédiatement",
        "effect_1": "mental-4,Locker room-1",
        "comment_1": "Vous vous enfermez dans votre culpabilité.",
        "answer_2": "Chercher quelqu'un à blâmer",
        "effect_2": "mental-2,Locker room-3",
        "comment_2": "Votre réaction provoque rapidement des tensions.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 61,
        "title": "La critique du père",
        "description": "Après un mauvais match, votre père vous appelle. Au lieu de vous rassurer, il vous dit : « Tu pouvais faire beaucoup mieux. »",
        "answer_1": "Vous énerver contre lui",
        "effect_1": "mental-3",
        "comment_1": "Ses paroles vous restent en tête bien plus longtemps que prévu.",
        "answer_2": "Mettre fin rapidement à l'appel",
        "effect_2": "mental-2",
        "comment_2": "Vous préférez couper court, mais ses paroles continuent de vous hanter.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 62,
        "title": "Le conflit de casier",
        "description": "Votre voisin de casier vous reproche d'utiliser trop d'espace avec vos affaires.",
        "answer_1": "Vous moquer de lui",
        "effect_1": "Locker room-3,reputation-1",
        "comment_1": "Le conflit devient personnel.",
        "answer_2": "L'ignorer complètement",
        "effect_2": "Locker room-2",
        "comment_2": "Le problème n'est pas réglé et la tension s'installe.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 63,
        "title": "La conférence désastreuse",
        "description": "Après le match, vous êtes interrogé par les journalistes. Une question vous énerve.",
        "answer_1": "Répondre avec colère",
        "effect_1": "reputation-5,mental-2",
        "comment_1": "Votre déclaration devient le sujet principal du lendemain.",
        "answer_2": "Répondre de manière sarcastique",
        "effect_2": "reputation-3,mental-1",
        "comment_2": "Votre sarcasme est largement repris sur les réseaux.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 64,
        "title": "Le réveil manqué",
        "description": "Votre réveil ne sonne pas. Vous arrivez avec près d'une heure de retard au centre d'entraînement.",
        "answer_1": "Entrer discrètement",
        "effect_1": "reputation-3,mental-1",
        "comment_1": "Tout le monde a remarqué votre arrivée tardive.",
        "answer_2": "Prévenir le coach en inventant une panne",
        "effect_2": "reputation-4,mental-1",
        "comment_2": "Le coach découvre rapidement que votre excuse ne tient pas.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 65,
        "title": "Le tacle du vétéran",
        "description": "À l'entraînement, un vétéran vous reproche de jouer trop individuellement.",
        "answer_1": "Lui répondre que vous êtes meilleur",
        "effect_1": "Locker room-4,reputation-2",
        "comment_1": "Votre réponse ne plaît absolument pas aux anciens.",
        "answer_2": "Ne rien répondre",
        "effect_2": "mental-2,Locker room-1",
        "comment_2": "Vous gardez le silence, mais sa remarque vous travaille.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 66,
        "title": "La photo compromettante",
        "description": "Une photo de vous lors d'une soirée circule sur les réseaux à quelques jours d'un match important.",
        "answer_1": "Répondre aux commentaires",
        "effect_1": "reputation-4,mental-2",
        "comment_1": "Vos réponses attirent encore plus l'attention sur la photo.",
        "answer_2": "Demander à vos amis de supprimer les publications",
        "effect_2": "reputation-2,mental-1",
        "comment_2": "La photo continue malgré tout à circuler.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 67,
        "title": "Le remplacement incompris",
        "description": "Vous êtes remplacé à la 60e minute alors que vous pensez avoir fait un bon match.",
        "answer_1": "Montrer votre colère devant le banc",
        "effect_1": "reputation-3,mental-2",
        "comment_1": "Votre réaction n'échappe ni au coach ni aux caméras.",
        "answer_2": "Refuser de serrer la main du coach",
        "effect_2": "reputation-4,Locker room-2",
        "comment_2": "Votre geste est considéré comme un manque de respect.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 68,
        "title": "La rivalité interne",
        "description": "Un coéquipier qui joue au même poste que vous commence à vous provoquer régulièrement.",
        "answer_1": "Entrer dans son jeu",
        "effect_1": "mental-2,Locker room-3",
        "comment_1": "Votre rivalité devient progressivement toxique.",
        "answer_2": "Le provoquer à votre tour",
        "effect_2": "mental-2,Locker room-4",
        "comment_2": "Le conflit prend une ampleur inutile.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 69,
        "title": "Le conseil ignoré",
        "description": "Le préparateur physique vous conseille de prendre une journée de récupération. Vous décidez de ne pas l'écouter.",
        "answer_1": "Faire une séance intense",
        "effect_1": "forme-4,mental-1",
        "comment_1": "Votre corps est épuisé et vous terminez la journée complètement vidé.",
        "answer_2": "Faire une petite séance seul",
        "effect_2": "forme-2,mental-1",
        "comment_2": "Même légère, la séance supplémentaire ralentit votre récupération.",
        "type_event": None,
        "type_effect": "-",
        "probability": 4
    },

    {
        "id": 70,
        "title": "La rumeur de transfert",
        "description": "Une rumeur affirme que vous souhaitez quitter le club. Vos coéquipiers commencent à vous poser des questions.",
        "answer_1": "Dire que vous voulez partir",
        "effect_1": "Locker room-4,reputation-3",
        "comment_1": "Votre déclaration fragilise votre position dans le vestiaire.",
        "answer_2": "Nier agressivement",
        "effect_2": "reputation-2,mental-2",
        "comment_2": "Votre réaction défensive laisse planer davantage de doutes.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 71,
        "title": "Le repas oublié",
        "description": "Vous réalisez que vous avez complètement oublié de préparer votre repas avant une longue journée d'entraînement.",
        "answer_1": "Manger n'importe quoi rapidement",
        "effect_1": "forme-3,mental-1",
        "comment_1": "Votre alimentation improvisée vous laisse sans énergie.",
        "answer_2": "Ne presque rien manger",
        "effect_2": "forme-4,mental-2",
        "comment_2": "Vous manquez clairement d'énergie pendant la séance.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 72,
        "title": "Le vestiaire silencieux",
        "description": "Après une lourde défaite, vous sentez que le groupe est complètement démoralisé.",
        "answer_1": "Vous isoler",
        "effect_1": "mental-3,Locker room-2",
        "comment_1": "Votre silence renforce votre propre sentiment d'isolement.",
        "answer_2": "Critiquer les autres joueurs",
        "effect_2": "mental-2,Locker room-4",
        "comment_2": "Vos critiques divisent encore davantage le groupe.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 73,
        "title": "Le rendez-vous manqué",
        "description": "Votre agent vous attend depuis trente minutes pour discuter de votre prochain contrat.",
        "answer_1": "Arriver sans prévenir",
        "effect_1": "reputation-2,mental-1",
        "comment_1": "Votre agent est particulièrement agacé.",
        "answer_2": "Annuler au dernier moment",
        "effect_2": "reputation-3,mental-1",
        "comment_2": "Votre agent commence à douter de votre sérieux.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 74,
        "title": "Le mauvais vestiaire",
        "description": "Après un déplacement, vous entrez par erreur dans le vestiaire adverse alors que l'équipe vous attend ailleurs.",
        "answer_1": "Faire comme si de rien n'était",
        "effect_1": "reputation-2,Locker room-1",
        "comment_1": "L'anecdote fait rire certains, mais vous passez pour quelqu'un de distrait.",
        "answer_2": "Vous énerver contre ceux qui vous indiquent le chemin",
        "effect_2": "reputation-2,Locker room-2",
        "comment_2": "Votre mauvaise humeur rend la situation encore plus gênante.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 75,
        "title": "Le commentaire du coach",
        "description": "Le coach vous dit que vous n'êtes actuellement pas au niveau attendu.",
        "answer_1": "Vous remettre complètement en question",
        "effect_1": "mental-4,reputation-1",
        "comment_1": "Ses paroles vous touchent plus profondément que prévu.",
        "answer_2": "Prendre sa remarque personnellement",
        "effect_2": "mental-3,Locker room-1",
        "comment_2": "Vous commencez à accumuler de la frustration envers le staff.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 76,
        "title": "Le coéquipier oublié",
        "description": "Vous organisez une sortie avec plusieurs joueurs mais oubliez volontairement un coéquipier avec qui vous êtes en froid.",
        "answer_1": "Assumer de l'avoir exclu",
        "effect_1": "Locker room-4,reputation-2",
        "comment_1": "L'affaire fait rapidement le tour du vestiaire.",
        "answer_2": "Prétendre que vous l'avez oublié",
        "effect_2": "Locker room-2,mental-1",
        "comment_2": "Votre excuse ne convainc personne.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 77,
        "title": "La nuit blanche",
        "description": "Impossible de dormir avant un match important. Vous passez une grande partie de la nuit à regarder votre téléphone.",
        "answer_1": "Continuer à regarder les réseaux",
        "effect_1": "forme-3,mental-2",
        "comment_1": "Au réveil, vous êtes épuisé et mentalement saturé.",
        "answer_2": "Vous lever et regarder un film",
        "effect_2": "forme-2,mental-2",
        "comment_2": "Vous ne récupérez quasiment pas avant le match.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 78,
        "title": "La comparaison permanente",
        "description": "Les médias vous comparent constamment à un jeune joueur de votre génération qui connaît une meilleure saison.",
        "answer_1": "Passer des heures à regarder ses statistiques",
        "effect_1": "mental-4,reputation-1",
        "comment_1": "La comparaison devient une obsession.",
        "answer_2": "Répondre aux journalistes",
        "effect_2": "mental-2,reputation-3",
        "comment_2": "Votre réponse révèle votre frustration.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    },

    {
        "id": 79,
        "title": "Le match oublié",
        "description": "Vous pensiez avoir un jour de repos mais le staff avait programmé une séance importante.",
        "answer_1": "Arriver très en retard",
        "effect_1": "reputation-4,mental-1",
        "comment_1": "Le staff est furieux de votre absence.",
        "answer_2": "Ne pas venir du tout",
        "effect_2": "reputation-5,Locker room-2",
        "comment_2": "Votre absence est considérée comme une faute professionnelle.",
        "type_event": None,
        "type_effect": "-",
        "probability": 2
    },

    {
        "id": 80,
        "title": "La colère après match",
        "description": "Après une nouvelle défaite, vous êtes furieux et un coéquipier tente de vous parler.",
        "answer_1": "L'envoyer balader",
        "effect_1": "Locker room-3,mental-2",
        "comment_1": "Votre colère blesse un coéquipier qui voulait simplement vous aider.",
        "answer_2": "Quitter immédiatement le vestiaire",
        "effect_2": "Locker room-2,mental-2",
        "comment_2": "Vous vous isolez au lieu de partager votre frustration avec le groupe.",
        "type_event": None,
        "type_effect": "-",
        "probability": 3
    }
]

for i in range(len(events_re)):
  c.execute("""
      INSERT INTO Relationship_Events 
      VALUES (
          :id,
          :title,
          :description,
          :answer_1,
          :effect_1,
          :comment_1,
          :answer_2,
          :effect_2,
          :comment_2,
          :type_event,
          :type_effect,
          :probability
      )
  """, events_re[i])

conn.commit()
conn.close()

# =============================================================== #

