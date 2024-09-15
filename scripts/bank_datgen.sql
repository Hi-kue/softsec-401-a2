CREATE TABLE IF NOT EXISTS `user` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_active INTEGER NOT NULL CHECK (is_active IN (0, 1)),
    is_superuser INTEGER NOT NULL CHECK (is_superuser IN (0, 1))
);


CREATE TABLE IF NOT EXISTS `transactions` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    bank_account_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    transaction_type TEXT NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal')),
    description TEXT NOT NULL DEFAULT '',
    is_approved INTEGER NOT NULL CHECK(is_approved IN (0, 1)),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS `bank_account` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    balance REAL NOT NULL DEFAULT 0,
    currency_type TEXT NOT NULL CHECK (currency_type IN ('USD', 'CAD')),
    withdraw_limit REAL NOT NULL,
    is_active INTEGER NOT NULL CHECK (is_active IN (0, 1))
);