from flask import Blueprint,request
from model import OrderModel
from exts import session
bp = Blueprint("order",__name__,url_prefix='/order')

@bp.route("/insert",methods=['POST'])
def addOrder():
    """
    添加订单
    :return:
    """
    args = request.json
    order = OrderModel(**args)
    try:
        session.add(order)
        session.commit()
        return {"code": 10000, "msg": "订单插入成功", "data": {}}
    except Exception as e:
        print(e)
        return {"code": 10001, "msg": "订单插入失败"+e, "data": {}}


@bp.route("/delete")
def deleteOrder():
    return "删除订单"

@bp.route("/update")
def updateOrder():
    return "修改订单"

@bp.route("/select")
def selectOrder():
    return "选择订单"

