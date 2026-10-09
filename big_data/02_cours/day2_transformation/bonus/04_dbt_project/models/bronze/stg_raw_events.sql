-- Modèle Bronze : Normalisation minimale des événements bruts
WITH source AS (
    SELECT * FROM {{ target.project }}.bronze_landing.native_raw_events
)
SELECT
    event_id,
    CAST(timestamp AS TIMESTAMP) AS event_timestamp,
    user_id,
    event_type,
    device.os AS device_os,
    device.browser AS device_browser,
    payload
FROM source
