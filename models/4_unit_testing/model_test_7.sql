-- This model contains an invalid date column with a name that does not end with '_date'
SELECT
    id,
    name,
    description,
    issue_test,
    issue_t
FROM {{ ref('test_checkpoint1') }};
