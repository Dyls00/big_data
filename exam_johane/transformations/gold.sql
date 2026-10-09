CREATE OR REPLACE TABLE
  `lasalle-big-data.examen_johane.gold_category_metrics` AS

SELECT
    category,
    COUNT(*) AS nombre_produits,
    ROUND(AVG(retail_price), 2) AS prix_vente_moyen,
    ROUND(AVG(retail_price - cost), 2) AS marge_unitaire_moyenne

FROM `lasalle-big-data.examen_johane.silver_products`

WHERE category IS NOT NULL

GROUP BY category;