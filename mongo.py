from pymongo import MongoClient

MONGO_URL = "mongodb+srv://arru8209:armanking09x@cluster0.hhlnxa9.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

    # Test connection
    client.admin.command("ping")

    print("✅ MongoDB connection working!")
    print("Database:", client.get_default_database())

except Exception as e:
    print("❌ MongoDB connection failed:")
    print(e)
