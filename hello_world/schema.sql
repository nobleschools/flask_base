DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS contacts;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEST NOT NULL
);

CREATE TABLE contacts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	owner_id INTEGER NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	uses_remaining INTEGER NOT NULL,
	FOREIGN KEY (owner_id) REFERENCES user (id)
);

