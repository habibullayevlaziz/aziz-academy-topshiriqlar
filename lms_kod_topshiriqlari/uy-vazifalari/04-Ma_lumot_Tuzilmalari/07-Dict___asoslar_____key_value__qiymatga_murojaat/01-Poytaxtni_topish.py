import sys
capitals = {"Uzbekistan": "Tashkent", "Japan": "Tokyo", "France": "Paris"}
print(capitals.get(sys.stdin.read().strip()))