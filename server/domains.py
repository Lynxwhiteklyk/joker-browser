import sqlite3

class DomainManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.conn = sqlite3.connect(self.data_file)
        self.create_table_if_not_exists()
        self.domains = self.load_domains()

    def create_table_if_not_exists(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS domains (
                id INTEGER PRIMARY KEY,
                name TEXT,
                ip_address TEXT
            )
        ''')
        self.conn.commit()

    def load_domains(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, ip_address FROM domains')
        rows = cursor.fetchall()
        domains = []
        for row in rows:
            domain = {
                'name': row[0],
                'ip_address': row[1]
            }
            domains.append(domain)
        return domains

    def get_domain_by_name(self, name):
        for domain in self.domains:
            if domain['name'] == name:
                return domain
        return None

    def add_domain(self, domain):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO domains (name, ip_address) VALUES (?, ?)', (domain['name'], domain['ip_address']))
        self.conn.commit()
        self.domains.append(domain)

    def delete_domain(self, name):
        domain = self.get_domain_by_name(name)
        if domain:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM domains WHERE name = ?', (name,))
            self.conn.commit()
            self.domains.remove(domain)

    def save_domains(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM domains')
        for domain in self.domains:
            cursor.execute('INSERT INTO domains (name, ip_address) VALUES (?, ?)', (domain['name'], domain['ip_address']))
        self.conn.commit()

