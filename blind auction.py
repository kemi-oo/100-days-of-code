import blind_auction_art
print(blind_auction_art.logo)
print("Welcome To The Blind Auction")

bid_information = {}
bids = []


bidding = "true"
# TODO-1: Ask the user for input
while bidding == "true":
    name = input("what's your name?\n")
    bid_amount = int(input("how much are you bidding?\n$"))
    bids.append(bid_amount)
# TODO-2: Save data into dictionary {name: price}
    bid_information[name] = bid_amount

# TODO-3: Whether if new bids need to be added
    more_bidders = input("are there more bidders. yes/no?\n").lower()
    if more_bidders == "yes":
        print("\n" * 50)
    elif more_bidders == "no":
        bidding = "false"
        print("\n" * 50)
    else:
        print("\n" * 50 , "wrong input")

# TODO-4: Compare bids in dictionary
for key, value in bid_information.items():
    if value == max(bids):
        highest_bidder = key
        print(f"The highest bidder is {highest_bidder} with a bid of ${max(bids)}")
