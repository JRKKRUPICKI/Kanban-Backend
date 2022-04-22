from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from . import views
from .models import User, Column, Row, Task, Limit, TaskUser


class ColumnTest(APITestCase):
    def setUp(self):
        self.dummy = Column.objects.create(name="ToDo", position=0, limit=0)

    def post_column(self, name, position, limit):
        url = reverse(views.ColumnView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_column(self):
        response = self.post_column("Done", 0, 0)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_columnList(self):
        response = self.client.get(reverse(views.ColumnView.name))
        assert response.status_code == status.HTTP_200_OK

    def test_get_columnDetail(self):
        response = self.client.get(reverse(views.ColumnDetailView.name, args=[self.dummy.id]))
        assert response.status_code == status.HTTP_200_OK

    def test_post_existing_column_name(self):
        response_one = self.post_column("ToDo", 0, 0)
        assert response_one.status_code == status.HTTP_400_BAD_REQUEST

    def test_put_column(self):
        url = reverse(views.ColumnDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "ToDo"

        data = {'name': "Changed"}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == "Changed"

    def test_delete_column(self):
        url = reverse(views.ColumnDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        delete_response = self.client.delete(url)
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


class RowTest(APITestCase):
    def setUp(self):
        self.dummy = Row.objects.create(name="Frontend", position=0, limit=0)

    def post_row(self, name, position, limit):
        url = reverse(views.RowView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_row(self):
        response = self.post_row("Done", 0, 0)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_rowList(self):
        response = self.client.get(reverse(views.RowView.name))
        assert response.status_code == status.HTTP_200_OK

    def test_get_rowDetail(self):
        response = self.client.get(reverse(views.RowDetailView.name, args=[self.dummy.id]))
        assert response.status_code == status.HTTP_200_OK

    def test_post_existing_row_name(self):
        response_one = self.post_row("Frontend", 0, 0)
        assert response_one.status_code == status.HTTP_400_BAD_REQUEST

    def test_put_row(self):
        url = reverse(views.RowDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Frontend"

        data = {'name': "Changed"}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == "Changed"

    def test_delete_row(self):
        url = reverse(views.RowDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        delete_response = self.client.delete(url)
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TaskTest(APITestCase):
    def setUp(self):
        self.column = Column.objects.create(name="ToDo", position=0, limit=0)
        self.row = Row.objects.create(name="Frontend", position=0, limit=0)
        self.dummy = Task.objects.create(name="Task", description="opis", position=0, column=self.column, row=self.row)

    def post_column(self, name, position, limit):
        url = reverse(views.ColumnView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def post_row(self, name, position, limit):
        url = reverse(views.RowView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def post_task(self, name, desciprion, position, column, row):
        url = reverse(views.TaskView.name)
        data = {
            'name': name,
            'desciprion': desciprion,
            'position': position,
            'column': column,
            'row': row,
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_task(self):
        self.post_column('ToDo', 0, 0)
        columns = self.client.get(reverse(views.ColumnView.name))
        column_id = columns.json()[0]['id']

        self.post_row('Frontend', 0, 0)
        rows = self.client.get(reverse(views.RowView.name))
        row_id = columns.json()[0]['id']

        response = self.post_task("Task", "desc", 0, column_id, row_id)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_taskList(self):
        response = self.client.get(reverse(views.TaskView.name))
        assert response.status_code == status.HTTP_200_OK

    def test_get_taskDetail(self):
        response = self.client.get(reverse(views.TaskDetailView.name, args=[self.dummy.id]))
        assert response.status_code == status.HTTP_200_OK

    def test_put_task(self):
        url = reverse(views.TaskDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == "Task"

        data = {'name': "Changed"}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == "Changed"

    def test_delete_task(self):
        url = reverse(views.TaskDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        delete_response = self.client.delete(url)
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


class UserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="Mike", first_name="Tyson")

    def registerUser(self, username, email, password, password2):
        url = reverse(views.RegisterView.name)
        data = {
            'username': username,
            'email': email,
            'password': password,
            'password2': password2,
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_register_user(self):
        response = self.registerUser("login", "email@email.com", "haslo", "haslo")
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_user_list(self):
        response = self.client.get(reverse(views.UserView.name))
        assert response.status_code, status.HTTP_200_OK

    def test_get_user_detail(self):
        response = self.client.get(reverse(views.UserDetailsView.name, args=[self.user.id]))
        assert response.status_code, status.HTTP_200_OK

    def test_put_user(self):
        url = reverse(views.UserDetailsView.name, args=[self.user.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == "Mike"

        data = {'username': "Changed"}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['username'] == "Changed"

    def test_delete_user(self):
        url = reverse(views.UserDetailsView.name, args=[self.user.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        delete_response = self.client.delete(url)
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_password_fields_validation(self):
        response = self.registerUser("login", "email@email.com", "haslo", "haslo2")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_existing_email_and_login(self):
        response = self.registerUser("login", "email@email.com", "haslo", "haslo")
        assert response.status_code == status.HTTP_201_CREATED
        response2 = self.registerUser("login", "email2@email.com", "haslo2", "haslo2")
        assert response2.status_code == status.HTTP_400_BAD_REQUEST
        response3 = self.registerUser("login3", "email@email.com", "haslo3", "haslo3")
        assert response3.status_code == status.HTTP_400_BAD_REQUEST


class LimitTest(APITestCase):
    def setUp(self):
        self.column = Column.objects.create(name="ToDo", position=0, limit=0)
        self.row = Row.objects.create(name="Frontend", position=0, limit=0)
        self.dummy = Limit.objects.create(limit=0, column=self.column, row=self.row)

    def post_column(self, name, position, limit):
        url = reverse(views.ColumnView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def post_row(self, name, position, limit):
        url = reverse(views.RowView.name)
        data = {
            'name': name,
            'position': position,
            'limit': limit,
        }
        response = self.client.post(url, data, format='json')
        return response

    def post_limit(self, limit, column, row):
        url = reverse(views.LimitView.name)
        data = {
            'limit': limit,
            'column': column,
            'row': row,
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_limit(self):
        self.post_column('ToDo', 0, 0)
        columns = self.client.get(reverse(views.ColumnView.name))
        column_id = columns.json()[0]['id']

        self.post_row('Frontend', 0, 0)
        rows = self.client.get(reverse(views.RowView.name))
        row_id = columns.json()[0]['id']

        response = self.post_limit(0, column_id, row_id)
        assert response.status_code == status.HTTP_201_CREATED

    def test_get_limitList(self):
        response = self.client.get(reverse(views.LimitView.name))
        assert response.status_code == status.HTTP_200_OK

    def test_get_limitDetail(self):
        response = self.client.get(reverse(views.LimitDetailView.name, args=[self.dummy.id]))
        assert response.status_code == status.HTTP_200_OK

    def test_put_limit(self):
        url = reverse(views.LimitDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['limit'] == 0

        data = {'limit': 6}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['limit'] == 6

    def test_delete_limit(self):
        url = reverse(views.LimitDetailView.name, args=[self.dummy.id])
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        delete_response = self.client.delete(url)
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
