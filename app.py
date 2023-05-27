from flask import Flask,render_template,url_for,redirect,request

import model
from exts import db, migrate,security  # 插件
from admin import admin  # 管理系统
from blueprints import interaction, user, order
import config
from flask_security import SQLAlchemyUserDatastore,login_required,current_user,LoginForm,login_user
from context_processors import security_context_processor
# 实例化app
app = Flask(__name__)
# 导入配置
app.config.from_object(config)
app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

# db绑定app
db.init_app(app)
# migrate绑定app,db
migrate.init_app(app, db)
# 注册蓝图
app.register_blueprint(user.bp)
app.register_blueprint(order.bp)
# admin绑定app
admin.init_app(app)

# Flask-Security绑定app db 实现角色管理 权限管理
user_datastore = SQLAlchemyUserDatastore(db,model.AdminModel,model.RoleModel)
security.init_app(app,user_datastore)
# define a context processor for merging flask-admin's template context into the
# flask-security views.

# 将 security_context_processor 注册为上下文处理器
app.context_processor(security_context_processor)

# @app.route('/login',methods=['GET','POST'])
# def login():
#     print("login进来了")
#     # 实例化登录表单
#     form = LoginForm(request.form)
#
#     # 处理表单提交
#     if request.method == 'POST' and form.validate():
#         # 执行登录验证逻辑
#         user = model.UserModel.query.filter_by(email=form.email.data).first()
#
#         if user is not None and user.verify_password(form.password.data):
#             # 验证成功，将用户添加到 current_user 中
#             login_user(user)
#
#             # 登录成功后的处理
#             return redirect(url_for('admin.index'))
#
#     # 渲染登录页面
#     return render_template('login.html', form=form)
#

# security.login_view = 'login'
@app.route("/",methods=["GET"])
def index():
   print("safga")
   return redirect('/admin')
# Add administrative views here
if __name__ == "__main__":
    app.run(port=8009, debug=True)
