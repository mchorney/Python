USE Friendships;
SELECT * FROM Friendships;
SELECT * FROM users;
INSERT INTO users (first_name, last_name)
VALUES ('Chris', 'Baker');
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Diana', 'Smith', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('James', 'Johnson', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Jessica', 'Davidson', NOW(), NOW());
SELECT * FROM users;
SELECT * FROM Friendships;
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 4, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 3, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 2, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (2, 1, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (3, 1, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4, 1, NOW(), NOW());
SELECT * FROM friendships;
SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
LEFT JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users as users2 
ON friendships.friend_id = users2.id
ORDER BY users2.last_name DESC;