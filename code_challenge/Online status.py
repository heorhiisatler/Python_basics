#Online status
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Jack": "online",
    "Eveline": "online",
    "dick": "offline"
}

def online_count(st):
    i = 0
    for user in st:
        if st[user] == "online":
            i = i + 1
    return i

print(online_count(statuses))
