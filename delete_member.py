import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def delete_member(name:str):
    resp = supabase.table("members").delete().eq("name", name).execute()
    return resp.data
if __name__ == "__main__":
    name = input("Enter member name: ")

    deleted = delete_member(name)
    if deleted:
        print(f"Product with name {name} deleted successfully!")
    else:
        print(f" No product found with name {name}.")
