from accounts.models import Account


def save_profile(backend, user, response, *args, **kwargs):
    if not backend.name == 'facebook':
        return # No support for non-facebook for now

    account, _ = Account.objects.get_or_create(
        social_auth_method=backend.name,
        social_id=kwargs.get('uid'))
    account.access_token = response.get('access_token')
    account.username = user.username
    account.gender = response.get('gender')
    account.first_name = user.first_name
    account.last_name = user.last_name
    account.email = kwargs.get('details').get('email')
    # TODO: Get profile picture
    account.save()