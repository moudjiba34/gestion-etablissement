DROP TABLE IF EXISTS classe;
DROP TABLE IF EXISTS eleve;

CREATE TABLE classe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  niveau TEXT NOT NULL,
  designation TEXT ,
  capacite INTEGER  NOT NULL
);

CREATE TABLE eleve (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nom TEXT NOT NULL,
  prenom TEXT NOT NULL,
  age INTEGER NOT NULL,
  classe_id INTEGER NOT NULL,
  FOREIGN KEY (classe_id) REFERENCES classe (id)
);

-- INSERT INTO classe(niveau,designation,capacite)
--   VALUES("Terminale","Terminale_A",50),
--         ("Terminale","Terminale_B",50),
--         ("Terminale","Terminale_C",50),
--         ("Premiere","Premiere_A",50),
--         ("Premiere","Premiere_B",50),
--         ("Second","Second_C",50),
--         ("Second","Second_C",50),
--         ("Second","Second_C",50);
-- INSERT INTO eleve(nom,prenom,age, classe_id)
--   VALUES("Ndiaye","Modou",17,2),
--         ("Diallo","Weuze",18,1),
--         ("Fall","Ousmane",16,2),
--         ("Dia","Lamine",16,5),
--         ("Sakho","Moussa",15,5),
--         ("Niang","Saly",20,5),
--         ("Seye","Codou",14,1),
--         ("Diallo","Fatou",20,1);