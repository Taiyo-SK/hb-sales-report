"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # creates empty list for salespeople
melons_sold = [] # creates empty list for melons sold
# guessing that both of these are outputted at the end of the program

f = open('sales-report.txt') # opens the sales report file, i.e. our sales data
# this is our data variable for the program

for line in f: # begins a for loop to iterate over each line in our data
    line = line.rstrip() # removes trailing space and the line break indicators
    entries = line.split('|') # yields the three pieces of data in each line, as separate strings
                                # returns as a list of strings
    salesperson = entries[0] # var where the first element of the list is the salesperson's name
    melons = int(entries[2]) # var where the third element is the number of melons
                                # type cast as integer and assign to var

    if salesperson in salespeople: # begins a nested if statement inside our for loop
                                    # compares the specific salesperson 
                                    # in the global salespeople list
        position = salespeople.index(salesperson) # assigns the index position for 
                                                    # that salesperson in the global list
        melons_sold[position] += melons # adds the number of melons from line 16 
                                        # to the global melons_sold list
        
    else:
        salespeople.append(salesperson) # add the salesperson from the line 
                                        #to the global salespeople list
        melons_sold.append(melons)  # add the melons sold from the line 
                                    # to the global melons sold list


for i in range(len(salespeople)): # make a range of the salespeople list and iterate
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # the sales report of melons per salesperson