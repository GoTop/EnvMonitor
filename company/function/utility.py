# coding=utf-8

def fake_get_or_create(model, *args, **kwargs):
    """
    解决使用Django 1.6 get_or_create() 会导致的TransactionManagementError问题
    http://stackoverflow.com/a/22875526/1314124
    """
    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:
        obj = model(**kwargs)
        obj.save()
    return obj