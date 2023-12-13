-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 DEFAULT COLLATE utf8mb4_unicode_ci CHARACTER SET utf8mb4;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;