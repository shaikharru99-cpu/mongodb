from pymongo import MongoClient

MONGO_URL = ""

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

    client.admin.command("ping")

    print("✅ MongoDB connection working!")

    db = client["mybot"]
    print("✅ Database:", db.name)

except Exception as e:
    print("❌ MongoDB connection failed:")
    print(e)
