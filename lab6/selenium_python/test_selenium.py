from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Firefox()

BASE_PATH = os.getcwd()

def test_home_page():
    driver.get(f"file://{BASE_PATH}/index.html")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    message = driver.find_element(By.ID, "home-message").text
    assert message == "Hello World"


def test_hello_page():
    driver.get(f"file://{BASE_PATH}/hello.html")
    name_input = driver.find_element(By.ID, "name")
    name_input.send_keys("Bartosz")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    message = driver.find_element(By.ID, "hello-message").text
    assert message == "Hello, Bartosz!"


def test_login_success():
    driver.get(f"file://{BASE_PATH}/login.html")
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("admin")
    password_input.send_keys("secret")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)
    response = driver.find_element(By.ID, "response").text
    assert '{"status":"success"}' in response


def test_login_failure():
    driver.get(f"file://{BASE_PATH}/login.html")
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("admin")
    password_input.send_keys("wrongpassword")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)
    response = driver.find_element(By.ID, "response").text
    assert '"status":"error"' in response


def test_login_failure_credentials():
    driver.get(f"file://{BASE_PATH}/login.html")
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("admin")
    password_input.send_keys("wrongpassword")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(1)
    response = driver.find_element(By.ID, "response").text
    assert '"message":"Invalid credentials"' in response


def test_products_page_apple():
    driver.get(f"file://{BASE_PATH}/products.html")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    products = driver.find_elements(By.TAG_NAME, "li")
    product_names = [p.text for p in products]
    assert "apple" in product_names

def test_products_page_banana():
    driver.get(f"file://{BASE_PATH}/products.html")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    products = driver.find_elements(By.TAG_NAME, "li")
    product_names = [p.text for p in products]
    assert "banana" in product_names

def test_products_page_cherry():
    driver.get(f"file://{BASE_PATH}/products.html")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    products = driver.find_elements(By.TAG_NAME, "li")
    product_names = [p.text for p in products]
    assert "cherry" in product_names

def test_counter_increment():
    driver.get(f"file://{BASE_PATH}/counter.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.clear()
    number_input.send_keys("10")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "counter-result").text
    assert result == "11"

def test_reverse_text():
    driver.get(f"file://{BASE_PATH}/reverse.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.send_keys("python")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "reverse-result").text
    assert result == "nohtyp"

def test_status_check():
    driver.get(f"file://{BASE_PATH}/status.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "status-result").text
    assert result == "ok"

def test_user_found():
    driver.get(f"file://{BASE_PATH}/user.html")
    user_input = driver.find_element(By.ID, "user_id")
    user_input.clear()
    user_input.send_keys("1")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "user-result").text
    assert "Alice" in result

def test_user_not_found():
    driver.get(f"file://{BASE_PATH}/user.html")
    user_input = driver.find_element(By.ID, "user_id")
    user_input.clear()
    user_input.send_keys("999")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "user-result").text
    assert "User not found" in result


def test_home_page_button_text():
    driver.get(f"file://{BASE_PATH}/index.html")
    button = driver.find_element(By.TAG_NAME, "button")
    assert button.text == "Load Message"

def test_hello_page_empty_name():
    driver.get(f"file://{BASE_PATH}/hello.html")
    name_input = driver.find_element(By.ID, "name")
    name_input.clear()
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)
    message = driver.find_element(By.ID, "hello-message").text
    assert message == "undefined"

def test_login_empty_fields():
    driver.get(f"file://{BASE_PATH}/login.html")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    response = driver.find_element(By.ID, "response").text
    assert '"status":"error"' in response

def test_counter_increment_zero():
    driver.get(f"file://{BASE_PATH}/counter.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.clear()
    number_input.send_keys("0")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "counter-result").text
    assert result == "1"

