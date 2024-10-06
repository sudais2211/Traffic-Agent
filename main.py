class TrafficAgent:
    def __init__(self):
        self.intersections = {}  # Store data for each intersection
        self.emergency_vehicle_detected = False
        self.threshold = 70  # Define a vehicle density threshold
        self.pedestrian_threshold = 5  # Define a pedestrian count threshold
    
    def update_intersection_data(self, intersection_id, vehicle_density, pedestrian_count, emergency_vehicle=False):
        self.intersections[intersection_id] = {
            'vehicle_density': vehicle_density,
            'pedestrian_count': pedestrian_count
        }
        if emergency_vehicle:
            self.emergency_vehicle_detected = True
    
    def optimize_traffic_flow(self):
        for intersection, data in self.intersections.items():
            if self.emergency_vehicle_detected:
                # Clear path for emergency vehicle
                self.give_priority_to_emergency_vehicle(intersection)
            elif data['vehicle_density'] > self.threshold:  # Use self.threshold here
                # Extend green light duration
                self.adjust_traffic_light(intersection, 'increase_green')
            elif data['pedestrian_count'] > self.pedestrian_threshold:  # Use self.pedestrian_threshold here
                # Prioritize pedestrian safety
                self.adjust_traffic_light(intersection, 'increase_red')
            else:
                # Standard light operation
                self.adjust_traffic_light(intersection, 'normal')
    
    def adjust_traffic_light(self, intersection_id, action):
        if action == 'increase_green':
            print(f"Increasing green light duration at {intersection_id}")
        elif action == 'increase_red':
            print(f"Increasing red light duration at {intersection_id}")
        else:
            print(f"Normal operation at {intersection_id}")
    
    def give_priority_to_emergency_vehicle(self, intersection_id):
        print(f"Clearing path for emergency vehicle at {intersection_id}")
        self.emergency_vehicle_detected = False

# Example usage:
agent = TrafficAgent()
agent.update_intersection_data('Intersection_1', vehicle_density=50, pedestrian_count=10)
agent.update_intersection_data('Intersection_2', vehicle_density=80, pedestrian_count=2, emergency_vehicle=True)
agent.optimize_traffic_flow()
