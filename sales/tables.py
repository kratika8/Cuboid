from .models import Cars
from table import Table
from table.columns import Column


class CarTable(Table):
    sales_id = Column(field='sales_id')
    pub_date = Column(field='pub_date')
    Customer_id = Column(field='Customer_id')
    Fuel = Column(field='Fuel')
    VEHICLE_SEGMENT = Column(field='VEHICLE_SEGMENT')
    SellingPrice=Column(field='SellingPrice')
    Power_steering=Column(field='Power_steering')
    airbags=Column(field='airbags')
    sunroof=Column(field='sunroof')
    Matt_finish=Column(field='Matt_finish')
    music_system=Column(field='music_system')
    Customer_Gender=Column(field='Customer_Gender')
    Customer_Incomegroup=Column(field='Customer_Incomegroup')
    Customer_Region=Column(field='Customer_Region')
    Customer_Marital_status=Column(field='Customer_Marital_status')

    class Meta:
        model = Cars