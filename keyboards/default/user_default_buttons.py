from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_main_default_button(products: str, profile: str, basket: str, questions: str, posts: str):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"🛍 {products}")
            ],
            [
                KeyboardButton(text=f"👤 {profile}"),
                KeyboardButton(text=f"🛒 {basket}")
            ],
            [
                KeyboardButton(text=f"❓ {questions}")
            ],
            [
                KeyboardButton(text=f"📰 {posts}")
            ]
        ],
        resize_keyboard=True
    )
    return buttons
