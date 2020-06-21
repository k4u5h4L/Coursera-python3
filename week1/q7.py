nested_d = {
    "Beijing": {
        "China": 51,
        "USA": 36,
        "Russia": 22,
        "Great Britain": 19
    },
    "London": {
        "USA": 46,
        "China": 38,
        "Great Britain": 29,
        "Russia": 22
    },
    "Rio": {
        "USA": 35,
        "Great Britain": 22,
        "China": 20,
        "Germany": 13
    }
}

US_count = []

for i in nested_d:
    US_count.append(nested_d[i]['USA'])

print(US_count)
