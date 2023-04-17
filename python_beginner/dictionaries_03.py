# dictionarilerde value yerine liste ya da dictionary koyabiliyoruz
# nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
# nesting list in dict
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
# nesting dict in dict
travel_log = {
    "France": {"cities visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"cities visited": ["Berlin", "Hamburg", "Stuttgart"]}
}

# we can have dictinories inside lists

travel_log = [
    {"country": "France",
     "cities visited": ["Paris", "Lille", "Dijon"],
     "total visits": 12},
    {"country": "Germany",
     "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total visits": 5
     },
]
