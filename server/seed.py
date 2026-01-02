from app import app
from models import db, Newsletter

if __name__ == '__main__':
    with app.app_context():

        Newsletter.query.delete()

        newsletters = [
            Newsletter(
                title="First Newsletter",
                body="Welcome to our very first newsletter!"
            ),
            Newsletter(
                title="Tech Weekly",
                body="This week we talk about Flask RESTful APIs."
            ),
            Newsletter(
                title="Breaking News",
                body="Someone learned PATCH and DELETE today!"
            )
        ]

        db.session.add_all(newsletters)
        db.session.commit()

        print("🌱 Database seeded successfully!")
