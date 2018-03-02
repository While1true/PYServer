# cd C:\Users\ck\PycharmProjects\VangeServer
# python manage.py runserver 0:8080
#
# cd C:\Users\ck\PycharmProjects\VangeServer
# python manage.py makemigrations
# python manage.py migrate
#
#
# SELECT t.*,(select category from vange.vange_category where category_id=id)category_id FROM vange.vange_bug t LIMIT 0, 50000
# SELECT t.*,a.category,b.publisher FROM vange.vange_bug t left join vange.vange_category a on t.category_id= a.id left join vange.vange_publisher b on t.publisher_id=b.id LIMIT 0, 50000
