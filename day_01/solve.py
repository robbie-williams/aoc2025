import sys

def solve():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input'
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    pos = 50
    count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            # Count multiples of 100 in [pos - distance, pos - 1]
            # Formula: floor((pos - 1) / 100) - floor((pos - distance - 1) / 100)
            added = (pos - 1) // 100 - (pos - distance - 1) // 100
            count += added
            pos = (pos - distance) % 100
        elif direction == 'R':
            # Count multiples of 100 in (pos, pos + distance]
            # Formula: floor((pos + distance) / 100) - floor(pos / 100)
            added = (pos + distance) // 100 - pos // 100
            count += added
            pos = (pos + distance) % 100
            
    print(f"Password: {count}")

if __name__ == '__main__':
    solve()
