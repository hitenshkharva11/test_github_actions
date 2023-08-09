-- This model contains an invalid boolean column with a name that does not start with 'is_', 'has_', or 'do_'
SELECT
    id,
    name,
    description,
    active_status,
    issue_test
FROM {{ ref('test_checkpoint1') }};
