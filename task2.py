def update_car_info(brand, model, year, color, price):
    car = {}
    car['brand'] = brand
    car['model'] = model
    car['year'] = year
    car['color'] = color
    car['price'] = price  
    car['is_available'] = True
    return car
car_info = update_car_info(brand='Toyota', model='Camry', year=2021, color='blue', price=300000)
print(car_info)
print(car_info)