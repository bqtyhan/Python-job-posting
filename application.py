from database import db


class ApplicationStatus:
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    ALL = [PENDING, ACCEPTED, REJECTED]
    LABELS = {
        PENDING: "Beklemede",
        ACCEPTED: "Kabul Edildi",
        REJECTED: "Reddedildi"
    }


class Application:
    def __init__(self, id, job_id, applicant_id, cover_letter, status, applied_at):
        self.id = id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.cover_letter = cover_letter
        self.status = status
        self.applied_at = applied_at

    @staticmethod
    def apply(job_id, applicant_id, cover_letter=""):
        # Aynı ilana tekrar başvurma
        existing = db.fetchone(
            "SELECT id FROM applications WHERE job_id=? AND applicant_id=?",
            (job_id, applicant_id)
        )
        if existing:
            return False, "Bu ilana zaten başvurdunuz."
        db.execute(
            "INSERT INTO applications (job_id, applicant_id, cover_letter) VALUES (?,?,?)",
            (job_id, applicant_id, cover_letter)
        )
        return True, "Başvurunuz alındı!"

    @staticmethod
    def get_by_applicant(applicant_id):
        rows = db.fetchall(
            """SELECT a.*, j.title as job_title, j.company FROM applications a
               JOIN jobs j ON a.job_id = j.id
               WHERE a.applicant_id=? ORDER BY a.applied_at DESC""",
            (applicant_id,)
        )
        return rows

    @staticmethod
    def get_by_job(job_id):
        rows = db.fetchall(
            """SELECT a.*, u.username, u.email FROM applications a
               JOIN users u ON a.applicant_id = u.id
               WHERE a.job_id=? ORDER BY a.applied_at DESC""",
            (job_id,)
        )
        return rows

    @staticmethod
    def update_status(app_id, new_status):
        db.execute("UPDATE applications SET status=? WHERE id=?", (new_status, app_id))

    @staticmethod
    def get_by_id(app_id):
        r = db.fetchone("SELECT * FROM applications WHERE id=?", (app_id,))
        if r:
            return Application(r["id"], r["job_id"], r["applicant_id"], r["cover_letter"], r["status"], r["applied_at"])
        return None
