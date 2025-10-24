SELECT
  '{{ target.name }}' AS target_name,
  '{{ target.schema }}' AS target_schema,
  '{{ target.database }}' AS target_database,
  '{{ this }}' AS full_model_path