from faker import Faker
import random

fake = Faker()

email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']

states = ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds', 'Newcastle', 'Bristol', 'Sheffield', 'Nottingham', 'Southampton']

state_city = [
    {'London': ['London', 'Barking', 
                'Barnet', 'Bexley', 'Brent', 
                'Bromley', 'Camden', 'Croydon', 
                'Ealing', 'Enfield', 'Greenwich', 
                'Hackney', 'Hammersmith', 'Haringey', 
                'Harrow', 'Havering', 'Hillingdon', 
                'Hounslow', 'Islington', 'Kensington', 'Kingston', 
                'Lambeth', 'Lewisham', 'Merton', 'Newham', 'Redbridge', 
                'Richmond', 'Southwark', 'Sutton', 'Tower Hamlets', 'Waltham Forest', 
                'Wandsworth', 'Westminster']},

    {'Manchester': ['Manchester', 'Bolton', 'Bury', 'Oldham', 'Rochdale', 
                    'Salford', 'Stockport', 'Tameside', 'Trafford', 'Wigan']},

    {'Birmingham': ['Birmingham', 'Coventry', 'Dudley', 'Sandwell', 'Solihull']},

    {'Liverpool': ['Liverpool', 'Knowsley', 'St Helens', 'Sefton', 'Wirral']},

    {'Leeds': ['Leeds', 'Bradford', 'Calderdale', 'Kirklees', 'Wakefield']},

    {'Newcastle': ['Newcastle', 'Gateshead', 'North Tyneside', 'South Tyneside', 'Sunderland']},

    {'Bristol': ['Bristol', 'Bath', 'North East Somerset', 'South Gloucestershire']},

    {'Sheffield': ['Sheffield', 'Barnsley', 'Doncaster', 'Rotherham']},

    {'Nottingham': ['Nottingham', 'Ashfield', 'Bassetlaw', 'Broxtowe', 'Gedling',
                    
                    'Mansfield', 'Newark', 'Sherwood', 'Rushcliffe']},

    {'Southampton': ['Southampton', 'Eastleigh', 'Fareham', 'Gosport', 'Havant', 'New Forest', 'Test Valley', 'Winchester']}

]

product_categories = {
    'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Printer', 'Monitor', 'Keyboard', 'Mouse'],
    'Clothing': ['T-shirt', 'Jeans', 'Dress', 'Shoes', 'Socks', 'Hat', 'Jacket', 'Sweater', 'Skirt', 'Shorts'],
    'Books': ['Fiction', 'Non-Fiction', 'Children', 'Young Adult', 'Mystery', 'Thriller', 'Romance', 'Science Fiction', 'Fantasy', 'Biography'],
    'Home': ['Sofa', 'Bed', 'Table', 'Chair', 'Desk', 'Dresser', 'Bookshelf', 'TV Stand', 'Nightstand', 'Couch'],
    'Garden': ['Lawn Mower', 'Grill', 'Patio Furniture', 'Garden Tools', 'Plants', 'Pots', 'Garden Hose', 'Sprinkler', 'Outdoor Lights', 'Outdoor Decor'],
    'Beauty': ['Shampoo', 'Conditioner', 'Body Wash', 'Lotion', 'Sunscreen', 'Deodorant', 'Perfume', 'Makeup', 'Nail Polish', 'Hair Dye'],
    'Health': ['Vitamins', 'Supplements', 'Protein Powder', 'Medicine', 'First Aid Kit', 'Thermometer', 'Blood Pressure Monitor', 'Pain Reliever', 'Cold Medicine', 'Allergy Medicine'],
    'Toys': ['Action Figures', 'Dolls', 'Board Games', 'Puzzles', 'Stuffed Animals', 'Building Blocks', 'Toy Cars', 'Dress Up', 'Outdoor Toys', 'Educational Toys'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Resistance Bands', 'Jump Rope', 'Exercise Ball', 'Kettlebell', 'Foam Roller', 'Treadmill', 'Exercise Bike', 'Elliptical'],
    'Outdoors': ['Tent', 'Sleeping Bag', 'Backpack', 'Cooler', 'Lantern', 'Hiking Boots', 'Water Bottle', 'Compass', 'Bug Spray', 'Sunscreen'],
    'Grocery': ['Milk', 'Yogurt', 'Juice', 'Bread', 'Eggs', 'Cheese', 'Butter', 'Cereal', 'Coffee', 'Tea'],
    'Movies': ['The Avengers', 'The Dark Knight', 'Star Wars', 'Jurassic Park', 'Harry Potter', 'The Lion King', 'The Incredibles', 'Toy Story', 'Finding Nemo', 'Frozen'],
    'Music': ['The Beatles', 'Elvis Presley', 'Michael Jackson', 'Madonna', 'Prince', 'Whitney Houston', 'Queen', 'Bob Marley', 'David Bowie', 'Led Zeppelin'],
    'Games': ['The Legend of Zelda', 'Super Mario Bros', 'Minecraft', 'World of Warcraft', 'Fortnite', 'Call of Duty', 'Grand Theft Auto', 'Overwatch', 'League of Legends', 'Pokemon'],
    'Tools': ['Hammer', 'Screwdriver', 'Drill', 'Saw', 'Wrench', 'Pliers', 'Tape Measure', 'Level', 'Utility Knife', 'Flashlight'],
    'Pet Supplies': ['Dog Food', 'Cat Food', 'Dog Toys', 'Cat Toys', 'Leash', 'Collar', 'Bed', 'Crate', 'Litter Box', 'Scratching Post'],
    'Jewelry': ['Necklace', 'Earrings', 'Bracelet', 'Ring', 'Watch', 'Brooch', 'Anklet', 'Pendant', 'Charm', 'Cufflinks']
}

