from database import db
from user import User
import re


class AuthManager:
    current_user = None

    @staticmethod
    def register(username, password, email, role="jobseeker"):
        if not username or not password or not email:
            return False, "Tüm alanları doldurun."

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            return False, "Geçerli bir e-posta adresi girin."

        existing = db.fetchone("SELECT id FROM users WHERE username=? OR email=?", (username, email))
        if existing:
            return False, "Bu kullanıcı adı veya e-posta zaten kullanılıyor."

        db.execute(
            "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
            (username, password, email, role)
        )
        return True, "Kayıt başarılı! Giriş yapabilirsiniz."

    @staticmethod
    def login(username, password):
        row = db.fetchone(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password)
        )
        if row:
            AuthManager.current_user = User(row["id"], row["username"], row["email"], row["role"], row["created_at"])
            return True, "Giriş başarılı!"
        return False, "Kullanıcı adı veya şifre hatalı."

    @staticmethod
    def logout():
        AuthManager.current_user = None

    @staticmethod
    def is_logged_in():
        return AuthManager.current_user is not None

    @staticmethod
    def is_employer():
        return AuthManager.current_user and AuthManager.current_user.role == "employer"

    @staticmethod
    def is_admin():
        return AuthManager.current_user and AuthManager.current_user.role == "admin"

    @staticmethod
    def is_jobseeker():
        return AuthManager.current_user and AuthManager.current_user.role == "jobseeker"
