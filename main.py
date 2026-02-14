import os
import shutil

# ===== НАСТРОЙКИ =====
STEAM_PATH = r"E:\Steam"  # Путь к Steam

# ИГРЫ ДЛЯ СОХРАНЕНИЯ (название папки: ID игры)
KEEP_GAMES = {
    "Counter-Strike Global Offensive": "730",
    "dota 2 beta": "570",
    "Deadlock": "1422450",
    "Steamworks Shared": "228980",
    "PUBG": "578080",
    "pubg": "578080",
}
# =====================

def main():
    print("=" * 50)
    print("STEAM CLEANER".center(50))
    print("=" * 50)
    print(f"Steam path: {STEAM_PATH}")
    print("\nGames to KEEP:")
    for game, game_id in KEEP_GAMES.items():
        print(f"  ✅ {game} (ID: {game_id})")
    
    # Счетчики
    deleted_folders = 0
    deleted_manifests = 0
    deleted_userdata = 0
    
    print("\n" + "=" * 50)
    print("DELETING GAMES...")
    print("=" * 50)
    
    # 1. Удаление папок игр
    common_path = os.path.join(STEAM_PATH, "steamapps", "common")
    if os.path.exists(common_path):
        print("\n📁 Checking game folders...")
        for folder in os.listdir(common_path):
            folder_path = os.path.join(common_path, folder)
            if os.path.isdir(folder_path):
                if folder not in KEEP_GAMES:
                    try:
                        print(f"  Deleting: {folder}")
                        shutil.rmtree(folder_path)
                        deleted_folders += 1
                    except Exception as e:
                        print(f"  ❌ Error deleting {folder}: {e}")
                else:
                    print(f"  ✅ Keeping: {folder}")
    
    # 2. Удаление манифестов
    steamapps_path = os.path.join(STEAM_PATH, "steamapps")
    if os.path.exists(steamapps_path):
        print("\n📄 Checking manifest files...")
        for file in os.listdir(steamapps_path):
            if file.startswith("appmanifest_") and file.endswith(".acf"):
                file_path = os.path.join(steamapps_path, file)
                game_id = file.replace("appmanifest_", "").replace(".acf", "")
                
                if game_id not in KEEP_GAMES.values():
                    try:
                        print(f"  Deleting: {file}")
                        os.remove(file_path)
                        deleted_manifests += 1
                    except Exception as e:
                        print(f"  ❌ Error deleting {file}: {e}")
                else:
                    print(f"  ✅ Keeping: {file}")
    
    # 3. Удаление пользовательских данных
    userdata_path = os.path.join(STEAM_PATH, "userdata")
    if os.path.exists(userdata_path):
        print("\n👤 Checking user data...")
        for user in os.listdir(userdata_path):
            user_path = os.path.join(userdata_path, user)
            if os.path.isdir(user_path):
                for game_id in os.listdir(user_path):
                    game_data_path = os.path.join(user_path, game_id)
                    if os.path.isdir(game_data_path) and game_id.isdigit():
                        if game_id not in KEEP_GAMES.values():
                            try:
                                print(f"  Deleting user data for game ID {game_id} (user: {user})")
                                shutil.rmtree(game_data_path)
                                deleted_userdata += 1
                            except Exception as e:
                                print(f"  ❌ Error deleting user data: {e}")
    
    # Итог
    print("\n" + "=" * 50)
    print("COMPLETE!".center(50))
    print("=" * 50)
    print("📊 Statistics:")
    print(f"  🗑️  Game folders deleted: {deleted_folders}")
    print(f"  🗑️  Manifests deleted: {deleted_manifests}")
    print(f"  🗑️  User data deleted: {deleted_userdata}")
    print("\n🔄 Restart Steam to see changes.")

if __name__ == "__main__":
    # Проверяем путь
    if not os.path.exists(STEAM_PATH):
        print(f"❌ Error: Steam path not found: {STEAM_PATH}")
    else:
        main()
