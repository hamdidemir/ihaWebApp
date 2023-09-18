from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import iha, Kira, RentalHistory
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import RentalForm


class IhaViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        # Create a test Iha object
        self.iha = iha.objects.create(
            Marka='Test Marka',
            Model='Test Model',
            Faydalı_yük=100,
            Havada_kalma_süresi=5,
            Kanat_açıklığı=10,
            Maksimum_kalkış_ağırlığı=200,
            image = image,
        )

        # Create a test Kira object
        self.rental = Kira.objects.create(
            iha=self.iha,
            kirayan_üye=self.user,
            baslangıc_tarih=datetime.now().date(),
            baslangıc_saat=datetime.now().time(),
            bitiş_tarih=(datetime.now() + timedelta(days=1)).date(),
            bitiş_saat=datetime.now().time(),
            Adet=1,
        )

    def test_index_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send GET request
        response = self.client.get(reverse('iha:index'))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the user_rentals variable is present in the context
        self.assertIn('user_rentals', response.context)

    def test_iha_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send GET request
        response = self.client.get(reverse('iha:iha_view', args=[self.iha.id]))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

    def test_add_rental_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request with valid data
        data = {
            'baslangıc_tarih': datetime.now().date(),
            'baslangıc_saat': datetime.now().time(),
            'bitiş_tarih': (datetime.now() + timedelta(days=1)).date(),
            'bitiş_saat': datetime.now().time(),
            'Adet': 1,
        }
        response = self.client.post(reverse('iha:add_rental', args=[self.iha.id]), data)

        # Check that the response has a 200 status code since it should render a template
        self.assertEqual(response.status_code, 200)

        # Check that the rendered template is 'iha/ihas.html'
        self.assertTemplateUsed(response, 'iha/ihas.html')

        # Check that the form is present in the context
        self.assertIn('form', response.context)

    def test_cancel_rental_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a POST request to cancel the rental
        response = self.client.post(reverse('iha:cancel_rental', args=[self.rental.id]))

        # Check that the response redirects to the index page
        self.assertRedirects(response, reverse('iha:index'))

        # Check that the rental object is deleted
        self.assertFalse(Kira.objects.filter(id=self.rental.id).exists())

    def test_rental_history_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request
        response = self.client.get(reverse('iha:rental_history'))

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)
