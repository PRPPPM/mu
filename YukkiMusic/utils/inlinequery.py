#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="‹ ايقاف التشغيل موقتاً ›",
            description=f"يقوم بإيقاف التشغيل الحالي على مكالمة الجماعية.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="‹ استئناف التشغيل ›",
            description=f"استئناف التشغيل الجاري على مكالمة جماعية.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="‹ كتم صوت التشغيل ›",
            description=f"كتم الصوت المشغل في مكالمة المجموعة.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="‹ الغاء كتم صوت التشغيل ›",
            description=f"إلغاء كتم صوت  في مكالمة الجماعية.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="‹ تخطي الاغنية المشغلة ›",
            description=f"تخطي الاغنيه. | للحصول على رقم المسار المحدد: /skip [رقم المسار] ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="‹ انهاء ↫ ايقاف التشغيل ›",
            description="أوقف التشغيل الجاري على المكالمة الجماعية.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="‹ تغيير ترتيب قائمه الانتظار ›",
            description="تبديل قائمة المسارات في قائمة الانتظار.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="‹ تخطي الاغنية المشغلة ›",
            description="تخطي مقطع من  الاغنيه او الفديو.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="‹ تكرار الاغنية ›",
            description="قم بتكرار الموسيقى قيد التشغيل الحالية. | الاستخدام:  /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
