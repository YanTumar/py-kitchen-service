from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Dish

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
