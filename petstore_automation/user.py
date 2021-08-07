def show_details(animal, count):
    i = 1
    comment = animal.upper()
    print(f"# {comment}")
    while i<=count:
        print(animal + "_list.append(f'{driver.find_element_by_xpath(product_id_"+animal+"_item"+str(i)+").text},{driver.find_element_by_xpath(name_"+animal+"_item"+str(i)+").text}')")
        i=i+1
    print()
        
        
show_details("fish", 4)
show_details("dog", 6)
show_details("cat", 2)
show_details("reptile", 2)
show_details("bird", 2)