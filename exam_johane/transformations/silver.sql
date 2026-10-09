
CREATE OR REPLACE TABLE
  `lasalle-big-data.examen_johane.silver_products` AS

SELECT
    NULLIF(TRIM(product_id), '') AS product_id,

    NULLIF(TRIM(name), '') AS name,

    NULLIF(TRIM(category), '') AS category,

    SAFE_CAST(
        NULLIF(TRIM(cost), '')
        AS FLOAT64
    ) AS cost,

    retail_price,

    is_active,

    SAFE_CAST(
        NULLIF(TRIM(added_date), '')
        AS DATE
    ) AS added_date

FROM `lasalle-big-data.examen_johane.bronze_products`

WHERE product_id IS NOT NULL
  AND TRIM(product_id) != '';