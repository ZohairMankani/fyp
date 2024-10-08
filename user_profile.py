# -*- coding: utf-8 -*-
"""user_profile.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J12lp0Y1m6OqnNZuez6Wt-HzUoCOEsf0
"""

import json
import os

user_profiles_file = "user_profiles.json"

def load_user_profiles():
    if os.path.exists(user_profiles_file):
        with open(user_profiles_file, "r") as file:
            return json.load(file)
    return {}

def save_user_profiles(profiles):
    with open(user_profiles_file, "w") as file:
        json.dump(profiles, file)

def create_or_update_profile(user_id, dietary_restrictions=None, preferences=None):
    profiles = load_user_profiles()
    profiles[user_id] = {
        "dietary_restrictions": dietary_restrictions or profiles.get(user_id, {}).get("dietary_restrictions", []),
        "preferences": preferences or profiles.get(user_id, {}).get("preferences", []),
    }
    save_user_profiles(profiles)
    print(f"Profile updated for user {user_id}: {profiles[user_id]}")