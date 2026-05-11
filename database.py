import sqlite3

# Veritabanı dosyasının yolu
DB_PATH = "job_posting.db"

class DatabaseManager:
    def __init__(self):
        """
        Sınıf başlatıldığında veritabanı bağlantısını kurar,
        tabloları oluşturur ve varsayılan admin kullanıcısını ekler.
        """
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
        self.seed_admin()

    def connect(self):
        """
        SQLite veritabanına bağlantı sağlar, yabancı anahtar (foreign key)
        desteğini açar ve sonuçların sözlük yapısında (Row) dönmesini ayarlar.
        """
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def create_tables(self):
        """
        Sistem için gerekli olan ana tabloları (Kullanıcılar, Kategoriler,
        İşler ve Başvurular) veritabanında oluşturur.
        """
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                role TEXT NOT NULL DEFAULT 'jobseeker',
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS job_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employer_id INTEGER NOT NULL,
                category_id INTEGER,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                salary TEXT,
                description TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (employer_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES job_categories(id)
            );

            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                applicant_id INTEGER NOT NULL,
                cover_letter TEXT,
                status TEXT DEFAULT 'pending',
                applied_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
                FOREIGN KEY (applicant_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)
        self.conn.commit()

        # Varsayılan iş kategorilerini ekler
        default_cats = ["Yazılım", "Pazarlama", "Tasarım", "Muhasebe", "İnsan Kaynakları", "Satış", "Diğer"]
        for cat in default_cats:
            self.cursor.execute("INSERT OR IGNORE INTO job_categories (name) VALUES (?)", (cat,))
        self.conn.commit()

    def seed_admin(self):
        """
        Sistemde herhangi bir admin bulunup bulunmadığını kontrol eder,
        eğer yoksa varsayılan bir yönetici hesabı oluşturur.
        """
        existing = self.cursor.execute(
            "SELECT id FROM users WHERE role='admin'"
        ).fetchone()
        if not existing:
            self.cursor.execute(
                "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
                ("admin", "admin123", "admin@admin.com", "admin")
            )
            self.conn.commit()

    def execute(self, query, params=()):
        """
        Verilen SQL sorgusunu parametrelerle birlikte çalıştırır
        ve değişiklikleri veritabanına kaydeder (commit).
        """
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def fetchone(self, query, params=()):
        """
        Verilen sorguyu çalıştırır ve sonuç kümesinden yalnızca ilk satırı döner.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        """
        Verilen sorguyu çalıştırır ve tüm sonuçları bir liste olarak döner.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """
        Açık olan veritabanı bağlantısını güvenli bir şekilde kapatır.
        """
        if self.conn:
             self.conn.close()

# Uygulama genelinde kullanılacak veritabanı yöneticisi nesnesi
db = DatabaseManager()