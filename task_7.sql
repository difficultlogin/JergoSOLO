DELETE FROM `something`
WHERE `id` IN (
    SELECT `id` FROM `something`
    ORDER BY `id` DESC
    LIMIT 5
)