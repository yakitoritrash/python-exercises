def love_calculator(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_number = sum(combined_names.count(letter) for letter in "true")
    love_number = sum(combined_names.count(letter) for letter in "love")
    
    love_score = int(f"{true_number}{love_number}")
    
    print(f"Love score = {love_score}")
    
love_calculator("lobster", "crabby")
          


    