def test_reverse_empty_text():
    driver.get(f"file://{BASE_PATH}/reverse.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "reverse-result").text
    assert result == 'undefined'


def test_reverse_text_kot():
    driver.get(f"file://{BASE_PATH}/reverse.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.send_keys("kot")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "reverse-result").text
    assert result == "tok"


def test_status_check_text():
    driver.get(f"file://{BASE_PATH}/status.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "status-result").text
    assert result == "ok"

def test_uppercase_hello():
    driver.get(f"file://{BASE_PATH}/uppercase.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.send_keys("hello")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "uppercase-result").text
    assert result == "HELLO"

def test_uppercase_empty():
    driver.get(f"file://{BASE_PATH}/uppercase.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "uppercase-result").text
    assert result == "undefined"

def test_lowercase_HELLO():
    driver.get(f"file://{BASE_PATH}/lowercase.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.send_keys("HELLO")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "lowercase-result").text
    assert result == "hello"

def test_lowercase_empty():
    driver.get(f"file://{BASE_PATH}/lowercase.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "lowercase-result").text
    assert result == "undefined"

def test_length_text():
    driver.get(f"file://{BASE_PATH}/length.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.send_keys("abcde")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "length-result").text
    assert result == "5"

def test_length_empty():
    driver.get(f"file://{BASE_PATH}/length.html")
    text_input = driver.find_element(By.ID, "text")
    text_input.clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "length-result").text
    assert result == "undefined"

def test_even_2():
    driver.get(f"file://{BASE_PATH}/even.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("2")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "even-result").text
    assert result == "true"

def test_even_3():
    driver.get(f"file://{BASE_PATH}/even.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "even-result").text
    assert result == "false"

def test_odd_3():
    driver.get(f"file://{BASE_PATH}/odd.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "odd-result").text
    assert result == "true"

def test_odd_2():
    driver.get(f"file://{BASE_PATH}/odd.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("2")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "odd-result").text
    assert result == "false"

def test_sum_2_3():
    driver.get(f"file://{BASE_PATH}/sum.html")
    a_input = driver.find_element(By.ID, "a")
    b_input = driver.find_element(By.ID, "b")
    a_input.send_keys("2")
    b_input.send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "sum-result").text
    assert result == "5"

def test_sum_negative():
    driver.get(f"file://{BASE_PATH}/sum.html")
    a_input = driver.find_element(By.ID, "a")
    b_input = driver.find_element(By.ID, "b")
    a_input.send_keys("-5")
    b_input.send_keys("10")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "sum-result").text
    assert result == "5"

def test_multiply_2_3():
    driver.get(f"file://{BASE_PATH}/multiply.html")
    a_input = driver.find_element(By.ID, "a")
    b_input = driver.find_element(By.ID, "b")
    a_input.send_keys("2")
    b_input.send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "multiply-result").text
    assert result == "6"

def test_multiply_zero():
    driver.get(f"file://{BASE_PATH}/multiply.html")
    a_input = driver.find_element(By.ID, "a")
    b_input = driver.find_element(By.ID, "b")
    a_input.send_keys("0")
    b_input.send_keys("100")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "multiply-result").text
    assert result == "0"

def test_factorial_5():
    driver.get(f"file://{BASE_PATH}/factorial.html")
    n_input = driver.find_element(By.ID, "n")
    n_input.send_keys("5")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "factorial-result").text
    assert result == "120"

def test_factorial_0():
    driver.get(f"file://{BASE_PATH}/factorial.html")
    number_input = driver.find_element(By.ID, "n")
    number_input.send_keys("0")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "factorial-result").text
    assert result == "1"

def test_palindrome_kayak():
    driver.get(f"file://{BASE_PATH}/palindrome.html")
    text_input = driver.find_element(By.ID, "word")
    text_input.send_keys("kayak")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "palindrome-result").text
    assert result == "true"

def test_palindrome_hello():
    driver.get(f"file://{BASE_PATH}/palindrome.html")
    text_input = driver.find_element(By.ID, "word")
    text_input.send_keys("hello")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "palindrome-result").text
    assert result == "false"

def test_prime_7():
    driver.get(f"file://{BASE_PATH}/prime.html")
    number_input = driver.find_element(By.ID, "n")
    number_input.send_keys("7")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "prime-result").text
    assert result == "true"

def test_prime_4():
    driver.get(f"file://{BASE_PATH}/prime.html")
    number_input = driver.find_element(By.ID, "n")
    number_input.send_keys("4")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "prime-result").text
    assert result == "false"

def test_greet_john():
    driver.get(f"file://{BASE_PATH}/greet.html")
    name_input = driver.find_element(By.ID, "name")
    role_input = driver.find_element(By.ID, "role")
    name_input.send_keys("John")
    role_input.send_keys("tester")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "greet-result").text
    assert result == "Hello John, you are a great tester!"

def test_greet_empty():
    driver.get(f"file://{BASE_PATH}/greet.html")
    name_input = driver.find_element(By.ID, "name")
    name_input.clear()
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "greet-result").text
    assert result == "undefined"

def test_day_1():
    driver.get(f"file://{BASE_PATH}/dayofweek.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("1")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "dayofweek-result").text
    assert result == "Tuesday"

def test_day_6():
    driver.get(f"file://{BASE_PATH}/dayofweek.html")
    number_input = driver.find_element(By.ID, "number")
    number_input.send_keys("6")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "dayofweek-result").text
    assert result == "Sunday"

def test_random_between_0_100():
    driver.get(f"file://{BASE_PATH}/random.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "random-result").text
    assert 0 <= int(result) <= 100

def test_random_another():
    driver.get(f"file://{BASE_PATH}/random.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "random-result").text
    assert 0 <= int(result) <= 100

def test_now_time_not_empty():
    driver.get(f"file://{BASE_PATH}/nowtime.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "nowtime-result").text
    assert result != ""

def test_now_time_format():
    driver.get(f"file://{BASE_PATH}/nowtime.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "nowtime-result").text
    assert ":" in result

def test_uuid_not_empty():
    driver.get(f"file://{BASE_PATH}/uuid.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "uuid-result").text
    assert len(result) > 0

def test_uuid_format():
    driver.get(f"file://{BASE_PATH}/uuid.html")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "uuid-result").text
    assert "-" in result


if __name__ == "__main__":
    test_home_page()
    test_hello_page()
    test_login_success()
    test_login_failure()
    test_login_failure_credentials()
    test_products_page_apple()
    test_products_page_banana()
    test_products_page_cherry()
    test_counter_increment()
    test_reverse_text()
    test_status_check()
    test_user_found()
    test_user_not_found()
    test_home_page_button_text()
    test_hello_page_empty_name()
    test_login_empty_fields()
    test_counter_increment_zero()
    test_reverse_empty_text()
    test_reverse_text_kot()
    test_status_check_text()
    test_uppercase_hello()
    test_uppercase_empty()
    test_lowercase_HELLO()
    test_lowercase_empty()
    test_length_text()
    test_length_empty()
    test_even_2()
    test_even_3()
    test_odd_3()
    test_odd_2()
    test_sum_2_3()
    test_sum_negative()
    test_multiply_2_3()
    test_multiply_zero()
    test_factorial_5()
    test_factorial_0()
    test_palindrome_kayak()
    test_palindrome_hello()
    test_prime_7()
    test_prime_4()
    test_greet_john()
    test_greet_empty()
    test_day_1()
    test_day_6()
    test_random_between_0_100()
    test_random_another()
    test_now_time_not_empty()
    test_now_time_format()
    test_uuid_not_empty()
    test_uuid_format()

    driver.quit()
