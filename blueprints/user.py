from flask import Blueprint
from model import UserModel
from exts import session,db
import json
bp = Blueprint("user",__name__,url_prefix="/user")

@bp.route('/insert')
def insert():
    # 检查数据库是否连接成功
    try:
        user = UserModel(id="123", nickName="saf", avatarUrl="saf", openid="123")
        session.add(user)
        session.commit()
    except Exception as e:
        print('数据库连接失败：', e)
    else:
        print('')

    return 'insert成功'
@bp.route('/query')
def query():
    # 检查数据库是否连接成功
    try:
        stmt = db.select(UserModel).order_by(UserModel.id.desc())
        users = session.execute(stmt).scalars()
        for item in users:
            print(item)
        return json.dumps(users)
    except Exception as e:
        print('数据库连接失败：', e)
    else:
        print('')


@bp.route('/delete')
def delete():
    # 检查数据库是否连接成功
    try:
        stmt = db.select(UserModel).filter_by(id='123')
        user = session.execute(stmt).scalar_one()
        session.delete(user)
        session.commit()
    except Exception as e:
        print('数据库连接失败：', e)
    else:
        print('')

    return 'delete成功'
@bp.route('/update')
def update():
    # 检查数据库是否连接成功
    try:
        stmt = db.select(UserModel).where(UserModel.id == 123)
        user = session.execute(stmt).scalar_one()
        user.nickName = "张三"
        session.commit()

    except Exception as e:
        print('数据库连接失败：', e)
    else:
        print('')

    return '修改成功'
