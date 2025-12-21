from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Dish
from django.urls import reverse
from django.test import Client


class ModelTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test_chef",
            password="testpassword123",
            first_name="Gordon",
            last_name="Ramsay",
            years_of_experience=15
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Dessert",
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Test Type")
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test description",
            price=10.50,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), dish.name)


    def test_create_cook_with_experience(self):
        username = "chef_luigi"
        password = "testpassword123"
        years_of_experience = 5
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))


class PublicViewTests(TestCase):
    def test_login_required(self):
        urls = [
            reverse("kitchen:index"),
            reverse("kitchen:cook-list"),
            reverse("kitchen:dish-list"),
        ]
        for url in urls:
            res = self.client.get(url)
            self.assertNotEqual(res.status_code, 200)


class PrivateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_index_page(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertEqual(res.status_code, 200)

    def test_retrieve_cooks(self):
        res = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(res.status_code, 200)

    def test_visit_count_increases(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "You have visited this page")
        self.assertContains(res, '<span class="badge bg-dark">1</span>')
        self.assertContains(res, "time in this session")
        res = self.client.get(reverse("kitchen:index"))
        self.assertContains(res, '<span class="badge bg-dark">2</span>')
        self.assertContains(res, "times in this session")


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="adminpassword123"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="test_cook",
            password="password123",
            years_of_experience=12
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
