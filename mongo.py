from pymongo import MongoClient

MONGO_URL = "mongodb+srv://arru8209:ARMANKING09X@cluster0.kh8ioei.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

    client.admin.command("ping")

    print("✅ MongoDB connection working!")

    db = client["mybot"]
    print("✅ Database:", db.name)

except Exception as e:
    print("❌ MongoDB connection failed:")
    print(e)
