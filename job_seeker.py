from database import db


class JobSeeker:
    def __init__(self, user_id):
        """
        İş arayan nesnesini başlatır ve ilgili kullanıcı kimliğini (ID) atar.

        Args:
            user_id (int): İş arayanın kullanıcı tablosundaki benzersiz kimliği.
        """
        self.user_id = user_id

    def get_applications(self):
        """
        İş arayan kullanıcının sistemdeki tüm iş başvurularını getirir.

        Returns:
            list: Kullanıcının yaptığı başvuruları içeren Application nesneleri listesi.
        """
        from application import Application
        return Application.get_by_applicant(self.user_id)