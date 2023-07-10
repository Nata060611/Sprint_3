# класс для хранения локаторов
class BurgerLocators:

    # Поле имя в форме регистрации
    input_name_reg_page = ".//div//label[contains(text(), 'Имя')]/parent::div/input"

    # Поле email в форме регистрации
    input_email_reg_page = ".//div//label[contains(text(), 'Email')]/parent::div/input"

    # Поле пароль в форме регистрации
    input_pass_reg_page = ".//div//label[contains(text(), 'Пароль')]/parent::div/input"

    # Кнопка зарегистрировать
    button_reg = ".//form/button[contains(text(), 'Зарегистрироваться')]"

    # Заголовок H2 с текстом "Вход"
    h2_enter = ".//h2[contains(text(), 'Вход')]"

    # Текст Некорректный пароль на форме регистрации
    p_error_pass = ".//div//label[contains(text(), 'Пароль')]/parent::div/following-sibling::p[contains(@class, 'input__error')]"

    # Кнопка "Войти в аккаунт" на главной странице
    button_login_mainpage = ".//button[contains(text(), 'Войти в аккаунт')]"

    # Кнопка "Войти" на странице входа
    button_login_loginpage = ".//button[contains(text(), 'Войти')]"

    # Поле email в форме логина
    login_input_email = ".//div//label[contains(text(), 'Email')]/parent::div/input"

    # Поле пароль в форме логина
    login_input_pass = ".//div//label[contains(text(), 'Пароль')]/parent::div/input"

    # Кнопка "Оформить заказ" на главной у авторизованного пользователя
    button_order = ".//button[contains(text(), 'Оформить заказ')]"

    # Кнопка "Личный кабинет" на главной странице
    button_lk_mainpage = ".//nav/a/p[contains(text(), 'Личный Кабинет')]/parent::a"

    # Кнопка "Войти" на странице регистрации
    button_login_reg_and_recover_page = ".//a[contains(text(), 'Войти')]"

    # Ссылка Конструктор в Личном Кабинете
    a_constructor = ".//p[contains(text(), 'Конструктор')]/parent::a"

    # Кнопка ВЫХОД в "Личном кабинете"
    button_exit_in_lk = ".//nav/ul/li/button[contains(text(), 'Выход')]"

    # Активный таб в конструкторе
    tabs_current = ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]"

    # Первый таб в конструкторе
    tabs_bulki = ".//span[contains(text(), 'Булки')]/parent::div"

    # Второй таб в конструкторе
    tabs_souses = ".//span[contains(text(), 'Соусы')]/parent::div"

    # Третий таб в конструкторе
    tabs_nachinki = ".//span[contains(text(), 'Начинки')]/parent::div"

    # Заголовок H2 Булки
    tabs_bulki_h2 = ".//h2[contains(text(), 'Булки')]"

    # Заголовок H2 Начинки
    tabs_souses_h2 = ".//h2[contains(text(), 'Соусы')]"

    # Заголовок H2 Начинки
    tabs_nachinki_h2 = ".//h2[contains(text(), 'Начинки')]"