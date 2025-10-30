# 🧠 ed_analytics — Modern Data Stack Project

## 📌 Overview
This project is a hands-on implementation of a modern data pipeline using **dbt Cloud + Snowflake**, showcasing ELT design principles, data modeling, and testing best practices.

It transforms raw service request data into clean, validated, and analytics-ready models.

---

## 🔄 Data Flow Architecture

raw.service_requests
↓
stg_service_requests
↓
(future) marts.*

---

## 🧱 Model Layers

### 1. **Source Layer**
- Ingests raw CSV data into `ed_analytics.raw.service_requests`.

### 2. **Staging Layer**
- Located in: `models/ed_analytics/staging/`
- Transforms, cleans, and standardizes raw data.
- Adds calculated fields like `closed_flag`, `duration_days`, etc.

### 3. **(Planned) Mart Layer**
- Will aggregate and summarize key metrics for reporting.
- Located in: `models/ed_analytics/marts/`

---

## ✅ Testing & Quality

- Built-in dbt tests:
  - `unique`, `not_null`
- Custom tests:
  - Timestamp format validation using macros
- Test coverage increases with each model added

---

## 📚 Documentation

- Auto-generated with `dbt docs`
- View interactive lineage, column descriptions, and test status
- Model-specific documentation lives in `schema.yml` files alongside models

---

## 🛠 Tech Stack

- **Snowflake** (data warehouse)
- **dbt Cloud** (orchestration & transformation)
- **dbt-utils**, **dbt-expectations** (testing packages)
- GitHub (version control)

---

## 🚀 TODOs / Next Steps

- [ ] Add mart model: `fct_service_metrics`
- [ ] Create CI/CD deployment job in dbt Cloud
- [ ] Connect BI tool (Tableau or Looker Studio)
- [ ] Add exposures and dashboard metadata
- [ ] Publish project documentation

---

## 🧩 Project Structure
ed_analytics/
├── models/
│   ├── ed_analytics/
│   │   ├── staging/
│   │   └── marts/         ← future models
├── macros/
├── tests/
├── dbt_project.yml
├── packages.yml
└── README.md              ← you’re here