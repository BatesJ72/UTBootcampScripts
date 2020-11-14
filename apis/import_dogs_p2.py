import requests
import pandas as pd 

# Get API data
r = requests.get("https://api.thedogapi.com/v1/breeds")
# print(r.status_code)

data = r.json()
df = pd.DataFrame(data)
# print(df)
adj = df[["id","name","temperament"]]
adj["points"] = 0
# print(adj)

# Explode out list of temperament adj
split = adj.assign(temperament=adj.temperament.str.split(',')).explode('temperament')
split = split.reset_index()
# split = split.set_index("temperament")
# print(split)


# Create input for user
## add data validation so they can only choose items in the list

adj_list = [] 

def main():
    while True:
        print("-" * 50)
        print("Let's Find Your Perfect Pup!")

        user_choice = input("What characteristics would you like in your dog? Type out adjectives. Press q when you're done.\n")
        
        if user_choice == "q":
            break

        adj_list.append(user_choice)

        print(adj_list)
        
        # Take user input and match it to the adj list of temperaments
        if [split[split["temperament"] == user_choice]]:
            split["points"] += 1

main()

print(f"You want a dog that is {adj_list}")

# for a in adj_list:
#     print(f"You want a dog that is {a}")

print(split)

    

