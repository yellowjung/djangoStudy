def obj_to_post(obj):
    """obj의 각 속성을 serialize 해서, dict 로 변환한다

    Args:
        obj (_type_): _description_
    """
    
    post = dict(vars(obj))
    
    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'
    
    if obj.tags:
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []
    
    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = 'https://via.placeholder.com/900x400/'
        
    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%s')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'
    
    del post['_state'], post['category'], post['create_dt']
    
    return post