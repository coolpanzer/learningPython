# Dictionaries are key value pairs

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": {
        "1": "Fools"
    },
    "May": {
        "12": ["Labor Day", "Birthday"]
    }
}

print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Apr").get("1"))
print(monthConversions.get("May").get("12"))


