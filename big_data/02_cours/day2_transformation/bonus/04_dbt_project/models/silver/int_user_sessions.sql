-- Modèle Silver : Nettoyage, déduplication et enrichissement
WITH stg AS (
    SELECT * FROM {{ ref('stg_raw_events') }}
),
dedup AS (
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY event_id ORDER BY event_timestamp DESC) AS rn
    FROM stg
)
SELECT
    event_id,
    event_timestamp,
    DATE(event_timestamp) AS event_date,
    user_id,
    event_type,
    device_os,
    device_browser
FROM dedup
WHERE rn = 1
