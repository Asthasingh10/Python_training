import time

def traffic_light_simulation(cycles):
    for i in range(cycles):
        print(f"\n🚦 Cycle {i + 1}")
        # Red Light
        print("🔴 RED - STOP")
        time.sleep(5)

        # Green Light
        print("🟢 GREEN - GO")
        time.sleep(5)

        # Yellow Light
        print("🟡 YELLOW - SLOW DOWN")
        time.sleep(2)

    print("\n✅ Simulation Complete!")

# Run the simulation for 3 cycles
traffic_light_simulation(3)
