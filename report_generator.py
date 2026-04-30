from database import db


class ReportGenerator:
    @staticmethod
    def total_users():
        row = db.fetchone("SELECT COUNT(*) as cnt FROM users")
        return row["cnt"] if row else 0

    @staticmethod
    def total_jobs():
        row = db.fetchone("SELECT COUNT(*) as cnt FROM jobs")
        return row["cnt"] if row else 0

    @staticmethod
    def active_jobs():
        row = db.fetchone("SELECT COUNT(*) as cnt FROM jobs WHERE is_active=1")
        return row["cnt"] if row else 0

    @staticmethod
    def total_applications():
        row = db.fetchone("SELECT COUNT(*) as cnt FROM applications")
        return row["cnt"] if row else 0

    @staticmethod
    def applications_by_status():
        rows = db.fetchall(
            "SELECT status, COUNT(*) as cnt FROM applications GROUP BY status"
        )
        return {r["status"]: r["cnt"] for r in rows}

    @staticmethod
    def top_jobs():
        rows = db.fetchall(
            """SELECT j.title, j.company, COUNT(a.id) as app_count
               FROM jobs j LEFT JOIN applications a ON j.id=a.job_id
               GROUP BY j.id ORDER BY app_count DESC LIMIT 5"""
        )
        return rows

    @staticmethod
    def jobs_by_category():
        rows = db.fetchall(
            """SELECT c.name, COUNT(j.id) as cnt
               FROM job_categories c LEFT JOIN jobs j ON c.id=j.category_id
               GROUP BY c.id"""
        )
        return rows

    @staticmethod
    def get_summary():
        return {
            "Toplam Kullanıcı": ReportGenerator.total_users(),
            "Toplam İlan": ReportGenerator.total_jobs(),
            "Aktif İlan": ReportGenerator.active_jobs(),
            "Toplam Başvuru": ReportGenerator.total_applications(),
        }
