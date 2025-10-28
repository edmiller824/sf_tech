select 
    id::INT as request_id 
    , to_timestamp(creation_date) as opened_date
    , lower(trim(request_name)) as request_title
    , lower(trim(request_desc)) as request_description
    , lower(trim(address)) as request_location
    , case  when closed_date is not null then DATEDIFF('day', creation_date, closed_date)
            else DATEDIFF('day', creation_date, current_timestamp())
        end AS duration_days_open
    , to_timestamp(closed_date) as closed_date
    , case  when to_timestamp(closed_date) is not null then TRUE else FALSE end as closed_flag
    , current_timestamp() as load_ts
from {{ source('raw', 'service_requests') }}
where id is not null