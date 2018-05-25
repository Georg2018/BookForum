from django import template
from django.db.models.aggregates import Count

from ..models import Discuss

register = template.Library()


@register.simple_tag()
def get_discussions_number(book_object):
    """
    获得本书讨论的数量。

    :param book_object: Book模型实例
    :return: 本书讨论数量
    """
    return book_object.discussions.count()


@register.simple_tag()
def get_discussions(book_object):
    """
    获得本书所有的讨论

    :param book_object: Book模型实例
    :return: 本书所有讨论的列表
    """
    return book_object.discussions.all()


@register.simple_tag()
def get_replys_number(discussion_object):
    return discussion_object.replys.count()


@register.simple_tag()
def get_discussion_replys(discussion, sort="-pub_date", num=1):
    num = int(num)
    replys = discussion.replys.order_by(sort)[:num]
    return replys


@register.simple_tag()
def get_hot_discussions(num=5):
    """
    得到指定数量的热门讨论

    :param num: 想要得到的讨论数量
    :return: Discuss模型的实例列表
    """
    discussions = Discuss.objects.annotate(reply_num=Count('replys')).all()
    discussions = sorted(discussions, key=lambda x: x.reply_num)
    return discussions[:num]


@register.inclusion_tag('tag/show_discussions.html')
def show_discussions(discussions_list):
    """
    加载指定讨论列表的模板

    :param dicussions_list: 将要展现的讨论列表
    :return: 返回一个字典作为模板的上下文
    """
    context = {
        'discussions_list': discussions_list,
    }
    return context


@register.inclusion_tag('tag/show_book_detail.html')
def show_book_detail(book_object):
    """
    作为一个左边栏，展示书籍的详细信息

    :param book_object: Book模型的实例
    :return: 返回一个字典作为模板的上下文
    """
    context = {
        "book": book_object,
    }
    return context