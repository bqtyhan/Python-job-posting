from database import db


class NotificationManager:
    @staticmethod
    def send(user_id, message):
        db.execute(
            "INSERT INTO notifications (user_id, message) VALUES (?,?)",
            (user_id, message)
        )

    @staticmethod
    def get_unread(user_id):
        return db.fetchall(
            "SELECT * FROM notifications WHERE user_id=? AND is_read=0 ORDER BY created_at DESC",
            (user_id,)
        )

    @staticmethod
    def get_all(user_id):
        return db.fetchall(
            "SELECT * FROM notifications WHERE user_id=? ORDER BY created_at DESC",
            (user_id,)
        )

    @staticmethod
    def mark_read(notif_id):
        db.execute("UPDATE notifications SET is_read=1 WHERE id=?", (notif_id,))

    @staticmethod
    def mark_all_read(user_id):
        db.execute("UPDATE notifications SET is_read=1 WHERE user_id=?", (user_id,))

    @staticmethod
    def unread_count(user_id):
        row = db.fetchone(
            "SELECT COUNT(*) as cnt FROM notifications WHERE user_id=? AND is_read=0",
            (user_id,)
        )
        return row["cnt"] if row else 0
