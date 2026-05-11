from database import db


class ReportGenerator:
    """Sistemdeki verileri analiz ederek yönetici paneli için istatistiksel raporlar hazırlayan sınıf."""

    @staticmethod
    def total_users():
        """Sistemde kayıtlı olan toplam kullanıcı sayısını veritabanından çeker."""
        row = db.fetchone("SELECT COUNT(*) as cnt FROM users")
        return row["cnt"] if row else 0

    @staticmethod
    def total_jobs():
        """Sistemde oluşturulmuş olan (aktif/pasif ayrımı yapmaksızın) toplam iş ilanı sayısını döndürür."""
        row = db.fetchone("SELECT COUNT(*) as cnt FROM jobs")
        return row["cnt"] if row else 0

    @staticmethod
    def active_jobs():
        """Şu anda yayında (is_active=1) olan toplam iş ilanı sayısını döndürür."""
        row = db.fetchone("SELECT COUNT(*) as cnt FROM jobs WHERE is_active=1")
        return row["cnt"] if row else 0

    @staticmethod
    def total_applications():
        """İlanlara yapılmış olan tüm başvuruların toplam sayısını verir."""
        row = db.fetchone("SELECT COUNT(*) as cnt FROM applications")
        return row["cnt"] if row else 0

    @staticmethod
    def applications_by_status():
        """Başvuruları durumlarına (beklemede, kabul, red) göre gruplandırarak her durumdan kaç adet olduğunu döner."""
        rows = db.fetchall(
            "SELECT status, COUNT(*) as cnt FROM applications GROUP BY status"
        )
        return {r["status"]: r["cnt"] for r in rows}

    @staticmethod
    def top_jobs():
        """En çok başvuru yapılan ilk 5 ilanı; başlık, şirket ve başvuru sayısıyla birlikte listeler."""
        rows = db.fetchall(
            """SELECT j.title, j.company, COUNT(a.id) as app_count
               FROM jobs j LEFT JOIN applications a ON j.id=a.job_id
               GROUP BY j.id ORDER BY app_count DESC LIMIT 5"""
        )
        return rows

    @staticmethod
    def jobs_by_category():
        """Kategorilere göre kaçar adet iş ilanı bulunduğunu gösteren listeyi hazırlar."""
        rows = db.fetchall(
            """SELECT c.name, COUNT(j.id) as cnt
               FROM job_categories c LEFT JOIN jobs j ON c.id=j.category_id
               GROUP BY c.id"""
        )
        return rows

    @staticmethod
    def get_summary():
        """Admin paneli ana sayfasında gösterilmek üzere temel istatistikleri bir sözlük yapısında toplar."""
        return {
            "Toplam Kullanıcı": ReportGenerator.total_users(),
            "Toplam İlan": ReportGenerator.total_jobs(),
            "Aktif İlan": ReportGenerator.active_jobs(),
            "Toplam Başvuru": ReportGenerator.total_applications(),
        }