companies = {
    'Electronics': ['Apple', 'Samsung', 'Dell', 'HP', 'Sony', 'Microsoft', 'Lenovo', 'Asus', 'Acer', 'Toshiba'],
    'Clothing': ['Nike', 'Adidas', 'Levi\'s', 'H&M', 'Zara', 'Gap', 'Uniqlo', 'Forever 21', 'American Eagle', 'Old Navy'],
    'Books': ['Penguin Random House', 'HarperCollins', 'Simon & Schuster', 
              'Hachette Livre', 'Macmillan Publishers', 'Scholastic', 'Pearson', 'Oxford University Press', 'Wiley', 'Bloomsbury'],
    'Home': ['IKEA', 'Wayfair', 'Ashley Furniture', 'Rooms', 'Crate & Barrel', 'Pier 1', 'West Elm', 'Pottery Barn', 'Ethan Allen', 'Havertys'],
    'Garden': ['Home Depot', 'Lowe\'s', 'Walmart', 'Target', 'Ace Hardware', 'Menards', 'True Value', 'Orchard Supply Hardware', 'Do it Best', 'Sears'],
    'Beauty': ['L\'Oréal', 'Estée Lauder', 'Procter & Gamble', 'Unilever', 'Shiseido', 'Coty', 'Johnson & Johnson', 'Revlon', 'Kao', 'Beiersdorf'],
    'Health': ['Johnson & Johnson', 'Pfizer', 'Roche', 'Novartis', 'Merck', 'GlaxoSmithKline', 'Sanofi', 'AbbVie', 'Amgen', 'Bayer'],
    'Toys': ['Mattel', 'Hasbro', 'LEGO', 'Bandai Namco', 'Spin Master', 'MGA Entertainment', 'Jazwares', 'Funko', 'Playmates Toys', 'WowWee'],
    'Sports': ['Nike', 'Adidas', 'Under Armour', 'Puma', 'Reebok', 'New Balance', 'Asics', 'Fila', 'Skechers', 'Converse'],
    'Outdoors': ['REI', 'Cabela\'s', 'Bass Pro Shops', 'Dick\'s Sporting Goods', 'Academy Sports + Outdoors', 'Gander Outdoors', 'Field & Stream', 'Big 5 Sporting Goods', 'Sportsman\'s Warehouse', 'Orvis'],
    'Grocery': ['Walmart', 'Kroger', 'Costco', 'Albertsons', 'Aldi', 'Publix', 'Target', 'H-E-B', 'Meijer', 'Whole Foods'],
    'Movies': ['Disney', 'Warner Bros', 'Universal Pictures', 'Paramount Pictures', '20th Century Fox', 'Columbia Pictures', 'Sony Pictures', 'Lionsgate', 'MGM', 'DreamWorks'],
    'Music': ['Universal Music Group', 'Sony Music Entertainment', 'Warner Music Group', 'EMI', 'BMG', 'Capitol Records', 'Columbia Records', 'Atlantic Records', 'RCA Records', 'Island Records'],
    'Games': ['Nintendo', 'Sony', 'Microsoft', 'Activision', 'Electronic Arts', 'Ubisoft', 'Blizzard Entertainment', 'Square Enix', 'Take-Two Interactive', 'Sega'],
    'Tools': ['Home Depot', 'Lowe\'s', 'Ace Hardware', 'Menards', 'True Value', 'Orchard Supply Hardware', 'Do it Best', 'Sears', 'Harbor Freight Tools', 'Northern Tool + Equipment'],
    'Pet Supplies': ['PetSmart', 'Petco', 'Chewy', 'Pet Supplies Plus', 'Pet Valu', 'Pet Supermarket', 'Petland', 'Petland Discounts', 'PetSense', 'Pet People'],
    'Jewelry': ['Tiffany & Co.', 'Cartier', 'Harry Winston', 'Bulgari', 'Van Cleef & Arpels', 'Chopard', 'Piaget', 'Graff', 'David Yurman', 'Mikimoto']
}

