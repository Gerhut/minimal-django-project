from django.test import TestCase, Client

# Create your tests here.
class ViewTestVase(TestCase):
    def test_views(self):
        client = Client()
        response = client.post('/', {"field": 10})
        assert response.status_code == 201
        instance_dict = response.json()

        response = client.get('/' + str(instance_dict['pk']))
        assert response.status_code == 200
        assert response.json()['field'] == 10

        response = client.delete('/' + str(instance_dict['pk']))
        assert response.status_code == 204

        response = client.get('/' + str(instance_dict['pk']))
        assert response.status_code == 404
