from database import db


class Employer:
    def __init__(self, user_id):
        """
        İşveren nesnesini başlatır ve ilgili kullanıcı kimliğini (ID) atar.

        Args:
            user_id (int): İşverenin kullanıcı tablosundaki benzersiz kimliği.
        """
        self.user_id = user_id

    def get_my_jobs(self):
        """
        Sistemde oturum açmış olan işverenin yayınladığı tüm iş ilanlarını listeler.

        Returns:
            list: İşverene ait Job nesnelerinden oluşan bir liste.
        """
        from job import Job
        return Job.get_by_employer(self.user_id)

    def get_applicants_for_job(self, job_id):
        """
        Belirli bir iş ilanı ID'si için yapılmış olan tüm başvuruları getirir.

        Args:
            job_id (int): Başvuruları görüntülenecek olan ilanın kimliği.

        Returns:
            list: Seçilen ilana yapılan başvuruları içeren Application nesneleri listesi.
        """
        from application import Application
        return Application.get_by_job(job_id)