supplying_countries_cities = {
    'United Kingdom': ['London', 'Manchester', 'Birmingham', 'Liverpool'],
    'United States': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Canada': ['Toronto', 'Montreal', 'Vancouver', 'Calgary'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse'],
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin'],
    'Spain': ['Madrid', 'Barcelona', 'Valencia', 'Seville'],
    'Japan': ['Tokyo', 'Yokohama', 'Osaka', 'Nagoya'],
    'China': ['Shanghai', 'Beijing', 'Guangzhou', 'Shenzhen']
}

categories = list(product_categories.keys())

def generate_customers(num_customers=10000):
    customers = []
    for _ in range(num_customers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f'{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}'
        phone = f'+44{random.randint(7000000000, 7999999999)}'
        state = random.choice(states)
        city = random.choice(state_city[states.index(state)][state])
        address = f'{random.randint(1, 100)} {fake.street_name()}, {fake.street_suffix()}'
        country = 'United Kingdom'
        zipcode = f'{random.randint(10, 99)}{random.randint(1, 9)} {random.choice(["1AB", "2CD", "3EF", "4GH", "5IJ", "6KL", "7MN", "8OP", "9QR"])}'
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=75).strftime('%Y-%m-%d')
        customer_type = random.choice(['Premium', 'Regular'])
        
        customers.append(
            f"('{first_name}', '{last_name}', '{email}', '{phone}', '{address}', '{city}', '{state}', '{country}', '{zipcode}', '{date_of_birth}', '{customer_type}')"
        )

    return customers

# Function to generate SQL insert for sales
def generate_sales(num_sales=20000, num_customers=10000, num_stores=10):
    sales = []
    for _ in range(num_sales):
        customer_id = random.randint(1, num_customers)
        sale_date = fake.date_between(start_date='-2y', end_date='today').strftime("%Y-%m-%d")
        store_id = random.randint(1, num_stores)
        total_amount = round(random.uniform(20.00, 500.00), 2)
        discount_amount = round(random.uniform(0.00, 50.00), 2)
        payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash'])

        
        
        sales.append(
            f"({customer_id}, '{sale_date}', {store_id}, {total_amount}, {discount_amount}, '{payment_method}')"
        )
    
    return sales

