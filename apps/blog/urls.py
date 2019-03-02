# -*- coding: utf-8 -*-
from django.conf.urls import url
# from .views import goview
from .views import (IndexView, DetailView, CategoryView, TagView, AboutView,
                    SilianView, MySearchView, ArchiveView, TimelineView,
                    SoftwareView,Software_DetailView,EbookView,Ebook_DetailView,
                    TrainView, Train_DetailView, QuestionsView, Questions_DetailView,
                    ProjectView)

urlpatterns = [
    # url(r'^go/$', goview, name='go'),  # 测试用页面

    url(r'^$', IndexView.as_view(), name='index'),  # 主页，自然排序

    url(r'^hot/$', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),  # 主页，按照浏览量排序
    url(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
    url(r'^category/(?P<slug>[\w-]+)/hot/$', CategoryView.as_view(), {'sort': 'v'},
        name='category_hot'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagView.as_view(), name='tag'),
    url(r'^tag/(?P<slug>[\w-]+)/hot/$', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),
    url(r'^about/$', AboutView.as_view(), name='about'),  # About页面
    url(r'^timeline/$', TimelineView.as_view(), name='timeline'),  # timeline页面
    url(r'archive/$', ArchiveView.as_view(), name='archive'),  # 归档页面
    url(r'^silian\.xml$', SilianView.as_view(content_type='application/xml'), name='silian'),  # 死链页面
    url(r'^search/$', MySearchView.as_view(), name='search_view'),  # 全文搜索

    url(r'^software/$',SoftwareView.as_view(),name="software"),
    url(r'^software/(?P<slug>[\w-]+)/$',Software_DetailView.as_view(),name="software_detail"),

    url(r'^ebook/$', EbookView.as_view(), name="ebook"),
    url(r'^ebook/(?P<slug>[\w-]+)/$', Ebook_DetailView.as_view(), name="ebook_detail"),

    url(r'^train/$', TrainView.as_view(), name="train"),
    url(r'^train/(?P<slug>[\w-]+)/$', Train_DetailView.as_view(), name="train_detail"),

    url(r'^questions/$', QuestionsView.as_view(), name="questions"),
    url(r'^questions/(?P<slug>[\w-]+)/$', Questions_DetailView.as_view(), name="questions_detail"),

    url(r'^project/$', ProjectView.as_view(), name="project"),
]
