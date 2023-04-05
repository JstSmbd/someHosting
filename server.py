import time
import requests
from json import dumps, loads


first = True
while True:
    res = requests.post("https://better-catkin-hat.glitch.me/post", json=
    {
        "meta": {
            "locale": "ru-RU",
            "timezone": "UTC",
            "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
            "interfaces": {
                "screen": {},
                "payments": {},
                "account_linking": {}
            }
        },
        "session": {
            "message_id": 4,
            "session_id": "38716ab0-f26c-4579-acb3-6489739e2bdb",
            "skill_id": "6869017c-0477-4aa4-bb30-83df617ad23d",
            "user": {
                "user_id": "F76484E69758D5A8F51F0125AF11793D70BCD3BC94769B4AAD4A4DADCD2A3E85"
            },
            "application": {
                "application_id": "E67D14610D87EB627CC5AFDA69A15525F43AA76D1B4013FADDD6FB97C36469F2"
            },
            "user_id": "E67D14610D87EB627CC5AFDA69A15525F43AA76D1B4013FADDD6FB97C36469F2",
            "new": first
        },
        "request": {
            "command": "помощь",
            "original_utterance": "Помощь",
            "nlu": {
                "tokens": [
                    "помощь"
                ],
                "entities": [],
                "intents": {}
            },
            "markup": {
                "dangerous_context": False
            },
            "type": "SimpleUtterance"
        },
        "version": "1.0"
    }).json()
    first = False
    print(res)
    time.sleep(20)
