# -*- coding: utf-8 -*-

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!kta!9e0)24d@9#<*=ra$r!0k0+p8@w+a%7g1bbof0+ad@4_('

# 自由选择需要开启的功能
# 是否开始[在线工具]应用
TOOL_FLAG = True
# 是否开启[API]应用
API_FLAG = True
# DEBUG模式是否开始的选择
# 值为0：所有平台关闭DEBUG,值为1:所有平台开启DEBUG,值为其他：根据平台类型判断开启（默认设置的Windows下才开启）
MY_DEBUG = 2

# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'izone',       # 数据库的名称
        'USER': 'root',        # 数据库的用户名
        'PASSWORD': '123456',  # 数据库的密码
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}
# 邮箱配置
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'your-email@163.com'
EMAIL_HOST_PASSWORD = 'your-password'  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = 465  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
DEFAULT_FROM_EMAIL = 'your-webname <your-email@163.com>'

# 网站默认设置和上下文信息
SITE_END_TITLE = '网站的名称，如TendCode'
SITE_DESCRIPTION = '网站描述'
SITE_KEYWORDS = '网站关键词，多个词用英文逗号隔开'
