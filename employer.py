import re
from database import db


class Employer:
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
            return Employer(row["user_id"], row["full_name"], row["phone"], row["bio"], row["skills"])
        return Employer(user_id)

    def save(self):
        if self.phone and not re.match(r"^(\+90|0)?[0-9]{10}$", self.phone):
            return False, "Geçerli bir telefon numarası girin."

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
        return True, "Profil güncellendi."

    def get_my_jobs(self):
        from job import Job
        return Job.get_by_employer(self.user_id)

    def get_applicants_for_job(self, job_id):
        from application import Application
        return Application.get_by_job(job_id)