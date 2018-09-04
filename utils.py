import urlparse
import requests

from django.conf import settings


def check_angel_company_type(company_id, access_token, company_type):
    check = (
        (lambda x: x.get('id') in (92334, 142922))
        if company_type == 'accelerator' else
        (lambda x: x.get('id') == 94212)
    )
    url = urlparse.urljoin(
        settings.ANGEL_API_URL, 'startups/{}'.format(company_id))
    resp = requests.get(url, params={'access_token': access_token})
    company_types = resp.json().get('company_type', {})
    if isinstance(company_types, list):
        return any(map(check, company_types))
    return check(company_types)


def find_matching_angel_company(user_id, company_id, access_token, role=None):
    if role:
        assert role in ['founder', 'employee', 'any']

    def get_company(company_id, data):
        possible_matches = map(lambda x: x['startup'], data)
        accelerator = filter(
            lambda x: x['id'] == company_id, possible_matches)
        if accelerator:
            return accelerator[0]
        return None

    company = None
    if role in ['founder', 'any']:
        url = urlparse.urljoin(settings.ANGEL_API_URL, 'startup_roles')
        url_params = {
            'access_token': access_token,
            'user_id': user_id,
            'role': 'founder',
        }
        resp = requests.get(url, params=url_params)
        company = get_company(company_id, resp.json().get('startup_roles'))

    if company is None and role in ['employee', 'any']:
        url_params['role'] = 'employee'
        resp = requests.get(url, params=url_params)
        company = get_company(company_id, resp.json()['startup_roles'])

    return company
