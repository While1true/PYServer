from myFirstPYServer.settings import ALLOWED_HOSTS
CURRENT_HOST='http://'+ALLOWED_HOSTS[0]+':8090/masterWeiBo/static/'
WORDPRESS_HOST=CURRENT_HOST+'pic/'
UPLOAD_IMG_HOST=CURRENT_HOST+"media/"