from database import db


class User:
    def __init__(self, id, username, email, role, created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.role = role
        self.created_at = created_at

    @staticmethod
    def get_by_id(user_id):
        row = db.fetchone("SELECT * FROM users WHERE id = ?", (user_id,))
        if row:
            return User(row["id"], row["username"], row["email"], row["role"], row["created_at"])
        return None

    @staticmethod
    def get_all():
        rows = db.fetchall("SELECT * FROM users")
        return [User(r["id"], r["username"], r["email"], r["role"], r["created_at"]) for r in rows]

    @staticmethod
    def delete(user_id):
        db.execute("DELETE FROM users WHERE id = ?", (user_id,))

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"
