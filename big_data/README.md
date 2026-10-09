# 🚀 Formation Intensive : Initiation au Big Data & Data Engineering sur GCP (21h)

Bienvenue dans le dépôt du cours **Initiation au Big Data & Data Engineering** (3 jours / 21h).

Cette formation est axée à **80% sur la pratique** et s'appuie sur l'écosystème **Google Cloud Platform (GCP)**, les cas pratiques sont inspirés de labs officiels **Google Cloud Skills Boost**, et des outils modernes de Data Engineering (**BigQuery, dlt, dbt, Looker Studio, GitHub Actions**).

---

## 📅 Programme du Cours, Slides & Labs

### 🟢 Jour 1 : Comprendre, stocker, ingérer (7h)

| Module | Durée | Type | Supports & Contenu |
| :--- | :---: | :---: | :--- |
| **1.1 Le paradigme Big Data** | 1h15 | Théorie + Démo | 📊 [Slides Théo 1.1](02_cours/day1_ingestion/theorie/01_slides_paradigme_bigdata.md)<br>Les 5V, OLTP vs OLAP, calcul distribué, découplage stockage/calcul (Serverless/PaaS Data), Lake / DWH / Lakehouse, introduction à `dbt`. |
| **1.2 GCP, coûts, gouvernance** | 0h45 | Mixte | 🧪 [Lab 1.2 : Gouvernance, IAM & Budget (Notebook)](02_cours/day1_ingestion/labs/02_lab_gcp_iam_budget_setup.ipynb)<br>Projets GCP, IAM, résidence des données en EU (RGPD), modèle de tarification BigQuery & Cloud Storage, configuration d'alertes budgétaires en direct. |
| **1.3 Prise en main BigQuery** | 0h30 | Pratique | 🧪 [Lab 1.1 & 1.3 : OLAP, Stockage en Colonnes et UI (Notebook)](02_cours/day1_ingestion/labs/01_lab_bigquery_olap_and_dry_run.ipynb)<br>Cloud Shell Editor / VS Code local + CLI `gcloud` & `bq`. Requêtes sur datasets publics, utilisation du **Dry Run** pour estimer le coût des requêtes. |
| **1.4 Lake vs Data Warehouse** | 1h15 | Pratique | 🧪 [Lab Data Lake & Tables Externes (Notebook)](02_cours/day1_ingestion/labs/03_lab_data_lake_and_external_tables.ipynb)<br>Création de buckets GCS, stockage de logs JSON, création de **Tables Externes**, chargement en **Tables Natives BigQuery**. |
| **1.5 ELT & Ingestion avec `dlt`** | 3h15 | Théorie (30m) + Pratique | 🧪 [Lab Qwiklabs Loading Data into BQ](02_cours/day1_ingestion/labs/05_lab_qwiklabs_loading_data_into_bigquery.md) & 📚 [Lab Ingestion dlt](02_cours/day1_ingestion/labs/06_ingestion_intro_dlt.ipynb)<br>Ingestion d'API REST vers BigQuery (Couche **Bronze**), gestion de la *schema evolution* et chargement incrémental.<br>*(Tutoriels dlt avancés disponibles dans `02_cours/day1_ingestion/bonus/`)*. |

---

### 🟡 Jour 2 : Analyser et transformer (7h)

| Module | Durée | Type | Supports & Contenu |
| :--- | :---: | :---: | :--- |
| **2.1 Modélisation & Architecture Medallion** | 1h00 | Théorie | 📊 [Slides Théo 2.1](02_cours/day2_transformation/theorie/02_slides_medallion_et_modelisation.md)<br>Architecture Medallion (**Bronze, Silver, Gold**), Modélisation dimensionnelle (Kimball) vs Dénormalisation BigQuery, Partitionnement & Clustering, Transformations SQL planifiées. |
| **2.2 Transformations SQL & Planification** | 3h30 | Pratique | 🧪 [Lab Transformations SQL & Planifiées (Notebook)](02_cours/day2_transformation/labs/02_lab_sql_transformations_planifiees.ipynb)<br>Écriture des requêtes de transformation SQL (Bronze ➔ Silver ➔ Gold), manipulation analytique et automatisation via **Scheduled Queries** (requêtes planifiées BigQuery). |
| **2.3 Bonus : SQL Semi-structuré & Projet dbt** | 2h30 | Pratique / Bonus | 🧪 [Lab JSON & Arrays](02_cours/day2_transformation/bonus/02_lab_qwiklabs_analyzing_json_arrays_nested.md) & 📚 [Projet dbt BigQuery](02_cours/day2_transformation/bonus/04_lab_dbt_bigquery.ipynb)<br>Manipulation avancée (`UNNEST`, `STRUCT`, `ARRAY_AGG`), fonctions de fenêtrage, et projet complet dbt (modèles, documentation et exécution). |

---

### 🔴 Jour 3 : Fiabiliser, orchestrer, évaluer (7h)

