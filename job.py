from database import db


class JobCategory:
    """İş ilanlarının sınıflandırıldığı kategorileri temsil eden sınıf."""

    def __init__(self, id, name):
        """Kategori nesnesini ID ve isim bilgileriyle başlatır."""
        self.id = id
        self.name = name

    @staticmethod
    def get_all():
        """Veritabanındaki tüm iş kategorilerini bir liste olarak döner."""
        rows = db.fetchall("SELECT * FROM job_categories")
        return [JobCategory(r["id"], r["name"]) for r in rows]

    @staticmethod
    def add(name):
        """Sisteme yeni bir iş kategorisi ekler (Eğer kategori zaten yoksa)."""
        db.execute("INSERT OR IGNORE INTO job_categories (name) VALUES (?)", (name,))


class Job:
    """İş ilanlarını temsil eden ve ilanlar üzerindeki veritabanı işlemlerini yürüten sınıf."""

    def __init__(self, id, employer_id, category_id, title, company, location, salary, description, is_active, created_at):
        """Bir iş ilanı nesnesini tüm detaylarıyla birlikte oluşturur."""
        self.id = id
        self.employer_id = employer_id
        self.category_id = category_id
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description
        self.is_active = is_active
        self.created_at = created_at

    @staticmethod
    def create(employer_id, category_id, title, company, location, salary, description):
        """Veritabanına yeni bir iş ilanı kaydı ekler."""
        db.execute(
            "INSERT INTO jobs (employer_id, category_id, title, company, location, salary, description) VALUES (?,?,?,?,?,?,?)",
            (employer_id, category_id, title, company, location, salary, description)
        )

    @staticmethod
    def get_all(active_only=True):
        """
        Sistemdeki tüm ilanları listeler.
        active_only parametresi True ise sadece yayında olan ilanları getirir.
        """
        if active_only:
            rows = db.fetchall("SELECT * FROM jobs WHERE is_active=1 ORDER BY created_at DESC")
        else:
            rows = db.fetchall("SELECT * FROM jobs ORDER BY created_at DESC")
        return [Job(*[r[k] for k in ["id","employer_id","category_id","title","company","location","salary","description","is_active","created_at"]]) for r in rows]

    @staticmethod
    def get_by_id(job_id):
        """ID bilgisi verilen tek bir iş ilanının detaylarını Job nesnesi olarak getirir."""
        r = db.fetchone("SELECT * FROM jobs WHERE id=?", (job_id,))
        if r:
            return Job(r["id"], r["employer_id"], r["category_id"], r["title"], r["company"], r["location"], r["salary"], r["description"], r["is_active"], r["created_at"])
        return None

    @staticmethod
    def get_by_employer(employer_id):
        """Belirli bir işverene (employer) ait olan tüm ilanları listeler."""
        rows = db.fetchall("SELECT * FROM jobs WHERE employer_id=? ORDER BY created_at DESC", (employer_id,))
        return [Job(r["id"], r["employer_id"], r["category_id"], r["title"], r["company"], r["location"], r["salary"], r["description"], r["is_active"], r["created_at"]) for r in rows]

    @staticmethod
    def search(keyword="", category_id=None, location=""):
        """
        Anahtar kelime, kategori ID veya konuma göre aktif ilanlar arasında arama yapar.
        """
        query = "SELECT * FROM jobs WHERE is_active=1"
        params = []
        if keyword:
            query += " AND (title LIKE ? OR company LIKE ? OR description LIKE ?)"
            params += [f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"]
        if category_id:
            query += " AND category_id=?"
            params.append(category_id)
        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")
        query += " ORDER BY created_at DESC"
        rows = db.fetchall(query, params)
        return [Job(r["id"], r["employer_id"], r["category_id"], r["title"], r["company"], r["location"], r["salary"], r["description"], r["is_active"], r["created_at"]) for r in rows]

    def delete(self):
        """Mevcut iş ilanı kaydını veritabanından tamamen siler."""
        db.execute("DELETE FROM jobs WHERE id=?", (self.id,))

    def toggle_active(self):
        """İlanın aktiflik durumunu tersine çevirir (Aktif ise Pasif yapar, veya tersi)."""
        self.is_active = 0 if self.is_active else 1
        db.execute("UPDATE jobs SET is_active=? WHERE id=?", (self.is_active, self.id))

    def update(self, title, company, location, salary, description, category_id):
        """İlanın başlık, şirket, konum, maaş ve açıklama gibi bilgilerini günceller."""
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description
        self.category_id = category_id
        db.execute(
            "UPDATE jobs SET title=?, company=?, location=?, salary=?, description=?, category_id=? WHERE id=?",
            (title, company, location, salary, description, category_id, self.id)
        )