from ma import ma
from models.order import OrderModel


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_instance = True
        model = OrderModel
        load_only = ("dump",)
        dump_only = (
            "id",
            "status",
        )
