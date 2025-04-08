
ACHIEVEMENTS = {
    1: {
        "id": "first_win",
        "name": "🏆 First Victory",
        "description": "Menang pertama kali",
        "reward": 200
    },
    2: {
        "id": "mafia_master", 
        "name": "🔪 Mafia Master",
        "description": "Menang 5 kali sebagai Mafia",
        "reward": 500
    },
    "detective_pro": {
        "name": "🔎 Detective Pro",
        "description": "Berhasil menangkap 3 Mafia",
        "reward": 2000
    },
    "rich_player": {
        "name": "💰 Rich Player",
        "description": "Mengumpulkan 10000 coins",
        "reward": 5000
    },
    "collector": {
        "name": "🎭 Collector",
        "description": "Memiliki 5 item berbeda",
        "reward": 3000
    }
}

def check_achievements(player_id):
    stats = game_data["player_stats"].get(str(player_id), {})
    achievements = stats.get("achievements", [])
    new_achievements = []
    
    # Check each achievement condition
    if stats.get("wins", 0) >= 1 and "first_win" not in achievements:
        new_achievements.append("first_win")
        
    if stats.get("mafia_wins", 0) >= 5 and "mafia_master" not in achievements:
        new_achievements.append("mafia_master")
        
    return new_achievements
