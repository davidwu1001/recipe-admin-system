from flask import url_for, abort, redirect, request
from flask_admin import Admin, expose
from model import UserModel, OrderModel, RecipeModel, IngredientModel, User_IngredientModel, AdminModel, RoleModel, \
    roles_users
from exts import db, security
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

# 创建Admin实例，等待与app绑定
admin = Admin(name='食铺记后台管理系统', template_mode='bootstrap3')


class RecipeView(ModelView):

    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin')  or current_user.has_role('Analyst') or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    column_labels = {
        'name': '菜谱名',
        'picture': '图片',
        'category': '分类',
        'process': '工艺',
        'text': '说明',
        'time_consuming': '耗时',
    }
    column_formatters = {
        'user_id': lambda v, c, m, p: m.create_user.nickName if m.create_user else None,
        "text": lambda v, c, m, p: m.text[:20] + '...' if len(m.text) > 20 else m.text,
        "picture": lambda v, c, m, p: m.picture[:20] + '...' if len(m.picture) > 20 else m.picture
    }
    # create_modal = True
    # edit_modal = True
    can_view_details = True
    form_columns = ["name", "picture", "category", "process", "text", "time_consuming"]  # 在表单中显示的字段
    column_list = ["name", "picture", "category", "process", "text", "time_consuming"]  # todo 啥意思
    column_display_pk = True  # 在列表中显示外键字段的主键值



class IngredientView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin')  or current_user.has_role('Analyst') or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    column_labels = {
        'name': '名称',
        'category': '分类',
        'subcategory': '子分类'
    }
    form_columns = ["name", "category", "subcategory"]  # 在表单中显示的字段
    column_list = ["name", "category", "subcategory"]
    column_display_pk = True  # 在列表中显示外键字段的主键值

class AdminView(ModelView):
    can_view_details = True
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role(
            'SuperAdmin'))
    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    column_labels = {
        "email": "邮箱",
        "roles": "角色",
        'fs_uniquifier':'标识',
        'active':'活跃状态',
        'confirmed_at':'确认',
        'password':'密码'
    }
    column_formatters = {
        'roles': lambda v, c, m, p: [role.name for role in m.roles]
    }
    form_columns = ["email","password", "roles",'fs_uniquifier','active','confirmed_at']  # 在表单中显示的字段
    column_list = ["email","password","roles",'fs_uniquifier','active','confirmed_at']  #

    column_display_pk = True  # 在列表中显示外键字段的主键值

class UserView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin')  or current_user.has_role('Analyst') or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    can_view_details = True
    column_labels = {
        'nickName': '昵称',
        'avatarUrl': '头像',
        'openid': 'openid',
        'orders': '订单',
    }
    column_formatters = {
        "orders": lambda v, c, m, p: [order.id for order in m.orders],
    }
    form_columns = ['id', 'nickName', "openid", "avatarUrl", "orders"]  # 在表单中显示的字段
    column_list = ['id', 'nickName', 'openid', 'avatarUrl', "orders"]
    column_display_pk = True  # 在列表中显示外键字段的主键值


class RoleView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin') or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    can_view_details = False

    column_labels = {
        'name': '名称',
        'description': '描述',
    }
    form_columns = ['name', 'description']
    column_list = ['name', 'description']
    column_display_pk = True  # 在列表中显示外键字段的主键值


class OrderView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin')  or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    column_labels = {
        'date_created': '创建日期',
        'ingredients': '订单项',
        'user_id': '创建用户',
        'address': "送货地址",
    }
    column_formatters = {
        'user_id': lambda v, c, m, p: m.create_user.nickName if m.create_user else None,
        'ingredients': lambda v, c, m, p: [ingredient.name for ingredient in m.ingredients],
    }
    column_list = ['id', 'date_created', 'user_id', 'ingredients','address']
    form_columns = ['date_created', 'user_id', 'ingredients','address']


class InteractionView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated and current_user.has_role('Admin') or current_user.has_role('Analyst') or current_user.has_role('SuperAdmin'))

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    column_labels = {
        'user_id': '用户',
        'ingredient_id': "食材",
        'view_count': "浏览次数",
        'collect_count': "收藏次数",
        'purchase_count': '下单次数'
    }
    column_formatters = {
        'user_id': lambda v, c, m, p: m.user.nickName if m.user else None,
        'ingredient_id': lambda v, c, m, p: m.ingredient.name if m.ingredient else None
    }
    column_list = ['id', 'user_id', 'ingredient_id', 'view_count', 'collect_count', 'purchase_count', ]
    form_columns = ['view_count', 'collect_count', 'purchase_count', 'user_id', 'ingredient_id']


admin.add_view(RecipeView(RecipeModel, db.session, name="食谱", url='/admin/recipe'))
admin.add_view(IngredientView(IngredientModel, db.session, name="食材", url='/admin/ingredient'))
admin.add_view(UserView(UserModel, db.session, name="用户", url='/admin/user'))
admin.add_view(OrderView(OrderModel, db.session, name="订单", url='/admin/order'))
admin.add_view(InteractionView(User_IngredientModel, db.session, name="交互信息", url='/admin/interaction'))
admin.add_view(AdminView(AdminModel, db.session, name="管理员", url='/admin/admin'))
admin.add_view(RoleView(RoleModel, db.session, name="角色", url='/admin/role'))
