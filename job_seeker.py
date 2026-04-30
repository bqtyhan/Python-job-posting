from database import db


class JobSeeker:
    def __init__(self, user_id, full_name="", phone="", bio="", skills=""):
        self.user_id = user_id
        self.full_name = full_name
        self.phone = phone
        self.bio = bio
        self.skills = skills

    @staticmethod
    def get_profile(user_id):
        row = db.fetchone("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
        if row:
            return JobSeeker(row["user_id"], row["full_name"], row["phone"], row["bio"], row["skills"])
        return JobSeeker(user_id)

    def save(self):
        existing = db.fetchone("SELECT id FROM profiles WHERE user_id = ?", (self.user_id,))
        if existing:
            db.execute(
                "UPDATE profiles SET full_name=?, phone=?, bio=?, skills=? WHERE user_id=?",
                (self.full_name, self.phone, self.bio, self.skills, self.user_id)
            )
        else:
            db.execute(
                "INSERT INTO profiles (user_id, full_name, phone, bio, skills) VALUES (?,?,?,?,?)",
                (self.user_id, self.full_name, self.phone, self.bio, self.skills)
            )

    def get_applications(self):
        from application import Application
        return Application.get_by_applicant(self.user_id)
