-- Fails if any closed_date value is not a valid timestamp
SELECT *
FROM {{ ref('stg_service_requests') }}
WHERE TRY_TO_TIMESTAMP(closed_date::STRING) IS NULL
  AND closed_date IS NOT NULL