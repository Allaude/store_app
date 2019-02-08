import factory
from pytest_factoryboy import register
from mystore.models import Item


@register
class ItemFactory(factory.Factory):
    item = factory.Sequence(lambda n: 'item%d' % n)
    price = 30.00
    weight = 2000.00
    user_id = 1

    class Meta:
        model = Item


def test_post_items(client, admin_headers):
    # test bad data
    item = {'item': 'tes'}
    rep = client.post('/api/v1/items',
                      json=item,
                      headers=admin_headers)
    assert rep.status_code == 422
    item['price'] = 30.00
    item['weight'] = 3000.00
    rep = client.post('/api/v1/items',
                      json=item,
                      headers=admin_headers)

    data = rep.get_json()
    rep = client.get('/api/v1/items/9999', headers=admin_headers)
    assert rep.status_code == 404
    rep = client.get('/api/v1/items/%d' % data['item']['id'], headers=admin_headers)
    assert rep.status_code == 200
    result = rep.get_json()['item']
    assert result['item'] == item['item']
    assert result['price'] == item['price']
    assert result['weight'] == item['weight']

    data_update = {"price": 50}
    rep = client.put('/api/v1/items/%d' % data['item']['id'], json=data_update, headers=admin_headers)
    assert rep.status_code == 200
    result = rep.get_json()['item']
    assert result['price'] == data_update['price']
    rep = client.delete('/api/v1/items/%d' % data['item']['id'], headers=admin_headers)
    assert rep.status_code == 200
    rep = client.get('/api/v1/items/%d' % data['item']['id'], headers=admin_headers)
    assert rep.status_code == 404


def test_get_all_item(client, db, item_factory, admin_headers):
    items = item_factory.create_batch(30)

    db.session.add_all(items)
    db.session.commit()

    rep = client.get('/api/v1/items', headers=admin_headers)
    assert rep.status_code == 200

    results = rep.get_json()
    for item in items:
        assert any(i['id'] == item.id for i in results['results'])