# Function to generate SQL insert for categories
def generate_categories():
    p_categories = []
    for category in categories:
        category_id = categories.index(category) + 1
        category_name = category
        description = f"Products in the {category_name.lower()} category"
        p_categories.append(f"({category_id}, '{category_name}', '{description}')")

    return p_categories

# Products should be generate from the product_categories. Each product under become a product
def generate_products():
    products = []
    for category, sub_categories in product_categories.items():
        for product in sub_categories:
            product_name = product
            category_id = categories.index(category) + 1
            brand = random.choice(companies[category])
            price = round(random.uniform(10.00, 500.00), 2)
            cost_price = round(price * random.uniform(0.5, 0.8), 2)
            quantity_in_stock = random.randint(0, 100)
            supplier_id = random.randint(1, 50)

            products.append(
                f"('{product_name}', {category_id}, '{brand}', {price}, {cost_price}, {quantity_in_stock}, {supplier_id})"
        )

    return products

# Function to generate SQL insert for suppliers
def generate_suppliers(num_suppliers=50):
    suppliers = []
    for supplier_id in range(1, num_suppliers + 1):
        supplier_name = random.choice(companies[random.choice(categories)])
        contact_person = fake.name()
        email = f"{supplier_name.lower().replace(' ', '_')}@{random.choice(email_domains)}"
        address = fake.address().replace("\n", ", ")
        country = random.choice(list(supplying_countries_cities.keys()))
        city = random.choice(supplying_countries_cities[country])
        state = random.choice(supplying_countries_cities[country])

        # Zip code should be generated based on the country
        if country == 'United Kingdom':
            zip_code = f'{random.randint(10, 99)}{random.randint(1, 9)} {random.choice(["1AB", "2CD", "3EF", "4GH", "5IJ", "6KL", "7MN", "8OP", "9QR"])}'
        else:
            zip_code = fake.zipcode()

        # Phone number should be generated based on the country
        if country == 'United Kingdom':
            phone = f'+44{random.randint(7000000000, 7999999999)}'

        if country == 'United States' or country == 'Canada':
            phone = f'+1{random.randint(2000000000, 9999999999)}'

        if country == 'Australia':
            phone = f'+61{random.randint(200000000, 999999999)}'

        if country == 'Germany':
            phone = f'+49{random.randint(200000000, 999999999)}'

        if country == 'France':
            phone = f'+33{random.randint(200000000, 999999999)}'
        
        if country == 'Italy':
            phone = f'+39{random.randint(200000000, 999999999)}'
        
        if country == 'Spain':
            phone = f'+34{random.randint(200000000, 999999999)}'

        if country == 'Japan':
            phone = f'+81{random.randint(200000000, 999999999)}'

        if country == 'China':
            phone = f'+86{random.randint(200000000, 999999999)}'


        suppliers.append(
            f"('{supplier_name}', '{contact_person}', '{phone}', '{email}', '{address}', '{city}', '{state}', '{country}', '{zip_code}')"
        )

    return suppliers

# Function to generate SQL insert for stores
def generate_stores(num_stores=10):
    stores = []
    for store_id in range(1, num_stores + 1):
        address = fake.address().replace("\n", ", ")
        city = random.choice(states)
        state = random.choice(state_city[states.index(city)][city])
        country = 'United Kingdom'
        store_name = f"ShopEase {city} Store"
        zip_code = f'{random.randint(10, 99)}{random.randint(1, 9)} {random.choice(["1AB", "2CD", "3EF", "4GH", "5IJ", "6KL", "7MN", "8OP", "9QR"])}'
        phone = f'+44{random.randint(7000000000, 7999999999)}'
        
        stores.append(f"('{store_name}', '{address}', '{city}', '{state}', '{country}', '{zip_code}', '{phone}')")
    return stores


# Function to generate SQL insert for inventory
def generate_inventory(num_inventory=1000, num_stores=10, num_products=170):
    inventory = []
    for inventory_id in range(1, num_inventory + 1):
        product_id = random.randint(1, num_products)
        store_id = random.randint(1, num_stores)
        quantity_available = random.randint(0, 10000)
        reorder_level = random.randint(10, 50)
        last_restocked_date = fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")
        
        inventory.append(f"({product_id}, {store_id}, {quantity_available}, {reorder_level}, '{last_restocked_date}')")
    return inventory

