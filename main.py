
# Remove one # in front of the one that's relevant to you
#resource_names = ["Plate", "Lens", "Radio", "Polyester", "Chip"] # Rebel Troops
#resource_names = ["Bearing", "Gear", "Chip", "Prism", "Engine"] # Demon God
#resource_names = ["E", "A", "R", "T", "H"] # Earth's Will
#resource_names = ["Coolant", "Graphite", "Moderator", "Core", ""] # Dung Beetle
#resource_names = ["Pearl", "Shell", "Conch", "Core", ""] # Goldfish
#resource_names = ["Rune", "Crystal", "Cauldron", "Core", ""] # Surf Clam
#resource_names = ["Futures", "Bond", "Stock", "Core", ""] # Hamster
#resource_names = ["Fuel", "Control", "Penstock", "Core", ""] # Earthworm

# Fill this in with how much you have
current_resources = [
    [2, 37, 11, 8, 7],  # ResourceA quantities for tiers 1-5
    [0, 22, 30, 13, 0], # ResourceB
    [3, 7, 6, 9, 0],  # ResourceC
    [3, 10, 3, 13, 0],  # ResourceD
    [0, 20, 0, 0, 0]  # ResourceE
]

# Fill this in with how much you want
required_resources = [
    [200, 0, 0, 0, 0],  # Required ResourceA quantities
    [200, 0, 0, 0, 0],  # ResourceB
    [200, 0, 0, 0, 0],  # ResourceC
    [200, 0, 0, 0, 0],  # ResourceD
    [100, 0, 0, 0, 0]   # ResourceE
]


# The rest of this is code, ignore it!

import math
import pprint
import traceback

try:
    resource_names
except:
    print("You didn't uncommon a line of resource_names! Do that if you want these to be more useful.")
    resource_names = ["Resource A", "Resource B", "Resource C", "Resource D", "Resource E"]

def optimize_resources(resource_names, current_resources, required_resources):
    """
    Optimize resources by downgrading them to meet the required quantity.

    :param resource_names: List of resource names.
    :param current_resources: 2D array representing current resource quantities for each tier.
    :param required_resources: 2D array representing required resource quantities for each tier.
    :return: List of instructions for downgrading resources.
    """
    instructions = []
    num_resources = len(resource_names)

    # Function to recursively downgrade resources
    def downgrade(resource_index, target_tier, required_amount):
        required_amount -= current_resources[resource_index][target_tier]
        if required_amount <= 0:
            return

        # Try slurping some from the next tier
        nt_required_amount = math.ceil(required_amount / 5)
        instructions.append(f"Downgrade {nt_required_amount} T{target_tier + 2} {resource_names[resource_index]}")
        downgrade(resource_index, target_tier + 1, nt_required_amount)

    # Check each resource and tier to see if downgrading is needed
    for i in range(num_resources)[::-1]:
        for tier in range(0, 5):
            downgrade(i, tier, required_resources[i][tier])

    return instructions[::-1]


# Optimize resources
try:
    instructions = optimize_resources(resource_names, current_resources, required_resources)
    pprint.pprint(instructions)
except Exception:
    print("whoops something went wrong, either it's impossible or I have a bug, sorry")
    print()
    print()
    print()
    print(traceback.format_exc())


