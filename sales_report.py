"""Generate sales report showing total melons each salesperson sold."""

# comments explaining original code marked with one hashtag #
## areas for improvement marked with two hashtags ##

## instead of global lists, could we create a sales order dictionary?
## that way, we don't have to check, append the global lists by each line of file
 
def sales_order_dict(log_file_path):
    """Return a dictionary of {salesperson_name: total_dollars, melons_sold}.
    Arguments:
        log_file_path (str) - the path to a sales report log file
    
    Return:
        melons_by_sales (dict)
    """

    melons_by_sales = {}

    with open(log_file_path) as f:
        for line in f: # begins a for loop to iterate over each line in our data
            line = line.rstrip() # removes trailing space and the line break indicators

        ## create a list of data and unpack its values
        salesperson_name, total_dollars, melons_sold = line.split('|')
        if salesperson_name in melons_by_sales:
            melons_by_sales[salesperson_name[0]] += float(total_dollars)
            melons_by_sales[salesperson_name[1]] += int(melons_sold)
        else:
                melons_by_sales[salesperson_name[0]] = float(total_dollars)
                melons_by_sales[salesperson_name[1]] = int(melons_sold)

    return melons_by_sales

def print_sales_report(sales_order_dict):
     """Print a report of salespeople, their total number of melons sold, 
        and their total sales.
    Arguments: sales_order_dict - {salesperson_name: total_dollars, melons_sold}.
     """
for sales_person_name, total_dollars, melons_sold in sales_order_dict.items():
    print(f"{sales_person_name} sold {melons_sold} melons netting {total_dollars} in sales.")

print_sales_report(sales_order_dict('sales-report.txt'))

# def get_melons_sold_by_salesperson(log_file_path):
#     """Return a dictionary of {salesperson_name: melons_sold}.

#     Arguments:
#         log_file_path (str) - the path to a sales report log file

#     Return:
#         mels_by_sales (dict)
#     """

#     mels_by_sales = {}

#     with open(log_file_path) as f:
#         for line in f:
#             line = line.rstrip()

#             # Create a list of data and unpack its values
#             salesperson_name, total_dollars, melons_sold = line.split('|')

#             # Set or increment the salesperson's total melons sold
#             if salesperson_name in mels_by_sales:
#                 mels_by_sales[salesperson_name] += int(melons_sold)
#             else:
#                 mels_by_sales[salesperson_name] = int(melons_sold)

#     return mels_by_sales


# def print_sales_report(melons_sold_by_salesperson):
#     """Print a report of salespeople and the total number of melons they've sold.

#     Arguments:
#         melons_sold_by_salesperson (dict) - {salesperson_name: melons_sold}
#     """

#     for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
#         print(f'{salesperson_name} sold {melons_sold} melons')


# print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))