| Module | Durée | Type | Supports & Contenu |
| :--- | :---: | :---: | :--- |
| **3.1 Orchestration & Approche Serverless** | 1h00 | Théorie | 📊 [Slides Théo 3.1](02_cours/day3_production/theorie/03_slides_orchestration_serverless.md)<br>Concepts d'orchestration moderne de workflows data, pourquoi Airflow est le standard industriel, limites pour les projets agiles, alternative Serverless avec **GitHub Actions** (CI/CD data, secrets, alertes). |
| **3.2 Pipeline CI/CD GitHub Actions** | 2h30 | Pratique | 🧪 [Lab GitHub Actions Orchestration (Notebook)](02_cours/day3_production/labs/01_lab_github_actions_orchestration.ipynb)<br>Mise en place d'un pipeline CI/CD automatisé et planifié (`workflow_dispatch`, `cron`) pour exécuter et valider des transformations SQL sur BigQuery sans serveur dédié. |
| **3.3 Visualisation Décisionnelle** | 0h30 | Pratique / Bonus | 📊 [Guide Looker Studio](02_cours/day3_production/bonus/04_looker_studio_guide.md)<br>Connexion directe à la table Gold BigQuery et création d'un tableau de bord décisionnel d'une page. |
| **3.4 Cas pratique évalué (Examen)** | 3h00 | Autonomie / Évaluation | 📝 [Sujet Examen](03_evaluation/SUJET_EXAMEN_BIG_DATA.md) & 📋 [QCM Théorique](03_evaluation/qcm_theorique.md)<br>**Mission globale sur dépôt Git :** Ingestion d'une API via `dlt`, structuration Medallion dans BigQuery, orchestration CI/CD, requêtes analytiques finales et QCM de synthèse. |

---

## 📁 Structure du Répertoire

```text
big_data/
├── .github/workflows/       # 🚀 Pipeline CI/CD GitHub Actions d'orchestration
├── 01_data/                 # Datasets bruts, schémas JSON, exemples de logs
├── 02_cours/                # Cours, TPs, exercices et scripts guidés
│   ├── day1_ingestion/      # GCP CLI, GCS Data Lake, Loading Data into BQ, dlt
│   │   ├── theorie/         # 📊 01_slides_paradigme_bigdata.md
│   │   ├── labs/            # 🧪 Labs guidés (OLAP, IAM/Budget, Data Lake, dlt)
│   │   └── bonus/           # 📚 Tutoriels approfondis (dlt avancé)
│   ├── day2_transformation/ # Medallion Architecture, Partitioning, SQL BigQuery
│   │   ├── theorie/         # 📊 02_slides_medallion_et_modelisation.md
│   │   ├── labs/            # 🧪 02_lab_sql_transformations_planifiees.ipynb
│   │   └── bonus/           # 📚 SQL JSON/UNNEST & Projet dbt complet
│   └── day3_production/     # Orchestration Serverless, CI/CD, Visualisation
│       ├── theorie/         # 📊 03_slides_orchestration_serverless.md
│       ├── labs/            # 🧪 01_lab_github_actions_orchestration.ipynb
│       └── bonus/           # 📚 Guide Looker Studio
├── 03_evaluation/           # Sujet et base du Cas Pratique Évalué (Examen final)
├── pyproject.toml           # Gestion des dépendances Python (uv)
└── README.md                # Ce document
```

---

## 🛠️ Préréquis & Configuration de l'Environnement

### 1. Outils requis
- **Python 3.11+** (géré via `uv`)
- **Google Cloud SDK (`gcloud` CLI)**
- Un compte **Google Cloud Platform** (Projet GCP configuré avec facturation activée ou crédits étudiants).

### 2. Installation de l'environnement Python
```bash
cd big_data
uv sync
```


### 3. Procédure d'accès à Google Cloud Platform pour le cours

Pour accéder à l'environnement du cours sur GCP, suivez ces 3 étapes :

#### 1. Activer votre adresse @campus.lasallebourges.com comme compte Google (si ce n'est pas déjà fait)
Si votre adresse n'est pas déjà un compte Google :
1. Rendez-vous sur : https://accounts.google.com/SignUpWithoutGmail
2. Renseignez votre nom, prénom et **l'adresse email exacte**  d'étudiant.
3. Choisissez un mot de passe.
4. Google vous envoie un code de vérification à 6 chiffres par email : saisissez-le pour valider.
*(Note : Cela ne change rien à votre boîte mail actuelle, cela permet juste à Google de vous authentifier).*

#### 2. Accéder à la console Google Cloud
1. Rendez-vous sur : https://console.cloud.google.com
2. Connectez-vous avec votre adresse email et le mot de passe défini à l'étape 1.
3. Acceptez les conditions d'utilisation lors de la première connexion.
4. **Sélectionnez le projet du cours** :
   - En haut à gauche, à côté du logo "Google Cloud", cliquez sur le menu déroulant des projets.
   - Sélectionnez le projet du cours : `lasalle-big-data`.
5. Vous avez maintenant accès aux services autorisés (BigQuery, Cloud Storage) !
