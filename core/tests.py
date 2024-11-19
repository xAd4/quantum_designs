from django.test import TestCase
from contact.models import Contact
from django.utils import timezone

class ContactModelTest(TestCase):
    def setUp(self):
        # Create a test contact
        self.contact = Contact.objects.create(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="Test Message"
        )

    def test_contact_creation(self):
        # Prove that the contact was created correctly
        self.assertTrue(isinstance(self.contact, Contact))
        self.assertEqual(self.contact.name, "Test User")
        self.assertEqual(self.contact.email, "test@example.com")
        self.assertEqual(self.contact.subject, "Test Subject")
        self.assertEqual(self.contact.message, "Test Message")
        
    def test_contact_str_method(self):
         # Test the __str__ method
        expected_str = "Test User sent message: Test Subject"
        self.assertEqual(str(self.contact), expected_str)
        
    def test_contact_dates(self):
        # Prove that dates are created automatically
        self.assertIsNotNone(self.contact.created_at)
        self.assertIsNotNone(self.contact.updated_at)
        
    def test_verbose_names(self):
        # Test the verbose names of the model
        self.assertEqual(
            Contact._meta.verbose_name, "Contact Message"
        )
        self.assertEqual(
            Contact._meta.verbose_name_plural, "Contact Messages"
        )

