from RPA.Browser.Selenium import Selenium
import datetime
br = Selenium(auto_close=False)


class Robot:
    def __init__(self, name):
        self.name = name

    def date_maker(self, list, input):
        # result_list = []
        index = list.index(input)

        # Check if the index allows for retrieving the next three elements
        while True:
            if index + 1 < len(list) and list[index + 1].isdigit():
                result_list = list[index + 1: index + 4]
                break
            else:
                index = index + 1
        return result_list

    def monthnum(self, day1, day2, month1, month2, year1, year2):
        bday_month = month1
        bday_month_number = datetime.datetime.strptime(bday_month, "%B").month
        # bday_month_number

        died_month = month2
        died_month_number = datetime.datetime.strptime(died_month, "%B").month

        if bday_month_number < died_month_number:
            age = year2 - year1
        elif bday_month_number > died_month_number:
            age = year2 - year1 - 1
        elif bday_month_number == died_month_number:
            if day1 < day2 or day1 == day2:
                age = year2 - year1
            elif day1 > day2:
                age = year2 - year1 - 1

        return age


    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):

        br.open_chrome_browser(webpage)
        br.input_text("id:searchInput", "Isaac Newton")       # change the name of person here
        br.press_keys("id:searchInput", "ENTER")
        birthday_element = br.get_text("xpath://table[@class='infobox biography vcard']")

        new_lines = birthday_element.split()

        born_list = self.date_maker(new_lines, "Born")
        dead_list = self.date_maker(new_lines, "Died")

        print("\nBirth and Death details of", new_lines[0], new_lines[1])
        birth = ' '.join(born_list)
        died = ' '.join(dead_list)
        print("Born: ", birth)
        print("Died: ", died)
        final_age = self.monthnum(int(born_list[0]), int(dead_list[0]), born_list[1], dead_list[1], int(born_list[2]), int(dead_list[2]))
        print("Age of individual:", final_age)

        paragraph_elements = br.get_text('//div[@id="mw-content-text"]')
        first_para_list = paragraph_elements.split("\n")
        updated_list = [item.strip() for item in first_para_list]

        max_words_element = max(
                (item for item in updated_list if item.startswith(new_lines[0])),
                key=lambda x: len(x.split())
            )
        print("\nHere is some info on", new_lines[0], new_lines[1],":")
        print(max_words_element)

    #  if person is not dead, error shows up
    #  if person is not born or is not a person, error shows up
    #  works for the scientist in the list given
