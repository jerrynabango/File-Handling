try:
    with open("my_file.txt", "w") as playbook:
        playbook.write("Jambo, kick-off.\n")
        playbook.write("58127\n")
        playbook.write("This is kick-off 3.\n")
except PermissionError:
    print("Permission denied. Unable to create or write to the playbook.")
except Exception as error:
    print(f"A turnover occurred: {error}")
finally:
    print("Playbook creation completed.")

try:
    with open("my_file.txt", "r") as playbook:
        print("Payload of the playbook:")
        print(playbook.read())
except FileNotFoundError:
    print("Playbook not found. Unable to read the playbook.")
except Exception as error:
    print(f"A fumble occurred: {error}")

try:
    with open("my_file.txt", "a") as playbook:
        playbook.write("Executing kick-off 4.\n")
        playbook.write("23234\n")
        playbook.write("Executing kick-off 6.\n")
except PermissionError:
    print("Permission denied. Unable to append to the playbook.")
except Exception as error:
    print(f"A false start occurred: {error}")
finally:
    print("Additional plays executed and recorded.")
