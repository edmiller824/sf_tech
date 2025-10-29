# ed_analytics – Modern Data Stack Project

### Overview
A 6-week project using Snowflake + dbt + BI tools to simulate a real-world analytics workflow and showcase a modern data engineering stack.

---

## ✅ Week 1 – Environment Setup & First Model

### 🧠 What I Set Up
- Created Snowflake warehouse, database (`analytics_db`), and personal schema (`ed_analytics.raw`)
- Loaded first raw dataset (`service_requests`)
- Connected dbt Cloud to Snowflake using `ACCOUNTADMIN` role
- Initialized dbt project and ran test models
- Defined first `source` in `sources.yml`
- Created and materialized a staging model (`stg_service_requests`)
- Validated model output in Snowflake

### 🧩 What I Learned
- dbt Cloud dev environments auto-generate schema names (`dbt_<username>[_branch]`)
- `{{ this }}` macro is the most reliable way to confirm where models are materialized
- `{{ source(...) }}` references raw sources cleanly and supports tests
- Schema and model folder structure must match `dbt_project.yml` to apply overrides

### 🚧 Challenges & Fixes
- Schema overrides via `dbt_project.yml` were ignored in dev due to dbt Cloud logic
- Used `debug_target.sql` to validate runtime values for `target.schema` and model paths
- Accepted building to `dbt_emiller_dev` in dev, with plans to deploy to `analytics_db.dev` in prod

### 🔭 Next Steps (Week 2)
- Clean and cast fields in `stg_service_requests`
- Add `schema.yml` tests (e.g., `not_null`, `unique`)
- Create `mart_open_requests` model for simple reporting
- Generate and explore dbt documentation and lineage graph


### ✅ Custom Timestamp Validation Tests

To ensure that `opened_date` and `closed_date` are valid timestamps:

**Test SQL structure:**
```sql
SELECT *
FROM {{ ref('stg_service_requests') }}
WHERE TRY_TO_TIMESTAMP(field::STRING) IS NULL
  AND field IS NOT NULL