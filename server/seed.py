from server.extensions import db
from server.app import app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Users
    user1 = User(username="admin")
    user1.password = "admin123"  # uses @password.setter to hash

    user2 = User(username="maverick")
    user2.password = "pharaoh"

    db.session.add_all([user1, user2])
    db.session.commit()

    # Guests
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Bill Gates", occupation="Philanthropist")
    guest3 = Guest(name="Zendaya", occupation="Actress")

    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    # Episodes
    ep1 = Episode(date=date(2024, 6, 10), number=1)
    ep2 = Episode(date=date(2024, 6, 11), number=2)
    ep3 = Episode(date=date(2024, 6, 12), number=3)

    db.session.add_all([ep1, ep2, ep3])
    db.session.commit()

    # Appearances
    a1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    a2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep1.id)
    a3 = Appearance(rating=3, guest_id=guest2.id, episode_id=ep2.id)
    a4 = Appearance(rating=5, guest_id=guest3.id, episode_id=ep3.id)

    db.session.add_all([a1, a2, a3, a4])
    db.session.commit()

    print("✅ Done seeding!")
