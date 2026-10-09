# 🐍 Cours LaSalle — Manipulation et Analyse de Données avec Python (NumPy & Pandas)

Bienvenue dans le dépôt officiel du cours **Manipulation et Analyse de Données avec Python**. 

Ce programme intensif de **14 heures (2 jours)** est conçu pour des étudiants de niveau **Master** possédant déjà les bases de la programmation en Python et souhaitant acquérir des compétences professionnelles en **Manipulation de données avec Python***

---

## 🎯 Objectifs Pédagogiques

À l'issue de cette formation, vous serez capables de :
1. **Adopter avec **NumPy** pour effectuer des calculs scientifiques à haute performance sans boucles lentes.
2. **Manipuler, nettoyer et transformer des jeux de données complexes** avec **Pandas** (gestion des `NaN`, doublons, types de données, ccréation de nouvelles variables).
3. **Réaliser des agrégations avancées** (fonctions `groupby`, tableaux croisés dynamiques / *pivot tables*, fenêtrages).
4. **Fusionner et structurer des données multi-tables** (`merge`, `join`, `concat`).
5. **Conduire une Analyse Exploratoire de Données (EDA)** complète sur un jeu de données réel et présenter des synthèses visuelles et chiffrées.
6. **Préparer la transition vers le Big Data** : les concepts manipulés ici sur des fichiers locaux constituent le socle direct du prochain cours d'**Introduction au Big Data**

---

## 🛍️ Fil Rouge : *TheLook eCommerce*

Tout au long des exercices et du projet final, vous travaillerez sur des données réelles d'une boutique en ligne : **TheLook eCommerce** (dataset public hébergé sur Google BigQuery).

Le jeu de données couvre :
- **Utilisateurs** (`thelook_users.csv`) : profils, géographie, canaux d'acquisition.
- **Produits** (`thelook_products.csv`) : catalogue, catégories, prix de vente et coûts.
- **Commandes & Articles** (`thelook_orders.csv`, `thelook_order_items.csv`) : paniers, transactions, dates et statut de livraison.

---

## 📚 Programme des Notebooks (`02_notebooks/`)

Le cours est découpé en 9 modules progressifs :

| # | Notebook | Thématiques couvertes |
| :-: | :--- | :--- |
| **00** | [`00_introduction_et_configuration.ipynb`](02_notebooks/00_introduction_et_configuration.ipynb) | Configuration de l'environnement avec `uv`, VS Code & validation |
| **01** | [`01_numpy_pensee_vectorielle.ipynb`](02_notebooks/01_numpy_pensee_vectorielle.ipynb) | Tableaux `ndarray`, vectorisation, *broadcasting*, masques booléens & `dtype` |
| **02** | [`02_pandas_premiers_pas.ipynb`](02_notebooks/02_pandas_premiers_pas.ipynb) | Structure des `Series` & `DataFrame`, indexation, filtres `.loc[]` / `.iloc[]` |
| **03** | [`03_transformations_feature_engineering.ipynb`](02_notebooks/03_transformations_feature_engineering.ipynb) | Mutateurs, conversion `.astype()`, accesseur temporel `.dt`, tri et masques |
| **04** | [`04_exercice_integrateur.ipynb`](02_notebooks/04_exercice_integrateur.ipynb) | Mise en pratique guidée des notions des modules 01 à 03 |
| **05** | [`05_nettoyage_donnees.ipynb`](02_notebooks/05_nettoyage_donnees.ipynb) | Traitement des valeurs manquantes (`NaN`), dédoublonnage, valeurs aberrantes |
| **06** | [`06_agregation_groupby_pivots.ipynb`](02_notebooks/06_agregation_groupby_pivots.ipynb) | Groupements `.groupby()`, fonctions d'agrégation et `pivot_table` |
| **07** | [`07_complements_merge_export_viz.ipynb`](02_notebooks/07_complements_merge_export_viz.ipynb) | Jointures (`pd.merge`), concaténation, visualisations et exports |
| **08** | [`08_capstone_eda_thelook.ipynb`](02_notebooks/08_capstone_eda_thelook.ipynb) | **Projet Capstone** : Analyse Exploratoire complète du dataset *TheLook* |

---

## 📁 Arborescence du Projet

```text
cours_lasalle/
├── 01_data/
│   ├── raw/              # Exports bruts (CSV) — Ne jamais modifier
│   ├── prepared/         # Datasets modifiés pendant le cours
│   ├── exercises/        # Jeux de données dédiés aux exercices
│   └── capstone/         # Dataset enrichi pour le projet final
├── 02_notebooks/         # Notebooks Jupyter (00 à 08)
├── 03_analysis/
│   ├── graphs/           # Visualisations exportées (PNG, SVG)
│   └── reports/          # Rapports de synthèse et exports CSV
├── src/                  # Scripts et modules Python auxiliaires
├── pyproject.toml        # Dépendances du projet (Pandas, NumPy, Matplotlib, IPykernel)
├── uv.lock               # Verrouillage précis des versions des dépendances
└── README.md             # Documentation générale (vous êtes ici)
```

---

## ⚙️ Guide d'Installation & Lancement

Le projet utilise **`uv`**, le gestionnaire de paquets et d'environnements virtuel ultra-rapide écrit en Rust.

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-compte/cours_lasalle.git
cd cours_lasalle
```

### 2. Créer et synchroniser l'environnement virtuel avec `uv`
```bash
# 1. Créer l'environnement virtuel (.venv)
uv venv

# 2. Activer l'environnement
# Sur macOS / Linux :
source .venv/bin/activate
# Sur Windows (PowerShell) :
.venv\Scripts\activate

# 3. Installer les dépendances du projet
uv sync
```

### 3. Ouvrir dans VS Code
```bash
code .
```

1. Dans **VS Code**, ouvrez l'un des notebooks du dossier `02_notebooks/`.
2. Assurez-vous d'avoir l'extension **Jupyter** installée (onglet *Extensions* ou `Ctrl + Shift + X`).
3. Sélectionnez l'interpréteur Python : ouvrez la palette de commandes avec `Ctrl + Shift + P` (ou `Cmd + Shift + P` sur Mac), tapez **`Python: Select Interpreter`** et sélectionnez l'environnement **`.venv`** (ou cliquez sur **Select Kernel** en haut à droite du notebook).
4. Vous êtes prêt à exécuter les cellules avec `Shift + Enter` !

---

## 🛠️ Stack Technique

- **Python** : `>= 3.13`
- **Environnement & Paquets** : [`uv`](https://docs.astral.sh/uv/)
- **Calcul Vectoriel** : `numpy`
- **Analyse & Manipulation** : `pandas`
- **Visualisation** : `matplotlib` / `seaborn`
- **Éditeur recommandé** : Visual Studio Code (avec extensions *Python* et *Jupyter*)
