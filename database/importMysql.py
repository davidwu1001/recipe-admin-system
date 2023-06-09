from exts import session
from model import UserModel,RecipeModel,IngredientModel
import json
from app import app

def Insert_Recipe(recipe):
    with app.app_context():  # 在应用上下文中进行
        try:
            session.begin()
            # todo 检查用户是否存在 若不存在先创建这个用户
            # 判断该食谱是否已存在
            exist = RecipeModel.query.filter_by(name=recipe['name']).first()
            if not exist:
                print(f"插入{recipe['name']}")
                recipe['category'] = '，'.join(recipe['category'])  # 目录一开始是数组类型，转化为字符串 todo 将category单独成为一个表
                recipe['user_id'] = 124521523 # 模拟user_id
                _recipe = RecipeModel(**recipe)  # 将字典转化为类
                session.add(_recipe)
            session.commit()
        except Exception as e:
            # 回滚事务
            session.rollback()
            print("数据库出错了",e)
def Insert_Ingredient(category):
    with app.app_context():  # 在应用上下文中进行
        try:
            session.begin()
            cate = category["category"]
            for sub in category['subcategories']:
                subcate = sub['subcategory']  # 猪肉
                ingredients = sub['ingredients']
                for item in ingredients:  # name
                    # 先检查是否存在该结点,如果存在就跳过 这样能保证从断点开始，不用每次都从头开始
                    exist = IngredientModel.query.filter_by(name=item).first()
                    if not exist:  # 食材不存在
                        _ingredient = IngredientModel(name=item, category=cate, subcategory=subcate)
                        print(f"插入{_ingredient.name}")
                        session.add(_ingredient)
            session.commit()
        except Exception as e:
            # 回滚事务
            session.rollback()
            print("数据库出错了",e)
def dataWashing(recipes):
    """
    清洗数据
    :param recipes:
    :return:
    """
    old_num = len(recipes)
    for recipe in recipes:
        if not recipe['recipe']['name']:  # 清洗掉不存在的食谱
            recipes.remove(recipe)
        if len(recipe['recipe']['name']) > 10:  # 清洗名字太长的数据
            recipes.remove(recipe)
    new_num = len(recipes)
    print(f"数据清洗完成，清洗前{old_num}，清理后{new_num}，共清洗掉{old_num-new_num}条无效数据")
    return recipes

def handlerRecipe():
    # 从neo4j中查询食谱插入 保证 recipe的id一致

    for idx, recipe in enumerate(recipes):
        # print(f"插入{idx} {recipe['recipe']['name']}")

        Insert_Recipe(recipe['recipe'], recipe['ingredient'], recipe['procedure'])

def handleIngredient():
    with open("source/ingredients.json") as f:
        ingredients = json.load(f)
        for category in ingredients:
            Insert_Ingredient(category)

if __name__ == "__main__":

    # handlerRecipe()
    handleIngredient()