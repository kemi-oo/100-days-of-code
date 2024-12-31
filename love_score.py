def calculate_love_score(name1, name2):
    names_string = (name1 + name2).lower()
    #calculating for true
    true_score = ( 
        names_string.count("t") +
        names_string.count("r") +
        names_string.count("u") +
        names_string.count("e")
    )
    #calculating for love
    love_score = (
        names_string.count("l") +
        names_string.count("o") +
        names_string.count("v") +
        names_string.count("e")
    )   

    # Combine the scores to form a two-digit number
    total_score = int(f"{true_score}{love_score}")
    print(total_score)         
calculate_love_score(name1="oluwakemi", name2="odianose")