from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestAuthentification(StaticLiveServerTestCase):
    def test_signup(self):
        self.browser = webdriver.Chrome("User/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("user-signup"))

        username = self.browser.find_element_by_id("id_username")
        username.send_keys("ewen_test")
        email = self.browser.find_element_by_id("id_email")
        email.send_keys("ewen_test@test.com")
        password1 = self.browser.find_element_by_id("id_password1")
        password1.send_keys("ewen12345")
        password2 = self.browser.find_element_by_id("id_password2")
        password2.send_keys("ewen12345")
        signup = self.browser.find_element_by_name("signup")
        signup.submit()

        self.assertEqual(self.browser.find_element_by_tag_name("h2").text, "ewen_test")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-account")
        )
        self.browser.close()

    def test_signin_not_account(self):
        self.browser = webdriver.Chrome("User/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("user-signin"))

        email = self.browser.find_element_by_id("id_email")
        email.send_keys("ewen_test@test.com")
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element_by_name("signin")
        signin.submit()

        self.assertEqual(
            self.browser.find_element_by_tag_name("p").text, "Identifiants incorrects"
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-signin")
        )
        self.browser.close()

    def test_signin(self):
        self.browser = webdriver.Chrome("User/tests/functional_tests/chromedriver")
        self.browser.get(self.live_server_url + reverse("user-signin"))

        email = self.browser.find_element_by_id("id_email")
        email.send_keys("toto@gmail.com")
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element_by_name("signin")
        signin.submit()

        self.assertEqual(self.browser.find_element_by_tag_name("h2").text, "toto")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-account")
        )
        self.browser.close()
