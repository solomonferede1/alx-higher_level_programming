-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- on your server (in localhost).
SELECT * 
FROM information_schema.user_privileges
WHERE (GRANTEE LIKE 'user_0d_1@localhost' OR  GRANTEE LIKE 'user_0d_2@localhost');