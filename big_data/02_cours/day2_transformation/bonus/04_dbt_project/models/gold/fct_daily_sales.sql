-- Modèle Gold : Mart d'agrégation d'activité quotidienne pour le suivi BI
WITH silver_events AS (
    SELECT * FROM {{ ref('int_user_sessions') }}
)
SELECT
    event_date,
    device_os,
    COUNT(DISTINCT user_id) AS active_users,
    COUNT(CASE WHEN event_type = 'page_view' THEN 1 END) AS total_page_views,
    COUNT(CASE WHEN event_type = 'purchase_success' THEN 1 END) AS total_purchases
FROM silver_events
GROUP BY 1, 2
