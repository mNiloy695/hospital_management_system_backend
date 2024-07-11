import random

# Define the range of numbers
start = 683458
end = 683509

# Define excluded members and leaders
excluded_members = {683499, 683500, 683459}
leaders = [683485, 683475, 683486, 683494, 189160, 189163]

# Generate numbers excluding excluded members
numbers = [num for num in range(start, end + 1) if num not in excluded_members]

# Shuffle the numbers
random.shuffle(numbers)

# Function to create groups
def create_groups(numbers, leaders):
    groups = []
    while len(numbers) >= 6:  # We need exactly 6 members per group to fit a leader
        # Randomly choose a leader
        leader = random.choice(leaders)
        # Select 6 other members for the group
        group_members = random.sample
