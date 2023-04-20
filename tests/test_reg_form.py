from selene import browser, have
import os
from selene.support.shared import browser



def test_reg_form():


    # open
    browser.open('/automation-practice-form')

    # name
    browser.element('#firstName').type('Mashka')
    browser.element('#lastName').type('Koshka')

    # email
    browser.element('#userEmail').type('koshka-mashka@mail.ru')

    #gender
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('8945632145')

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
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()


    # resources
    # browser.element('#uploadPicture').send_keys(os.getcwd() + "/pict.jpg ")
   # browser.element('#uploadPicture').send_keys(os.path.abspath("./tests/resources/pict.jpg"))

   #browser.element('#uploadPicture').send_keys(os.path.abspath(".\tests\resources\pict.jpg"))

    # submit
    browser.element('#submit').click()

   # must have
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts('Student Name Mashka Koshka', 'Student Email koshka-mashka@mail.ru',
                                                    'Gender Female', 'Mobile 8945632145',
                                                    'Date of Birth 31 December,1999',
                                                    'Subjects History', 'Hobbies Reading',
                                                    'Picture',
                                                    'Address Rajpath 17',
                                                    'State and City NCR Delhi'))
    ...









