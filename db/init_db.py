from pymongo import MongoClient
import os

def initialize_if_needed():
    """Seeds the MongoDB with sample user and their data if empty."""
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://nlp-mongo:27017/"))
    db = client["daribrain"]

    users = db["users"]
    grammar_notes = db["grammar_notes"]
    notes = db["personal_notes"]
    vocab = db["vocab_book"]

    # Seed only if no users exist
    if users.count_documents({}) == 0:
        print("🔄 Seeding MongoDB...")

        # Create a sample user
        test_user = {
            "username": "test_user",
            "email": "test@example.com",
            "role": "student"
        }
        user_id = users.insert_one(test_user).inserted_id

        # Seed grammar notes
        grammar_notes.insert_many([
            {"user_id": user_id, "title": "Present Simple", "description": "Used for daily routines."},
            {"user_id": user_id, "title": "Future Tense", "description": "Used for future plans."}
        ])

        # Seed personal notes
        notes.insert_one({
            "user_id": user_id,
            "title": "First Note",
            "content": "This is a sample note."
        })

        # Seed vocab
        vocab.insert_one({
            "user_id": user_id,
            "word": "سفر",
            "meaning": "travel",
            "synonyms": "گردش، مسافرت",
            "example": "من به سفر رفتم"
        })

        print("✅ MongoDB initialized with test data.")
    else:
        print("ℹ️ MongoDB already has data. Skipping init.")
