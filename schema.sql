
CREATE DATABASE IF NOT EXISTS whatsapp_leads;

USE whatsapp_leads;

CREATE TABLE leads(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(50),
    interest VARCHAR(255),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE conversations(
    id INT AUTO_INCREMENT PRIMARY KEY,
    lead_id INT,
    message TEXT,
    sender VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
