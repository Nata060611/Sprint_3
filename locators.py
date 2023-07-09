# класс для хранения локаторов
class BurgerLocators:

    # Поле имя в форме регистрации
    input_name = ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']"

    # Поле email в форме регистрации
    input_email = ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']"

    # Поле пароль в форме регистрации
    input_pass = ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']"

    # Кнопка зарегистрировать
    button_reg = ".//form/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"

    # Заголовок H2 с текстом "Вход"
    h2_enter = ".//h2[text()='Вход']"

    # Текст Некорректный пароль на форме регистрации
    p_text = ".//fieldset[3]/div/p[@class='input__error text_type_main-default']"

    # Кнопка "Войти в аккаунт" на главной странице
    button_login_mainpage = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"

    # Кнопка "Войти в аккаунт" на странице входа
    button_login_loginpage = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"

    # Поле email в форме логина
    login_input_email = ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']"

    # Поле пароль в форме логина
    login_input_pass = ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']"

    # Кнопка "Оформить заказ"
    button_order = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"

    # Кнопка "Личный кабинет" на главной странице
    button_lk_mainpage = ".//nav/a/p[@class='AppHeader_header__linkText__3q_va ml-2']"

    # Кнопка "Войти" на странице регистрации
    button_login_reg_and_recover_page = ".//a[@class='Auth_link__1fOlj']"

    # Ссылка Конструктор в Личном Кабинете
    a_constructor = ".//a[@class='AppHeader_header__link__3D_hX']/p[text()='Конструктор']/parent::a"

    # Кнопка ВЫХОД в "Личном кабинете"
    button_exit_in_lk = ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and (text()='Выход')]"

    # Активный таб в конструкторе
    div_current = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"

    # Первый таб в конструкторе
    div_first = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[@style='display: flex;']/div[1]"

    # Второй таб в конструкторе
    div_second = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[@style='display: flex;']/div[2]"

    # Третий таб в конструкторе
    div_third = ".//section[@class='BurgerIngredients_ingredients__1N8v2']/div[@style='display: flex;']/div[3]"
