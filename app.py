import replicate
import os

# This checks if the API key is set in the environment
token = os.environ.get("REPLICATE_API_TOKEN")

if not token:
    print("❌ Error: REPLICATE_API_TOKEN is not set.")
else:
    print(f"✅ Token found: {token[:6]}... (Testing connection)")
    try:
        # We run a very simple "hello-world" model to see if it responds
        output = replicate.run(
            "replicate/hello-world:5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa",
            input={"text": "Test Connection"}
        )
        print(f"🚀 Success! Replicate returned: {output}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
