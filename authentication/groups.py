def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_user = Permission.objects.get(codename='add_user')
    change_user = Permission.objects.get(codename='change_user')
    delete_user = Permission.objects.get(codename='delete_user')
    view_user = Permission.objects.get(codename='view_user')

    add_client = Permission.objects.get(codename='add_client')
    change_client = Permission.objects.get(codename='change_client')
    delete_client = Permission.objects.get(codename='delete_client')
    view_client = Permission.objects.get(codename='view_client')

    add_contract = Permission.objects.get(codename='add_contract')
    change_contract = Permission.objects.get(codename='change_contract')
    delete_contract = Permission.objects.get(codename='delete_contract')
    view_contract = Permission.objects.get(codename='view_contract')

    add_event = Permission.objects.get(codename='add_event')
    change_event = Permission.objects.get(codename='change_event')
    delete_event = Permission.objects.get(codename='delete_event')
    view_event = Permission.objects.get(codename='view_event')

    add_status = Permission.objects.get(codename='add_status')
    change_status = Permission.objects.get(codename='change_status')
    delete_status = Permission.objects.get(codename='delete_status')
    view_status = Permission.objects.get(codename='view_status')

    management_permissions = [
        add_client, change_client, delete_client, view_client,
        add_contract, change_contract, delete_contract, view_contract,
        add_event, change_event, delete_event, view_event,
        add_user, change_user, delete_user, view_user,
        add_status, change_status, delete_status, view_status,
    ]

    management = Group(name='MANAGEMENT')
    management.save()

    management.permissions.set(management_permissions)

    sales_permissions = [
        add_client, change_client, delete_client, view_client,
        add_contract, change_contract, delete_contract, view_contract,
        add_event, change_event, delete_event, view_event,
    ]
    sales = Group(name='SALES')
    sales.save()
    sales.permissions.set(sales_permissions)

    support_permissions = [
        view_client, view_contract, change_event, view_event,
    ]
    support = Group(name='SUPPORT')
    support.save()
    support.permissions.set(support_permissions)

    for user in User.objects.all():
        if user.team == 'MANAGEMENT':
            management.user_set.add(user)
        if user.team == 'SALES':
            sales.user_set.add(user)
        if user.team == 'SUPPORT':
            support.user_set.add(user)
