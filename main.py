def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Starting at position (0, 0).")
    print("Enter N/S/E/W to move, or STOP to end.")

    while True:
        # Get user input (normalize it to lowercase for consistency)
        command = input("Enter direction: ").strip().lower()

        # Check for STOP
        if command == "stop":
            print("Session ended.")
            break

        # Handle valid moves
        elif command in ["n", "north"]:
            y += 1
        elif command in ["s", "south"]:
            y -= 1
        elif command in ["e", "east"]:
            x += 1
        elif command in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input. Please enter N/S/E/W or STOP.")
            continue  # Skip showing position if invalid

        # Show current position after valid move
        print(f"Current position: ({x}, {y})")

    # After session ends, show final position
    print(f"Final position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin.")


# Run the program
gps_tracker()
