
import csv
import os
from io import StringIO

import dlt
from google.cloud import storage


# Configuration du projet
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "lasalle-big-data")
BUCKET_NAME = os.getenv("GCS_BUCKET", "exam_bucket_eu")
CSV_FILE = os.getenv("GCS_FILE", "products.csv")
DATASET_NAME = "examen_johane"
TABLE_NAME = "bronze_products"


def parse_float(value):
    """Convertit une valeur en nombre, ou retourne None si elle est vide."""
    if value is None or value.strip() == "":
        return None

    try:
        return float(value.strip())
    except ValueError:
        return None


def parse_bool(value):
    """Convertit les valeurs courantes du CSV en booléen."""
    if value is None or value.strip() == "":
        return None

    value = value.strip().lower()

    if value in ("true", "1", "yes", "oui"):
        return True
    if value in ("false", "0", "no", "non"):
        return False

    return None


def read_products_from_gcs():
    """Télécharge le CSV depuis GCS et prépare les lignes produits."""
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(CSV_FILE)

    if not blob.exists():
        raise FileNotFoundError(
            f"Fichier introuvable dans GCS : gs://{BUCKET_NAME}/{CSV_FILE}"
        )

    csv_content = blob.download_as_text(encoding="utf-8-sig")
    reader = csv.DictReader(StringIO(csv_content))

    if not reader.fieldnames:
        raise ValueError("Le fichier CSV est vide ou ne contient pas d'en-têtes.")

    expected_columns = {
        "product_id",
        "name",
        "category",
        "cost",
        "retail_price",
        "is_active",
        "added_date",
    }

    missing_columns = expected_columns - set(reader.fieldnames)
    if missing_columns:
        raise ValueError(
            f"Colonnes manquantes dans le CSV : {sorted(missing_columns)}"
        )

    products = []

    for row in reader:
        products.append(
            {
                "product_id": row["product_id"],
                "name": row["name"],
                "category": row["category"],
                # On conserve cost en texte pour le convertir dans Silver.
                "cost": row["cost"],
                "retail_price": parse_float(row["retail_price"]),
                "is_active": parse_bool(row["is_active"]),
                # On conserve la date en texte pour la convertir dans Silver.
                "added_date": row["added_date"],
            }
        )

    print(f"{len(products)} lignes lues depuis gs://{BUCKET_NAME}/{CSV_FILE}")
    return products


def main():
    products = read_products_from_gcs()

    pipeline = dlt.pipeline(
        pipeline_name="exam_johane_products",
        destination="bigquery",
        dataset_name=DATASET_NAME,
    )

    # Schéma explicite pour conserver les types attendus dans Bronze.
    products_resource = dlt.resource(
        products,
        name=TABLE_NAME,
        columns={
            "product_id": {"data_type": "text"},
            "name": {"data_type": "text"},
            "category": {"data_type": "text"},
            "cost": {"data_type": "text"},
            "retail_price": {"data_type": "double"},
            "is_active": {"data_type": "bool"},
            "added_date": {"data_type": "text"},
        },
    )

    load_info = pipeline.run(
        products_resource,
        write_disposition="replace",
    )

    print("Chargement Bronze terminé.")
    print(load_info)


if __name__ == "__main__":
    main()