
def gets( t, s, d=None ):
    '''
        拓展字典的get方法
        gets( 字典, key [, '默认值'])
        dict = {'a':{'b':1}}
        gets( dict, 'a.b', 'xx')
        返回值 | 默认值（未指定返回None）
    '''
    if not t: return d
    for k in s.split('.'):
        if isinstance(t, list) and k.lstrip('-').isdigit():
            l = k = int(k)
            if k < 0: l = abs(k) - 1
            if len(t) > l: t = t[k]; continue
        elif isinstance(t, dict) and k in t:
            t = t[k]; continue
        return d
    return t

class mydict(dict):
    def dict2til(self, d):
        '''
            将字典平铺
        '''
        for k, v in d.items():
            if isinstance(v, (list, dict)):
                lst = v if isinstance(v, list) else [v]
                for item in lst:
                    # item = {"{}.{}".format(k, a): b for a, b in item.items()}
                    yield from self.dict2til(item)
                    for k1, v1 in self.dict2til(item):
                        yield k1, v1

            yield k, v

    def gets(self, k, d=None):
        dic = {k: v for k, v in self.dict2til(self)}
        return d if k not in dic.keys() else dic.get(k)

