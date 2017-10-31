from src.dao.mongo_dao import seq_dao, group_dao
from basic_db import vending_id
from src.model.group import Group

def create_group(name, members):
    filter = {
        'name': name
    }
    count = group_dao.count_docs(filter)
    if count > 0:
        res = {
            'success': 0,
            'msg': "组织已存在"
        }
        return res
    else:
        id = vending_id("group")
        doc = {
            'id': id,
            'name': name,
            'members': members
        }
        group_dao.insert_single_doc(doc)
        res = {
            'success': 1
        }
        return res


def get_group_orm_by_name(name):
    filter = {
        'name': name
    }
    return get_group_orm_by_filter(filter)


def get_group_orm_by_id(id):
    filter = {
        'id': id
    }
    return get_group_orm_by_filter(filter)


def get_group_orm_by_filter(filter):
    doc = group_dao.fetch_single_doc(filter)
    if doc:
        return Group(doc)
    else:
        return None


def add_player_to_group(player_name, group_id):
    group = get_group_orm_by_id(group_id)
    res = group.add_member(player_name)
    return res

