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


c.execute("""
    CREATE TABLE IF NOT EXISTS Training_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    post TEXT NOT NULL,
    type_event TEXT,
    probability REAL
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Injury_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    effect TEXT NOT NULL,
    comment TEXT NOT NULL,
    type_event TEXT,
    tier TEXT,
    probability REAL
    )
""")


# =============================================================== #




# ========================== ADD EVENT ========================== #
events = [
    {
        "id": 61,
        "title": "Rupture des croisés",
        "description": "Sur un changement brutal de direction, votre genou tourne tandis que votre pied reste bloqué dans la pelouse.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. Une longue rééducation commence.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 62,
        "title": "Rupture du tendon d'Achille",
        "description": "Lors d'une accélération, une douleur brutale derrière votre cheville vous arrête net.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 9 mois. Saison terminée. Retour long et particulièrement exigeant.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 63,
        "title": "Fracture du tibia",
        "description": "Un duel extrêmement violent se termine par un choc qui vous oblige à quitter immédiatement le terrain.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. Plusieurs mois seront nécessaires avant de retrouver les terrains.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 64,
        "title": "Fracture du péroné",
        "description": "Votre jambe encaisse un contact important pendant un match et la douleur vous empêche immédiatement de continuer.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison compromise. Une longue période de récupération vous attend.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 65,
        "title": "Double blessure au genou",
        "description": "Une mauvaise réception provoque une importante torsion du genou. Les examens révèlent plusieurs structures touchées.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 10 mois. Saison terminée. Rééducation longue et retour progressif.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 66,
        "title": "Fracture de la cheville",
        "description": "Votre cheville se retrouve prise sous votre poids lors d'un duel. Les médecins comprennent rapidement que la blessure est sérieuse.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison terminée. Plusieurs mois de récupération.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 67,
        "title": "Rupture musculaire majeure",
        "description": "Vous tentez une accélération maximale lorsque votre cuisse cède brutalement.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. La blessure est beaucoup plus sérieuse que prévu.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 68,
        "title": "Fracture du fémur",
        "description": "Un choc extrêmement violent lors d'un match provoque une grave blessure à la cuisse.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 12 mois. Saison terminée. Une très longue rééducation sera nécessaire.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 69,
        "title": "Genou détruit sur un tacle",
        "description": "Un tacle arrive sur votre jambe d'appui alors que votre corps part dans la direction opposée.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 10 mois. Saison terminée. Plusieurs structures du genou sont touchées.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 70,
        "title": "Grave blessure à l'épaule",
        "description": "Une chute spectaculaire lors d'un duel aérien provoque une importante lésion de l'épaule.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. Une opération et une longue rééducation sont nécessaires.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 71,
        "title": "Fracture du bassin",
        "description": "Un choc violent lors d'un duel vous projette lourdement au sol. Les examens révèlent une fracture importante.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 9 mois. Saison terminée. Le retour devra être extrêmement progressif.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 72,
        "title": "Rupture des ischio-jambiers",
        "description": "Sur une accélération en contre-attaque, votre cuisse arrière lâche complètement.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison terminée. Une longue réathlétisation vous attend.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 73,
        "title": "Grave fracture du pied",
        "description": "Votre pied reste coincé sous un adversaire lors d'un duel. La blessure est immédiatement inquiétante.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. Opération et rééducation nécessaires.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 74,
        "title": "Rupture ligamentaire",
        "description": "Votre genou part dans une position anormale après un contact en plein match.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. Une reconstruction ligamentaire est nécessaire.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 75,
        "title": "Blessure à l'entraînement",
        "description": "Lors d'une opposition anodine, votre pied se bloque et votre genou subit une torsion importante.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 9 mois. Saison terminée. Le football devra attendre.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 76,
        "title": "Accident domestique",
        "description": "Une chute malheureuse dans votre vie privée provoque une grave blessure à la jambe.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison compromise. Le club devra patienter avant votre retour.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 77,
        "title": "Accident à vélo",
        "description": "Une chute à vélo pendant votre jour de repos vous laisse avec une importante blessure à l'épaule et au bras.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. Votre retour au football sera long et progressif.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 78,
        "title": "Grave blessure au genou",
        "description": "Après un appui mal contrôlé, votre genou subit une torsion importante. Les examens sont sans appel.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 10 mois. Saison terminée. Une reconstruction est nécessaire.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 79,
        "title": "Fracture complexe de la cheville",
        "description": "Un duel se termine par une réception catastrophique. Votre cheville est gravement touchée.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 9 mois. Saison terminée. Plusieurs mois de rééducation.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 80,
        "title": "Rupture du tendon rotulien",
        "description": "Lors d'une détente explosive, votre genou cède brutalement et vous devez être évacué.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. La rééducation sera particulièrement longue.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 81,
        "title": "Grave blessure au mollet",
        "description": "Une accélération à pleine vitesse provoque une importante lésion musculaire.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. La saison est fortement compromise.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 82,
        "title": "Fracture de fatigue avancée",
        "description": "Une douleur ignorée pendant plusieurs semaines finit par devenir une véritable fracture.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison terminée. Une longue période sans football commence.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 83,
        "title": "Blessure grave en musculation",
        "description": "Une charge mal maîtrisée lors d'une séance de musculation provoque une grave blessure à la jambe.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. La récupération sera longue.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 84,
        "title": "Choc violent contre le poteau",
        "description": "En tentant de sauver un ballon, vous percutez violemment le poteau. La blessure nécessite une prise en charge immédiate.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. Plusieurs mois de récupération avant un retour complet.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 85,
        "title": "Grave blessure musculaire",
        "description": "Après plusieurs semaines de calendrier infernal, votre corps finit par céder lors d'un sprint.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 7 mois. Saison terminée. Le staff reconnaît avoir peut-être trop tiré sur votre organisme.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 86,
        "title": "Collision aérienne",
        "description": "Vous percutez violemment un adversaire lors d'un duel aérien et retombez lourdement.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. Une blessure sérieuse nécessite une longue récupération.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 87,
        "title": "Grave lésion de la hanche",
        "description": "Une mauvaise chute pendant un match provoque une blessure profonde à la hanche.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 8 mois. Saison terminée. Le retour devra être extrêmement progressif.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 88,
        "title": "Tendon gravement endommagé",
        "description": "Une douleur négligée depuis plusieurs semaines se transforme en blessure majeure lors d'un entraînement.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 9 mois. Saison terminée. Une longue rééducation est inévitable.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 89,
        "title": "Accident pendant un déplacement",
        "description": "Un accident pendant un déplacement de l'équipe vous laisse avec une blessure importante nécessitant une hospitalisation.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 6 mois. Votre saison est terminée et votre retour sera très progressif.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    },
    {
        "id": 90,
        "title": "Le cauchemar du dernier match",
        "description": "Alors que votre équipe joue un match décisif, votre genou lâche sur un simple changement d'appui. Le stade entier comprend immédiatement que quelque chose ne va pas.",
        "effect": "mental-10,forme+20",
        "comment": "ABSENCE : 10 mois. Saison terminée. Le verdict est lourd : longue rééducation et plusieurs mois loin des terrains.",
        "type_event": "Injury",
        "tier": "C",
        "probability": 1
    }
]
# ====================== INSERT DICT TO TABLE ====================== #

for i in range(len(events)):
  c.execute("""
      INSERT INTO Injury_Events 
      VALUES (
          :id,
          :title,
          :description,
          :effect,
          :comment,
          :type_event,
          :tier,
          :probability
      )
  """, events[i])

conn.commit()
conn.close()

# =============================================================== #

