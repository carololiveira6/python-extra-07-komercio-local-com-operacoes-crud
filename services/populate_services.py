from database import DATABASE_PATH
import csv, os
from os.path import exists

import database

FIELDNAMES = ["id", "name", "price"]

class ProductService():

    @staticmethod
    def list_all_products(DATABASE_PATH):

        with open(DATABASE_PATH) as file:
            reader = csv.DictReader(file)

            return list(reader)
    
    @staticmethod
    def get_last_id(DATABASE_PATH):
        id_list = []

        with open(DATABASE_PATH, 'r') as file:
            reader = csv.DictReader(file)

            for product in reader:
                id_list.append(int(product['id']))

            if id_list != []:
                my_last_id = sorted(id_list)[-1] + 1
            else:
                my_last_id = 1

            return my_last_id

    @staticmethod
    def create(DATABASE_PATH, **kwargs): 
    
        if not exists(DATABASE_PATH) or os.stat(DATABASE_PATH).st_size == 0:

            with open(DATABASE_PATH, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

                writer.writeheader()
        
        my_id = ProductService.get_last_id(DATABASE_PATH)

        with open(DATABASE_PATH, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            kwargs['id'] = my_id

            if file.tell() == 0:
                writer.writeheader()

            if ProductService.verify_product(DATABASE_PATH, **kwargs):
                
                return ('', 422)
            
            writer.writerow(kwargs)

        return (kwargs, 201)

    @staticmethod
    def verify_product(DATABASE_PATH, **kwargs):

    csv_products = ProductService.list_all_products(DATABASE_PATH)

    for product in csv_products:

        if product['name'].lower() == kwargs['name'].lower():

            return True
    return False