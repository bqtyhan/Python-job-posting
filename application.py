from database import db


class ApplicationStatus:
    """Sistemdeki iş başvurularının sahip olabileceği durum kodlarını ve etiketlerini tanımlar."""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    # Tüm durum kodlarının listesi
    ALL = [PENDING, ACCEPTED, REJECTED]

    # Durum kodlarının kullanıcı arayüzünde görünecek Türkçe karşılıkları
    LABELS = {
        PENDING: "Beklemede",
        ACCEPTED: "Kabul Edildi",
        REJECTED: "Reddedildi"
    }


class Application:
    """İş başvurusu verilerini temsil eden ve veritabanı işlemlerini yürüten temel sınıftır."""

    def __init__(self, id, job_id, applicant_id, cover_letter, status, applied_at):
        """
        Bir başvuru nesnesini veritabanından alınan bilgilerle başlatır.

        Args:
            id (int): Başvurunun benzersiz kimliği.
            job_id (int): Başvurulan iş ilanının kimliği.
            applicant_id (int): Başvuran kullanıcının kimliği.
            cover_letter (str): Başvuru sırasında eklenen ön yazı.
            status (str): Başvurunun güncel durumu (beklemede, kabul vb.).
            applied_at (str): Başvurunun yapıldığı tarih bilgisi.
        """
        self.id = id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.cover_letter = cover_letter
        self.status = status
        self.applied_at = applied_at

    @staticmethod
    def apply(job_id, applicant_id, cover_letter=""):
        """
        Yeni bir iş başvurusu oluşturur. Kullanıcının aynı ilana birden fazla
        başvuru yapmasını engellemek için mükerrer kontrolü yapar.

        Returns:
            tuple: (başarı durumu (bool), mesaj (str))
        """
        # Kullanıcının bu ilana daha önce başvurup başvurmadığını kontrol eder
        existing = db.fetchone(
            "SELECT id FROM applications WHERE job_id=? AND applicant_id=?",
            (job_id, applicant_id)
        )
        if existing:
            return False, "Bu ilana zaten başvurdunuz."

        # Yeni başvuru kaydını veritabanına ekler
        db.execute(
            "INSERT INTO applications (job_id, applicant_id, cover_letter) VALUES (?,?,?)",
            (job_id, applicant_id, cover_letter)
        )
        return True, "Başvurunuz alındı!"

    @staticmethod
    def get_by_applicant(applicant_id):
        """
        Belirli bir iş arayanın yapmış olduğu tüm başvuruları, ilan başlığı ve
        şirket bilgileriyle birlikte tarih sırasına göre getirir.
        """
        rows = db.fetchall(
            """SELECT a.*, j.title as job_title, j.company
               FROM applications a
                        JOIN jobs j ON a.job_id = j.id
               WHERE a.applicant_id = ?
               ORDER BY a.applied_at DESC""",
            (applicant_id,)
        )
        return rows

    @staticmethod
    def get_by_job(job_id):
        """
        Belirli bir iş ilanına yapılan tüm başvuruları, başvuran kişilerin
        kullanıcı adı ve e-posta bilgileriyle birlikte listeler.
        """
        rows = db.fetchall(
            """SELECT a.*, u.username, u.email
               FROM applications a
                        JOIN users u ON a.applicant_id = u.id
               WHERE a.job_id = ?
               ORDER BY a.applied_at DESC""",
            (job_id,)
        )
        return rows

    @staticmethod
    def update_status(app_id, new_status):
        """Veritabanındaki bir başvurunun durumunu (kabul, red, beklemede) günceller."""
        db.execute("UPDATE applications SET status=? WHERE id=?", (new_status, app_id))

    @staticmethod
    def get_by_id(app_id):
        """
        Benzersiz başvuru ID'si ile başvurunun tüm detaylarını sorgular
        ve bir Application nesnesi olarak döndürür.
        """
        r = db.fetchone("SELECT * FROM applications WHERE id=?", (app_id,))
        if r:
            return Application(r["id"], r["job_id"], r["applicant_id"], r["cover_letter"], r["status"], r["applied_at"])
        return None