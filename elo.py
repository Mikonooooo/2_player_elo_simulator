from datetime import datetime

def main():
    p1 = int(input("Starting Elo for P1: "))
    p2 = int(input("Starting Elo for P2: "))
    k = int(input("Elo k factor: "))
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f_name = f"log_{t}.txt"
    game_counter = 0
    
    with open(f_name, "a") as f:
        f.write(f"Session started at {t}\n")
        f.write(f"Initial Elo - P1: {p1}, P2: {p2}, K factor: {k}\n")
        
        while True:
            user_input = input("Enter '1' for P1 win, '0' for P2 win, 'q' to quit: ")
            if user_input == "q":
                break
            elif user_input in ["0", "1"]:
                s = int(user_input)
                game_counter += 1
                e1 = 1 / (1 + 10 ** ((p2 - p1) / 400))
                e2 = 1 / (1 + 10 ** ((p1 - p2) / 400))
                p1 = round(p1 + k * (s - e1))
                p2 = round(p2 + k * ((1 - s) - e2))
                print(f"P1: {p1}")
                print(f"P2: {p2}")
                f.write(f"Game {game_counter}: {'P1 wins' if s == 1 else 'P2 wins'}, P1: {p1}, P2: {p2}\n")
            else:
                print("Invalid input.")
                
    print(f"Logs saved to {f_name}")

if __name__ == "__main__":
    main()