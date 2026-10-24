import heapq

# Flight data:
# destination: (time, fuel, weather, congestion)
graph = {
    "Delhi": {
        "Mumbai": (2.2,4500,2,3), "Jaipur": (1,1800,1,1),
        "Kolkata": (2.3,4200,3,2), "Dubai": (3.5,7000,2,2),
        "Singapore": (5.8,12000,2,3)
    },
    "Mumbai": {
        "Delhi": (2.2,4500,2,3), "Ahmedabad": (1,1700,2,1),
        "Bangalore": (1.8,3200,1,2), "Dubai": (3,6500,2,2)
    },
    "Jaipur": {
        "Delhi": (1,1800,1,1), "Ahmedabad": (1.2,2000,2,2)
    },
    "Kolkata": {
        "Delhi": (2.3,4200,3,2), "Bangalore": (2.5,4300,2,3),
        "Singapore": (4,9000,2,3)
    },
    "Bangalore": {
        "Mumbai": (1.8,3200,1,2), "Kolkata": (2.5,4300,2,3),
        "Chennai": (1,1700,1,1), "Singapore": (4.5,10000,2,3)
    },
    "Ahmedabad": {
        "Mumbai": (1,1700,2,1), "Jaipur": (1.2,2000,2,2),
        "Dubai": (2.8,6000,2,2)
    },
    "Chennai": {
        "Bangalore": (1,1700,1,1), "Singapore": (4,8500,2,2)
    },
    "Dubai": {
        "Delhi": (3.5,7000,2,2), "Mumbai": (3,6500,2,2),
        "Ahmedabad": (2.8,6000,2,2), "London": (7.2,18000,3,3),
        "Paris": (7,17500,2,3)
    },
    "London": {
        "Dubai": (7.2,18000,3,3), "Paris": (1.3,3500,1,2),
        "New York": (8,20000,2,3)
    },
    "Paris": {
        "London": (1.3,3500,1,2), "Dubai": (7,17500,2,3),
        "New York": (8.5,21000,2,3)
    },
    "Singapore": {
        "Delhi": (5.8,12000,2,3), "Kolkata": (4,9000,2,3),
        "Bangalore": (4.5,10000,2,3), "Chennai": (4,8500,2,2),
        "Tokyo": (7,15000,2,3), "Sydney": (8,17000,2,3)
    },
    "Tokyo": {
        "Singapore": (7,15000,2,3), "Sydney": (9.5,21000,2,3),
        "New York": (13,30000,3,4)
    },
    "Sydney": {
        "Singapore": (8,17000,2,3), "Tokyo": (9.5,21000,2,3)
    },
    "New York": {
        "London": (8,20000,2,3), "Paris": (8.5,21000,2,3),
        "Tokyo": (13,30000,3,4), "Toronto": (1.5,4000,1,2)
    },
    "Toronto": {
        "New York": (1.5,4000,1,2)
    }
}


def cost(data):
    time, fuel, weather, congestion = data
    return time * 100 + fuel * 0.10 + weather * 50 + congestion * 50


def dijkstra(start, end):
    dist = {city: float("inf") for city in graph}
    parent = {city: None for city in graph}
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        current_cost, city = heapq.heappop(queue)

        if current_cost > dist[city]:
            continue
        if city == end:
            break

        for next_city, data in graph[city].items():
            new_cost = current_cost + cost(data)

            if new_cost < dist[next_city]:
                dist[next_city] = new_cost
                parent[next_city] = city
                heapq.heappush(queue, (new_cost, next_city))

    if dist[end] == float("inf"):
        return None, None

    route = []
    city = end

    while city:
        route.append(city)
        city = parent[city]

    return route[::-1], dist[end]


def details(route):
    time = fuel = weather = congestion = 0

    for a, b in zip(route, route[1:]):
        t, f, w, c = graph[a][b]
        time += t
        fuel += f
        weather += w
        congestion += c

    return time, fuel, weather, congestion


# ---------------- MAIN PROGRAM ----------------

print("\n" + "=" * 50)
print("                SKYPATH OPTIMIZER")
print("          Dijkstra's Algorithm")
print("=" * 50)

print("\nAvailable Airports:")
print(", ".join(graph))

start = input("\nEnter departure airport: ").strip()
end = input("Enter destination airport: ").strip()

if start not in graph or end not in graph:
    print("\nInvalid airport name!")

elif start == end:
    print("\nDeparture and destination cannot be the same!")

else:
    route, total_cost = dijkstra(start, end)

    if route is None:
        print("\nNo route found!")

    else:
        time, fuel, weather, congestion = details(route)

        print("\n" + "=" * 50)
        print("                 ROUTE RESULT")
        print("=" * 50)

        print("\nOptimal Route:")
        print(" -> ".join(route))

        print("\nFlight Details:")
        print(f"Total Flight Time      : {time:.2f} hours")
        print(f"Total Fuel Consumption : {fuel:.2f} L")
        print(f"Weather Penalty        : {weather}")
        print(f"Congestion Penalty     : {congestion}")
        print(f"Total Route Cost       : {total_cost:.2f}")

        print("\nAlgorithm: Dijkstra's Algorithm")
        print("Time Complexity: O((V + E) log V)")

        print("=" * 50)