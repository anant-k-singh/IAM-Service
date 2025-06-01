from sqlalchemy.orm import Session
from . import models, auth

def seed_database(db: Session):
    # Check if we already have users
    if db.query(models.User).first():
        print("Database already seeded!")
        return

    # Create sample users for each role
    sample_users = [
        {
            "email": "admin@example.com",
            "password": "Admin@123",
            "full_name": "Admin User",
            "role": models.UserRole.ADMIN
        },
        {
            "email": "legal@example.com",
            "password": "Legal@123",
            "full_name": "Legal User",
            "role": models.UserRole.LEGAL
        },
        {
            "email": "pm@example.com",
            "password": "PM@123",
            "full_name": "Project Manager",
            "role": models.UserRole.PM
        },
        {
            "email": "sales@example.com",
            "password": "Sales@123",
            "full_name": "Sales User",
            "role": models.UserRole.SALES
        },
        {
            "email": "user@example.com",
            "password": "User@123",
            "full_name": "Regular User",
            "role": models.UserRole.USER
        }
    ]

    # Create users
    for user_data in sample_users:
        hashed_password = auth.get_password_hash(user_data["password"])
        db_user = models.User(
            email=user_data["email"],
            full_name=user_data["full_name"],
            hashed_password=hashed_password,
            role=user_data["role"]
        )
        db.add(db_user)
    
    db.commit()
    print("Database seeded successfully!")

    # Print credentials for reference
    print("\nSample User Credentials:")
    print("------------------------")
    for user in sample_users:
        print(f"Email: {user['email']}")
        print(f"Password: {user['password']}")
        print(f"Role: {user['role'].value}")
        print("------------------------") 