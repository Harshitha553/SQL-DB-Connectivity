import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def add_member(name: str, email: str):
    data = {"name": name, "email": email}
    response = supabase.table("members").insert(data).execute()

    if response.data:
        print(f" Member registered successfully: {response.data[0]}")
    else:
        print(f" Failed to register member: {response}")
if __name__ == "__main__":
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    add_member(name, email)
