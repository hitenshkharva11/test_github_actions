-- This model contains a semicolon at the end
SELECT
    id,
    name,
    description
FROM {{ ref('test_checkpoint1') }}
