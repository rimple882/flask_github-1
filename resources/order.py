from collections import Counter
from flask_restful import Resource, request
from models.item import ItemModel

from models.order import OrderModel, ItemInOrder
from schemas.order import OrderSchema

order_schema = OrderSchema()


class Order(Resource):
    def post(self):
        data = request.get_json()
        items = []
        item_id_quantities = Counter(data["item_ids"])

        for _id, count in item_id_quantities.most_common():
            item = ItemModel.find_by_id(_id)
            if not item:
                return {"message": "item not found"}, 404
            items.append(ItemInOrder(item_id=_id, quantity=count))
        order = OrderModel(items=items, status="pending")
        order.save_to_db()
        order.set_status("failed")
        # order.charge_with_Stripe(data["token"])
        order.set_status("complete")
        return order_schema.dump(order)
