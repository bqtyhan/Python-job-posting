from database import db
from user import User
import re


class AuthManager:
    """Kullanıcı kayıt, giriş ve oturum yönetimi işlemlerini yürüten merkezi yönetim sınıfı."""

    # Oturum açmış olan mevcut kullanıcı nesnesini tutar
    current_user = None

    @staticmethod
    def register(username, password, email, role="jobseeker"):
        """
        Sisteme yeni bir kullanıcı kaydeder. Kullanıcı adı, şifre ve e-posta kontrolü yapar.

        Args:
            username (str): Kullanıcı adı.
            password (str): Şifre.
            email (str): E-posta adresi.
            role (str): Kullanıcı rolü (varsayılan: 'jobseeker').

        Returns:
            tuple: (başarı durumu (bool), mesaj (str))
        """
        # Alanların boş olup olmadığını kontrol eder
        if not username or not password or not email:
            return False, "Tüm alanları doldurun."

        # E-posta formatının geçerliliğini regex ile kontrol eder
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            return False, "Geçerli bir e-posta adresi girin."

        # Kullanıcı adı veya e-postanın sistemde zaten var olup olmadığını kontrol eder
        existing = db.fetchone("SELECT id FROM users WHERE username=? OR email=?", (username, email))
        if existing:
            return False, "Bu kullanıcı adı veya e-posta zaten kullanılıyor."

        # Yeni kullanıcıyı veritabanına ekler
        db.execute(
            "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
            (username, password, email, role)
        )
        return True, "Kayıt başarılı! Giriş yapabilirsiniz."

    @staticmethod
    def login(username, password):
        """
        Kullanıcı adı ve şifre ile sisteme giriş yapar. Başarılıysa oturum bilgilerini saklar.

        Args:
            username (str): Kullanıcı adı.
            password (str): Şifre.

        Returns:
            tuple: (başarı durumu (bool), mesaj (str))
        """
        # Veritabanında eşleşen kullanıcıyı arar
        row = db.fetchone(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password)
        )
        if row:
            # Kullanıcı bulunduysa User nesnesini oluşturur ve oturumu başlatır
            AuthManager.current_user = User(
                row["id"],
                row["username"],
                row["email"],
                row["role"],
                row["created_at"]
            )
            return True, "Giriş başarılı!"

        return False, "Kullanıcı adı veya şifre hatalı."

    @staticmethod
    def logout():
        """Aktif kullanıcı oturumunu sonlandırır ve mevcut kullanıcı bilgisini temizler."""
        AuthManager.current_user = None

    @staticmethod
    def is_logged_in():
        """
        Sistemde aktif bir oturum olup olmadığını kontrol eder.

        Returns:
            bool: Oturum açılmışsa True, aksi halde False.
        """
        return AuthManager.current_user is not None

    @staticmethod
    def is_employer():
        """
        Oturum açan kullanıcının 'işveren' rolünde olup olmadığını kontrol eder.

        Returns:
            bool: İşveren ise True.
        """
        return AuthManager.current_user and AuthManager.current_user.role == "employer"

    @staticmethod
    def is_admin():
        """
        Oturum açan kullanıcının 'admin' rolünde olup olmadığını kontrol eder.

        Returns:
            bool: Yönetici ise True.
        """
        return AuthManager.current_user and AuthManager.current_user.role == "admin"

    @staticmethod
    def is_jobseeker():
        """
        Oturum açan kullanıcının 'iş arayan' rolünde olup olmadığını kontrol eder.

        Returns:
            bool: İş arayan ise True.
        """
        return AuthManager.current_user and AuthManager.current_user.role == "jobseeker"