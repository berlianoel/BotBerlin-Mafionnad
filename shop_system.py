
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from game_state import game_data

SHOP_ITEMS = {
    "protection": {
        "id": 1,
        "name": "🛡️ Protection",
        "price": 1000,
        "icon": "🛡️",
        "description": "Lindungi diri dari serangan malam"
    },
    "fake_id": {
        "id": 2,
        "name": "📄 Fake ID", 
        "price": 800,
        "icon": "📄",
        "description": "Sembunyikan identitasmu"
    },
    "double_vote": {
        "id": 3,
        "name": "✌️ Double Vote",
        "price": 1200,
        "icon": "✌️", 
        "description": "Vote bernilai 2x"
    },
    "gems": {
        "id": 4,
        "name": "💎 Gems",
        "price": 2000,
        "icon": "💎",
        "description": "Special currency"
    },
    "revival": {
        "id": 5,
        "name": "🔮 Revival",
        "price": 2500,
        "icon": "🔮",
        "description": "Hidup kembali"
    }
}

POINTS_PER_GAME = 100

def get_shop_keyboard():
    keyboard = []
    for item_id, item in SHOP_ITEMS.items():
        keyboard.append([
            InlineKeyboardButton(
                f"{item['icon']} {item['name']} - 💰{item['price']}", 
                callback_data=f"buy_{item_id}"
            )
        ])
    keyboard.append([InlineKeyboardButton("⬅️ Kembali", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

def get_player_stats(player_id):
    if str(player_id) not in game_data["player_stats"]:
        game_data["player_stats"][str(player_id)] = {
            "money": 0,
            "gems": 0,
            "protection": 0,
            "fake_id": 0,
            "items": {}
        }
    return game_data["player_stats"][str(player_id)]
