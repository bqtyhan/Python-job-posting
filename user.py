from database import db


class User:
    """Sistemdeki kullanıcı verilerini temsil eden ve kullanıcı işlemlerini yöneten temel sınıf."""

    def __init__(self, id, username, email, role, created_at=None):
        """
        Bir kullanıcı nesnesini başlatır ve veritabanından alınan temel bilgileri atar.

        Args:
            id (int): Kullanıcının benzersiz kimliği.
            username (str): Kullanıcı adı.
            email (str): E-posta adresi.
            role (str): Kullanıcının yetki rolü (admin, employer, jobseeker).
            created_at (str, optional): Hesabın oluşturulma tarihi.
        """
        self.id = id
        self.username = username
        self.email = email
        self.role = role
        self.created_at = created_at

    @staticmethod
    def get_by_id(user_id):
        """
        Verilen kullanıcı ID'si ile veritabanında arama yapar ve eşleşen kullanıcıyı döner.

        Args:
            user_id (int): Aranacak kullanıcının kimlik numarası.

        Returns:
            User: Kullanıcı bulunursa User nesnesi, bulunamazsa None.
        """
        row = db.fetchone("SELECT * FROM users WHERE id = ?", (user_id,))
        if row:
            return User(row["id"], row["username"], row["email"], row["role"], row["created_at"])
        return None

    @staticmethod
    def get_all():
        """
        Sistemdeki tüm kayıtlı kullanıcıları veritabanından çeker ve liste olarak döndürür.

        Returns:
            list: User nesnelerinden oluşan bir liste.
        """
        rows = db.fetchall("SELECT * FROM users")
        return [User(r["id"], r["username"], r["email"], r["role"], r["created_at"]) for r in rows]

    @staticmethod
    def delete(user_id):
        """
        Belirtilen ID'ye sahip kullanıcıyı veritabanından kalıcı olarak siler.

        Args:
            user_id (int): Silinecek kullanıcının kimlik numarası.
        """
        db.execute("DELETE FROM users WHERE id = ?", (user_id,))

    def __repr__(self):
        """Kullanıcı nesnesinin terminal veya loglarda nasıl görüneceğini belirleyen metin temsilidir."""
        return f"<User {self.username} ({self.role})>"