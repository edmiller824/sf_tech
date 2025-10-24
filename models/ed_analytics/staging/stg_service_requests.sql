select *
from {{ source('raw', 'service_requests') }}

-- models/staging/debug_target.sq
-- SELECT 
--   '{{ target.database }}' AS target_db,
--   '{{ target.schema }}' AS target_schema,
--   '{{ this }}' AS model_full_path