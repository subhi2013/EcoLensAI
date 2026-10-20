import json
try:
    with open("waste_data.json", "r") as file:
        waste_observations = json.load(file)

except json.JDONDecodeError:
    print("No saved observations found. Starting with an empty list.")
    waste_observations = []
observation1 = {"item":"plastic bottle","category":"plastic"}
waste_observations.append(observation1)
print(waste_observations)
observation2 = {"item":"banana peel","category":"organic waste"}
waste_observations.append(observation2)
print("\---------ECO LENS WASTE REPORT------")
print("=====================================")
print("total observation:",len(waste_observations))
print("first item:",observation1["item"])
if observation1["category"] == "plastic":
    print("the first item is plastic")
else:
    print("the first item is not plastic")
plastic_count = 0
for observations in waste_observations:
    if observations["category"] == "plastic":
        plastic_count += 1
print("plastic waste count:", plastic_count)
organic_count = 0
for observations in waste_observations:
    if observations["category"] == "organic waste":
        organic_count += 1
print("organic waste count:", organic_count)
print("total no of waste observations:",len(waste_observations))
print("total no of plastic observations:",plastic_count)
print("total no of organic observations:",organic_count)
if plastic_count > organic_count:
    print("plastic waste is more common")
elif organic_count > plastic_count:
    print("organic waste is more common")
else:
    print("both categories have equal counts")
with open("waste_data.json", "r") as file:
    waste_observations = json.load(file)
categories = ["plastic","organic","recyclable"]
item = input("enter a waste item:").strip() 
category = input("enter its category:").lower().strip()
with open("waste_data.json", "w") as file:
    json.dump(waste_observations, file, indent=4)

print("Observation saved successfully!")
if item == "" or category == "":
    print("error:item and category cannot be empty")
elif category not in categories:
    print("invalid category!please enter plastic,organic,or recyclable")
else:
    new_observations = {"item":item,"category":category}
    waste_observations.append(new_observations)
for observation in waste_observations:
    print(observation)
category_counts = {}
for observation in waste_observations:
    category = observation["category"]
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1
print(category_counts)
recyclable_count = category_counts.get("recyclable", 0)
if category_counts:
    most_common_category = max(category_counts, key=category_counts.get)
    print("most common category:",most_common_category)
    print("number of observations:")
    category_counts[most_common_category]
    largest_count = category_counts[most_common_category]
    print(f"{most_common_category.title()} waste is the largest category with {largest_count} observations")
else:
    print("no waste observations available yet")
search_item = input("enter a waste item to search:").strip().lower()
found = False
for observation in waste_observations:
    if observation["item"].strip().lower() == search_item:
        print("category:",observation["category"])
        found = True
        if found == False:
            print("waste item not found")
total_count = len(waste_observations)
recyclable_percentage = (recyclable_count / total_count) * 100
print("recyclable percentage:",recyclable_percentage, "%")
percentage = (category_counts[category] / total_count) * 100
print(f"{category}:{percentage:.1f}%")
ranked_categories = sorted(category_counts.items(),
                           key=lambda item: item[1],
                           reverse=True)
for rank, (category, count) in enumerate(ranked_categories,start=1):
    print(f"{rank}.{category.title()}-{count}")
if most_common_category == "plastic":
    print("please reduce single use plastics")
elif most_common_category == "organic waste":
    print("try composting food scraps to reduce waste")
else:
    print("sort recyclable materials and send them for recycling")
if not waste_observations:
    print("no waste observations available yet, add observations to generate insights")
