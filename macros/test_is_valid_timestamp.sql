{% test is_valid_timestamp(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE TRY_TO_TIMESTAMP({{ column_name }}::STRING) IS NULL
  AND {{ column_name }} IS NOT NULL
{% endtest %}