-- Fails if any opened_date value is not a valid timestamp
SELECT *
FROM {{ ref('stg_service_requests') }}
WHERE TO_TIMESTAMP(opened_date) IS NULL
  AND opened_date IS NOT NULL