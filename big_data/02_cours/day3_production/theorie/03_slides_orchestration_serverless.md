---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #0f0f1a
color: #e0e0ff
header: "Formation Big Data — Module 3.3 : Orchestration & Serverless"
footer: "La Salle — Data Engineering sur GCP"
style: |
  section {
    font-size: 22px;
    font-family: 'Segoe UI', sans-serif;
  }
  h1 { color: #00d4ff; }
  h2 { color: #00b4d8; border-bottom: 2px solid #0077b6; padding-bottom: 8px; }
  h3 { color: #48cae4; }
  code { background: #1a1a2e; color: #90e0ef; border-radius: 4px; padding: 2px 6px; }
  pre { background: #1a1a2e; border-radius: 8px; }
  strong { color: #00d4ff; }
  em { color: #48cae4; }
  table { font-size: 20px; }
  blockquote { border-left: 4px solid #0077b6; color: #90e0ef; }
---

# 🚀 Module 3.3 : Orchestration, CI/CD & Abstraction Serverless

### Du pipeline manuel à l'automatisation en production

> *"Un pipeline de données qui ne tourne pas automatiquement n'existe pas vraiment en production."*

---

## 📌 Ordre du Jour

| # | Thème | Durée |
|---|-------|-------|
| 1 | L'évolution du Cloud : IaaS → PaaS → FaaS 
| 2 | L'Abstraction Serverless (Function as a Service)
| 3 | Rappel J2 : Scheduled Queries & Materialized Views 
| 4 | Pourquoi l'Orchestration est vitale en Data Engineering 
| 5 | Apache Airflow : Le standard de l'industrie 
| 6 | GitHub Actions : L'approche CI/CD agile 
| 7 | Synthèse : Choisir le bon outil 

---

<!-- _class: lead -->

# Partie 1
## L'évolution de l'hébergement Cloud

---

## 🏗️ De la cave au Cloud

```
On-Premise  →  IaaS  →  PaaS  →  SaaS/FaaS
─────────────────────────────────────────────────
Vous gérez  →  Vous gérez  →  Vous configurez  →  Vous écrivez
    TOUT        l'OS+Code      seulement le code    la fonction
```

- **On-Premise** : Vous gérez TOUT (Réseau, Électricité, Serveurs, OS, Code).
- **IaaS** *(Infrastructure as a Service)* : GCP vous loue une VM (Compute Engine). Vous gérez l'OS et le code.
- **PaaS** *(Platform as a Service)* : Vous utilisez un outil existant mais configurez son architecture (ex : BigQuery, Cloud SQL...).
- **SaaS** *(Software as a Service)* : Vous utilisez un outil clé en main, sans aucune gestion d'infrastructure (ex : Gmail, Google sheets...).
- **FaaS** *(Function as a Service)* : L'abstraction ultime — vous ne gérez que la logique.

---

## 📊 Comparatif de responsabilités

| Couche | On-Premise | IaaS | PaaS | FaaS |
|--------|-----------|------|------|------|
| Réseau & Datacenter | ✅ Vous | ☁️ Cloud | ☁️ Cloud | ☁️ Cloud |
| Serveurs physiques | ✅ Vous | ☁️ Cloud | ☁️ Cloud | ☁️ Cloud |
| Système d'exploitation | ✅ Vous | ✅ Vous | ☁️ Cloud | ☁️ Cloud |
| Runtime / Framework | ✅ Vous | ✅ Vous | ✅ Vous | ☁️ Cloud |
| **Votre code / logique** | ✅ Vous | ✅ Vous | ✅ Vous | ✅ **Vous** |
| Facturation | Fixe | À l'heure | À l'usage | **À la seconde** |

> 💡 En Data Engineering, on utilise souvent **PaaS + FaaS** selon la complexité du pipeline.

---

<!-- _class: lead -->

# Partie 2
## L'Abstraction Serverless (FaaS)

---

## ⚡ Le concept Serverless

**Le serveur existe, mais ce n'est plus votre problème.**

- Vous écrivez uniquement la **fonction** (le code métier).
- Le cloud (ex: Cloud Functions / AWS Lambda / GitHub Actions) s'occupe de :
  - Provisionner le CPU et la RAM
  - Lancer l'OS **uniquement quand la fonction est appelée**
  - Redimensionner automatiquement selon la charge
  - Arrêter et ne plus facturer quand la fonction est terminée

### 🎯 Avantage Data Engineering

> On ne paie qu'à la **seconde d'exécution**.
> Parfait pour un pipeline qui tourne **une fois par jour à 4h du matin** !

---

## 🔄 Serverless sur GCP — L'écosystème

```
Traitement de données
┌─────────────────────────────────────────────────────────────┐
│  BigQuery Scheduled Queries  ←── SQL planifié (sans serveur) │
│  BigQuery Materialized Views ←── Refresh automatique         │
│  Cloud Functions             ←── Code Python/Node (triggers) │
│  Cloud Run Jobs              ←── Conteneur éphémère          │
└─────────────────────────────────────────────────────────────┘


Orchestration
┌─────────────────────────────────────────────────────────────┐
│  GitHub Actions              ←── CI/CD (gratuit, simple)     │
│  Cloud Scheduler + Pub/Sub   ←── Cron serverless GCP         │
│  Cloud Composer              ←── Airflow managé (avancé)     │
└─────────────────────────────────────────────────────────────┘
```

---

<!-- _class: lead -->

# Partie 3
## Rappel Jour 2 : Automatisation Native BigQuery

### Scheduled Queries & Materialized Views

---

## 🔄 Rappel : Architecture Medallion

Pendant le **Jour 2**, vous avez construit un pipeline complet en SQL natif :

```
bronze.raw_events          ← données brutes, jamais modifiées
         │
         │  Transformation SQL  (typage, déduplication, filtrage)
         ▼
silver.events              ← données propres, partitionnées + clustered
         │
         │  Agrégation SQL      (KPIs quotidiens par pays / OS)
         ▼
gold.daily_kpis            ← métriques prêtes pour Looker Studio
```

> 💡 Chaque flèche = une **requête SQL** qui peut être **planifiée automatiquement**.

---

## ⏰ Scheduled Queries — Rappel & Approfondissement

Les **Scheduled Queries** de BigQuery permettent d'exécuter une requête SQL sur un calendrier défini — **sans serveur, sans orchestrateur externe**.


---

## ⏰ Configurer une Scheduled Query — Étapes

### Via la Console BigQuery

1. Ouvrir **Console BigQuery** → coller la requête SQL
2. Cliquer sur **"Planifier"** → **"Créer une requête planifiée"**
3. Configurer :
   - **Nom** : `refresh_silver_events`
   - **Récurrence** : `Toutes les heures` ou `Chaque jour à 02:00`
   - **Mode d'écriture** : `Overwrite table` (reconstruction complète)

### Via le CLI `bq`

```bash
bq mk \
  --transfer_config \
  --data_source=scheduled_query \
  --target_dataset=silver \
  --display_name="Refresh Silver Events (hourly)" \
  --schedule="every 60 minutes" \
  --params='{"query": "..."}'
```

---

## 🔄 Materialized Views — Rappel & Limites

Une **Materialized View** se rafraîchit **automatiquement** dès que la table source change.

```sql
CREATE MATERIALIZED VIEW `silver.mv_events`
PARTITION BY event_date
CLUSTER BY user_id
OPTIONS (
  enable_refresh = true,
  refresh_interval_minutes = 30,
  description = 'Vue matérialisée — auto-refresh 30 min'
)
AS
SELECT
  event_id,
  PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%SZ', event_ts)      AS event_ts,
  DATE(PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%SZ', event_ts)) AS event_date,
  user_id,
  LOWER(TRIM(event_type)) AS event_type,
  SAFE_CAST(amount_str AS FLOAT64) AS amount,
  country
FROM `bronze.raw_events`
WHERE device_os != 'UnknownOS' AND country != 'XX';
-- ⚠️ ROW_NUMBER() non supporté → pas de déduplication complexe
```

---

## 🆚 Scheduled Query vs Materialized View

| Critère | Scheduled Query | Materialized View |
|---------|----------------|-------------------|
| Rafraîchissement | Planifié (cron) | Automatique (~30 min) |
| Déduplication (`ROW_NUMBER`) | ✅ Supportée | ❌ Non supportée |
| Logique complexe (`CTE`, `CASE`) | ✅ Oui | ⚠️ Limitée |
| Contrôle du timing | ✅ Précis | ❌ Géré par BigQuery |
| Coût stockage | Table complète | Partiel (incrémental) |
| Idéal pour | Silver complexe, Gold | Agrégations Gold simples |

> ✅ **Règle** : Materialized View pour les agrégations simples, Scheduled Query pour toute logique métier avancée (déduplication, typage, filtrage).

---

## 📊 Rappel : Impact du Partitionnement 

Rappel du **Benchmark**

| Requête | Filtre | Bytes scannés | Réduction coût |
|---------|--------|--------------|----------------|
| Full scan | Aucun | ~100% | Référence |
| Filtre partition | `event_date BETWEEN ...` | **~10-20%** | ↓ 80-90% |

```sql
-- ✅ Requête optimisée : partition
SELECT event_date, event_type, amount
FROM `silver.events`
WHERE event_date = '2024-01-15'   -- partition pruning
ORDER BY event_ts;
```

> 💡 **1 TB scanné = ~5$ sur BigQuery on-demand.** Le partitionnement peut réduire les coûts de **90%+**.

---

<!-- _class: lead -->

# Partie 4
## Pourquoi orchestrer ses données ?

---

## 🕸️ Un pipeline = un graphe de dépendances

Un pipeline de données n'est jamais un script unique. C'est un **DAG** (Directed Acyclic Graph — Graphe Orienté Acyclique).

```
📥 Ingestion (dlt / API)
        │
        ▼
🥉 Bronze (raw_events)
        │
        ├──► ⏳ Attendre fin ingestion
        │
        ▼
🥈 Silver (Scheduled Query — toutes les heures)
        │
        ├──► ⏳ Attendre fin transformation
        │
        ▼
🥇 Gold (Scheduled Query — chaque nuit)
        │
        ▼
✅ Tests qualité → Alertes → Looker Studio
```

> ⚠️ Si l'ingestion échoue, il ne faut **surtout pas** lancer la transformation Silver !

---

## 🚨 Les problèmes sans orchestrateur

Sans orchestration, les pipelines manuels posent de graves problèmes :

| Problème | Impact |
|----------|--------|
| **Pas de gestion des dépendances** | Silver se lance même si Bronze est vide |
| **Pas de gestion des erreurs** | Un échec passe inaperçu jusqu'au lendemain matin |
| **Pas de rejeu automatique** | Intervention manuelle à chaque panne |
| **Pas de monitoring** | "Est-ce que le pipeline a tourné ?" |
| **Pas de lineage** | Impossible de tracer l'origine d'une anomalie |
| **Scripts dispersés** | `cron1.sh`, `script_final_v3.py`... |

> 🎯 **L'orchestrateur est le chef d'orchestre** : il sait quoi lancer, quand, dans quel ordre, et quoi faire en cas de problème.

---

## 📐 Anatomie d'un DAG

Un **DAG** (Directed Acyclic Graph) modélise les tâches et leurs dépendances :

```
    [Ingestion API]
          │
    ┌─────┴─────┐
    ▼           ▼
[Bronze FR] [Bronze BE]      ← tâches parallèles
    │           │
    └─────┬─────┘
          ▼
   [Silver Merge]            ← attend les 2 branches
          │
    ┌─────┴─────┐
    ▼           ▼
[Gold KPIs] [Gold Funnel]   ← tâches parallèles
    │           │
    └─────┬─────┘
          ▼
   [Tests qualité]
          │
          ▼
   [Alerte Slack / Email]
```

**Acyclique** = pas de boucle. Chaque tâche ne peut pas dépendre d'elle-même (indirectement).


---

<!-- _class: lead -->

# Partie 6
## GitHub Actions : L'Orchestration CI/CD Agile

---

## 🔧 CI/CD — Rappel du concept

**CI/CD** : Continuous Integration / Continuous Deployment.

- Initialement conçu pour **automatiser les tests et déploiements logiciels**.
- **En Data Engineering** : on l'utilise comme un **orchestrateur serverless léger** !

```
Push Git  ──► GitHub Actions ──► Tests ──► Deploy
    │                │
    │                └──► [Cron] Toutes les nuits à minuit :
    │                          - Allumer une VM virtuelle
    │                          - Installer Python + dépendances
    │                          - Lancer dlt (ingestion)
    │                          - Lancer dbt run (transformation)
    │                          - Lancer dbt test (validation)
    │                          - Éteindre la VM (facturation arrêtée)
    └──────────────────────────────────────────────────────────►
```

---

## 📄 Un workflow GitHub Actions — Exemple Data

```yaml
# .github/workflows/daily_pipeline.yml
name: "Daily Data Pipeline"

on:
  schedule:
    - cron: '0 2 * * *'      # chaque nuit à 02:00 UTC
  workflow_dispatch:          # ou déclencher manuellement

jobs:
  run_pipeline:
    runs-on: ubuntu-latest    # VM éphémère — gratuit jusqu'à 2000 min/mois

    steps:
      - name: "Checkout code"
        uses: actions/checkout@v4

      - name: "Authenticate to GCP"
        uses: google-github-actions/auth@v2
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: "Setup Python"
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: "Install dependencies"
        run: pip install dlt[bigquery] dbt-bigquery

      - name: "Step 1 - Ingestion (dlt)"
        run: python ingestion/run_pipeline.py

      - name: "Step 2 - Transformation (dbt)"
        run: |
          dbt run --profiles-dir .
          dbt test --profiles-dir .

      - name: "Step 3 - Notification Slack"
        if: success()
        run: echo "Pipeline termine avec succes"
```

---

## ✅❌ GitHub Actions — Avantages & Limites

### ✅ Avantages
- **Gratuit** : 2 000 minutes/mois pour les repos publics, 500 pour les privés
- **Aucune infrastructure à gérer** : GitHub s'occupe de tout
- **Visuel** : historique des runs dans l'onglet "Actions"
- **Intégré à Git** : le pipeline **est** dans le même repo que le code
- **Simple à déboguer** : les logs sont directement accessibles

### ❌ Limites

| Limite | Détail |
|--------|--------|
| **Pas de dépendances complexes** | Difficile de gérer des branches conditionnelles |
| **Pas de backfill natif** | Pas de gestion native des données historiques |
| **Durée max** | 6h par job (suffisant pour la plupart des ETL) |
| **Pas adapté au streaming** | Déclenché par événement, pas par flux continu |

---

## 🔐 Sécurité — Gestion des secrets

Les **secrets** (clés API, credentials GCP) ne doivent **JAMAIS** être dans le code !

```
GitHub Repository
├── Settings → Secrets and variables → Actions
│   ├── GCP_SA_KEY          ← Clé de compte de service GCP (JSON)
│   ├── SLACK_WEBHOOK       ← URL webhook Slack
│   └── BQ_PROJECT_ID       ← ID du projet BigQuery
│
└── .github/workflows/daily_pipeline.yml
    └── ${{ secrets.GCP_SA_KEY }}   ← Référence sécurisée
```

```yaml
# Utilisation dans un workflow
- name: Authenticate to GCP
  uses: google-github-actions/auth@v2
  with:
    credentials_json: ${{ secrets.GCP_SA_KEY }}
    # ↑ Jamais en clair ! Toujours via secrets.NOM_SECRET
```

---

<!-- _class: lead -->

# Partie 7
## Synthèse : Quel outil pour quel pipeline ?

---

## 🗺️ Carte de décision — Orchestration

```
Besoin d'orchestration
         │
         ▼
Est-ce que le pipeline est purement SQL sur BigQuery ?
    │                            │
   OUI                          NON
    │                            │
    ▼                            ▼
Logique complexe ?         Python / multi-outils ?
  (déduplication, CTE)          │
    │         │                 ▼
   NON       OUI        Budget important ?
    │         │             │         │
    ▼         ▼            NON       OUI
Materialized  Scheduled     │         │
   View       Query         ▼         ▼
                        GitHub    Apache Airflow
                        Actions   (Cloud Composer)
```

---

## 🆚 Comparatif global des solutions

| Critère | Scheduled Query | Materialized View | GitHub Actions | Airflow |
|---------|----------------|-------------------|----------------|---------|
| Coût | Requête seule | Requête seule | Gratuit | ~400€/mois |
| Complexité setup | Très simple | Très simple | Simple | Complexe |
| Gestion dépendances | Non | Non | Basique | Avancée |
| Multi-outils (Python+SQL+dbt) | SQL only | SQL only | Oui | Oui |
| Monitoring & Alertes | Basique | Basique | GitHub UI | Interface riche |

---

## 🏁 Synthèse du Module 3.3

### Les grandes leçons

| Concept | À retenir |
|---------|-----------|
| **Serverless** | Payer à la seconde, pas à l'heure de VM allumée |
| **DAG** | Modéliser les dépendances entre tâches — jamais de scripts dispersés |
| **Scheduled Queries** | SQL planifié pour les transformations Medallion simples |
| **Materialized Views** | Auto-refresh pour les agrégations Gold sans logique complexe |
| **GitHub Actions** | Orchestrateur agile pour les pipelines multi-outils légers |
| **Apache Airflow** | Standard pro — pour les pipelines complexes avec équipes |

---

## 🔗 Le pipeline de production complet

```
[GitHub Actions — cron 02:00]
         │
         ▼
dlt — Ingestion API → bronze.raw_events  (BigQuery)
         │
         ▼
Scheduled Query — bronze → silver.events (toutes les heures)
         │
         ▼
Scheduled Query — silver → gold.daily_kpis (chaque nuit)
         │
         ▼
test — Vérification qualité des données
         │
         ▼
Looker Studio — Dashboard en temps réel
         │
         ▼
Alerte Slack/Email si echec a n'importe quelle etape
```

---

## 🧠 Questions de Réflexion

1. Pourquoi ne peut-on pas utiliser une **Materialized View** pour la déduplication `ROW_NUMBER()` ?
2. Quelle est la différence entre un **cron** classique et un **DAG** Airflow ?
3. Dans quel cas GitHub Actions devient-il **insuffisant** comme orchestrateur ?

---

## 💻 Lab — Ce que vous allez faire

### Lab 03 — Pipeline en production avec GitHub Actions

**Créer un workflow GitHub Actions** qui déclenche le pipeline Medallion


### Architecture cible

```
GitHub Actions (cron) → dlt (Bronze) → Scheduled Query (Silver) → Gold
```