# Function to generate SQL insert for sales items
def generate_sales_items(num_sales_items=30000, num_sales=20000, num_products=170):
    sales_items = []
    for sale_item_id in range(1, num_sales_items + 1):
        sale_id = random.randint(1, num_sales)
        product_id = random.randint(1, num_products)
        quantity = random.randint(1, 10)
        price_at_sale = round(random.uniform(10.00, 500.00), 2)
        total_line_amount = round(price_at_sale * quantity, 2)
        
        sales_items.append(f"({sale_id}, {product_id}, {quantity}, {price_at_sale}, {total_line_amount})")
    return sales_items

# Function to generate SQL insert for payments
def generate_payments(num_payments=20000, num_sales=20000):
    payments = []
    for payment_id in range(1, num_payments + 1):
        sale_id = random.randint(1, num_sales)
        payment_date = fake.date_between(start_date='-2y', end_date='today').strftime("%Y-%m-%d")
        payment_amount = round(random.uniform(20.00, 1000.00), 2)
        payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash'])
        
        payments.append(f"({sale_id}, '{payment_date}', {payment_amount}, '{payment_method}')")
    return payments


# Generate and save SQL commands to insert data
def save_data_to_file():

    # Customers
    customers = generate_customers()
    with open('customers.sql', 'w') as file:
        file.write("""INSERT INTO customers (first_name, last_name, email, phone, address, 
                   city, state, country, zip_code, date_of_birth, customer_type) VALUES\n""")
        file.write(",\n".join(customers) + ";\n")
    
    
    # Sales
    sales = generate_sales()
    with open('sales.sql', 'w') as file:
        file.write("INSERT INTO sales (customer_id, sale_date, store_id, total_amount, discount_amount, payment_method) VALUES\n")
        file.write(",\n".join(sales) + ";\n")

    # Categories
    categories = generate_categories()
    with open('categories.sql', 'w') as file:
        file.write("INSERT INTO categories (category_id, category_name, description) VALUES\n")
        file.write(",\n".join(categories) + ";\n")
    
    # Suppliers
    suppliers = generate_suppliers()
    with open('suppliers.sql', 'w') as file:
        file.write("INSERT INTO suppliers (supplier_name, contact_person, phone, email, address, city, state, country, zip_code) VALUES\n")
        file.write(",\n".join(suppliers) + ";\n")
    
    # Products
    products = generate_products()
    with open('products.sql', 'w') as file:
        file.write("INSERT INTO products (product_name, categoryI_id, brand, price, cost_price, quantity_in_Stock, supplier_id) VALUES\n")
        file.write(",\n".join(products) + ";\n")
    
    # Stores
    stores = generate_stores()
    with open('stores.sql', 'w') as file:
        file.write("INSERT INTO stores (store_name, address, city, state, country, zip_code, phone) VALUES\n")
        file.write(",\n".join(stores) + ";\n")
    
    # Inventory
    inventory = generate_inventory()
    with open('inventory.sql', 'w') as file:
        file.write("INSERT INTO inventory (product_id, store_id, quantity_available, reorder_level, last_restocked_date) VALUES\n")
        file.write(",\n".join(inventory) + ";\n")
    
    # Sales Items
    sales_items = generate_sales_items()
    with open('sales_items.sql', 'w') as file:
        file.write("INSERT INTO SalesItems (product_id, quantity, price_at_sale, total_line_amount) VALUES\n")
        file.write(",\n".join(sales_items) + ";\n")
    
    # Payments
    payments = generate_payments()
    with open('payments.sql', 'w') as file:
        file.write("INSERT INTO payments (sale_id, payment_date, payment_amount, payment_method) VALUES\n")
        file.write(",\n".join(payments) + ";\n")


save_data_to_file()