from django.test import TestCase, Client

# Create your tests here.
class ViewTestVase(TestCase):
    def test_views(self):
        client = Client()
        response = client.post('/', {"content": 'hello'})
        assert response.status_code == 201
        post_dict = response.json()

        response = client.get('/' + str(post_dict['id']))
        assert response.status_code == 200
        assert response.json()['content'] == 'hello'

        response = client.delete('/' + str(post_dict['id']))
        assert response.status_code == 204

        response = client.get('/' + str(post_dict['id']))
        assert response.status_code == 404
