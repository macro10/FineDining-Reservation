import sys
import json

def handle_reservation(reservation_data):
    """
    Handles the reservation data received from Rust
    """
    print("Received reservation data:", reservation_data)
    # You can add more processing here if needed

if __name__ == "__main__":
    # Read the reservation data from command line argument
    if len(sys.argv) > 1:
        try:
            reservation_data = json.loads(sys.argv[1])
            handle_reservation(reservation_data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}", file=sys.stderr)
    else:
        print("No reservation data provided", file=sys.stderr)
