config = ("Linux", "Python", 3.10)
# config[0] = "Windows"  # This will raise an error (immutable)

for setting in config:
    print("System config:", setting)
