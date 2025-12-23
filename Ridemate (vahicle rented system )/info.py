class vehicle:
    def __init__(self,car_id=0,car_name="",price=0,available=0):
        self.car_id=car_id
        self.car_name=car_name
        self.price=price
        self.available=available
    def __str__(self):
        return f"{self.car_id},{self.car_name},{self.price},{self.available} "
    