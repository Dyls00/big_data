# 📦 Données de la Formation — TheLook eCommerce

Ce dossier contient les datasets utilisés tout au long de la formation
**Manipulation de Données avec Python (NumPy & Pandas)**.

## 📁 Structure

```
01_data/
├── raw/                          # Exports bruts — NE PAS MODIFIER
│   ├── thelook_users.csv         # 5 000 utilisateurs
│   ├── thelook_products.csv      # 2 000 produits (mode)
│   ├── thelook_orders.csv        # 20 000 commandes
│   └── thelook_order_items.csv   # 50 000 articles commandés
├── exercises/                    # Datasets préparés pour les exercices
│   ├── temperatures_365.csv      # 365 températures (exercice NumPy E1.1)
│   ├── thelook_sales.csv         # Jointure dénormalisée (clean)
│   └── thelook_sales_dirty.csv   # Idem avec problèmes de qualité injectés
├── capstone/
│   └── thelook_capstone.csv      # Dataset enrichi + dégradé pour le projet final
```

## 📊 Schéma des données

### `thelook_users.csv`
| Colonne | Type | Description |
|---------|------|-------------|
| id | int | Identifiant unique |
| first_name | str | Prénom |
| last_name | str | Nom |
| email | str | Adresse email |
| age | int | Âge (18-80) |
| gender | str | M ou F |
| country | str | Pays (15 pays) |
| city | str | Ville |
| traffic_source | str | Canal d'acquisition (Search, Organic, Facebook, Email, Display) |
| created_at | datetime | Date de création du compte |

### `thelook_products.csv`
| Colonne | Type | Description |
|---------|------|-------------|
| id | int | Identifiant produit |
| name | str | Nom complet (Marque + Descripteur + Catégorie) |
| category | str | Catégorie (19 catégories mode) |
| brand | str | Marque (20 marques) |
| department | str | Département (Men / Women) |
| cost | float | Coût d'achat |
| retail_price | float | Prix de vente conseillé |
| sku | str | Référence produit |
| distribution_center_id | int | Centre de distribution (1-10) |

### `thelook_orders.csv`
| Colonne | Type | Description |
|---------|------|-------------|
| order_id | int | Identifiant commande |
| user_id | int | → users.id |
| status | str | Complete (65%), Shipped, Processing, Cancelled, Returned |
| created_at | datetime | Date de commande |
| num_of_item | int | Nombre d'articles (1-5) |
| shipped_at | datetime | Date d'expédition (NaT si non expédié) |
| delivered_at | datetime | Date de livraison (NaT si non livré) |
| returned_at | datetime | Date de retour (NaT si non retourné) |

### `thelook_sales.csv` (dénormalisé)
Jointure de `order_items × products × users`. Contient toutes les colonnes
des items + product_name, category, brand, department, cost, gender, age,
country, city, traffic_source.

### `thelook_sales_dirty.csv` ⚠️
Même structure que `thelook_sales.csv` avec des **problèmes injectés** :
- ~8% de NaN dans `sale_price`
- ~5% de NaN dans `age`
- ~2% de lignes dupliquées
- Pays avec variantes d'écriture (US, USA, United States, united states…)
- `cost` au format texte avec `$` (ex: `"$12.50"`)
- Outliers dans `sale_price` (valeurs négatives, prix > 5000$)
- Casse mélangée dans `category`

### `thelook_capstone.csv` ⚠️
Dataset enrichi (+ first_name, last_name, email, notes) avec des dégradations
différentes du dirty. Colonne `notes` 95% vide (piège).

## 🌉 Pont vers BigQuery

Ces données sont calquées sur le dataset public Google
[`bigquery-public-data.thelook_ecommerce`](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=thelook_ecommerce).

Dans le prochain cours (Big Data / BigQuery), les étudiants retrouveront
les **mêmes tables** directement dans BigQuery, avec des millions de lignes.
