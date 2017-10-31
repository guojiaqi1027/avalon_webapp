from src.dao.mongo_dao import group_dao

class Group:
    def __init__(self, group):
        self.group = group
    
    @property
    def group_id(self):
        return self.group['id']

    @property
    def group_name(self):
        return self.group['name']

    @property
    def group_members(self):
        return self.group['members']
    
    def add_member(self, player_name):
        if player_name in self.group['members']:
            res = {
                'succes': 0,
                'msg': '{} 已经在组织中'.format(player_name)
            }
            return res
        self.group['members'].append(player_name)
        self.save_group()
        res = {
            'success': 1
        }
        return res
    def save_group(self):
        filter = {
            'id': self.group['id']
        }
        group_dao.update_single_doc(filter, self.group, upsert=True)
