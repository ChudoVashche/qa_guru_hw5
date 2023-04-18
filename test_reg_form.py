from selene import browser


def test_reg_form():
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 900
    browser.config.base_url = 'https://demoqa.com'

    # open
    browser.open('/automation-practice-form')

    # name
    browser.element('#firstName').type('Mashka')
    browser.element('#lastName').type('Koshka')

    # email
    browser.element('#userEmail').type('koshka-mashka@mail.ru')

    #gender
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('+79845632245')

    # date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]>[value="1999"]').click()
    browser.element('[class="react-datepicker__month-select"]>[value="11"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()

    # subjects
    browser.element('#subjectsInput').type('his').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()

    # address
    browser.element('#currentAddress').type('Rajpath 17')
    browser.element('#state').click().press_enter()
    browser.element('#city').click().press_enter()

    ...





    ...


