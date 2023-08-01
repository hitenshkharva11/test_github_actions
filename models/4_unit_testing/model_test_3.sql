SELECT
    id,
    name,
    description
FROM {{ ref('test_checkpoint1') }}

