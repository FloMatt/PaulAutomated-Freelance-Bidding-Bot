# Imports of prgram dependencies. Everyone of these is used somewhere
import random
import time
from tkinter import *
from tkinter import ttk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import messagebox
import pandas as pd
import itertools
from itertools import islice
import threading
import socket
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
# sys.setrecursionlimit(25000)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# main Variables for the program
original_order_id_list = []
unbid_new = []
unneeded_subject_list = []  # ['Criminal Law', 'History', 'Management', 'Human Resource Management']

#This section is was used in develpoment to minimize the time taken to re-run the application. Hard-coded inputs
'''
on_revision = 0
slides_checked = 1
problems_checked = 1
questions_checked = 1
high_checked = 1
under_checked = 1
master_checked = 1
phd_checked = 1

# min_price = 0
# max_price = 10000
# min_price = float(input("Min order price: "))
min_price = 1  # to be removed *
# max_price = float(input("Max order price: "))
max_price = 925  #
# time_min = 0
# time_max = 10000000
# time_min = int(input("Time min (hrs): ")) * 60
time_min = 1 * 60  #
# time_max = int(input("Time max (hrs): ")) * 60
time_max = 4000 * 60  #

# pages_min = 1
# pages_max = 10000
# pages_min = int(input("Minium pages: "))
pages_min = 1  #
# pages_max = int(input("Maximum pages: "))
pages_max = 1808  #
'''
# *************************************************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Major sections divided using such comments, haha

# Tkinter function testing function
def btn_clicked():
    print("Button Clicked")

# Adding aesthetic appeal to the output 
def all_output():
    for tr in all_s:
        output.insert(INSERT, ":ǀ------------Applied----------------ǀ")
        output.insert(INSERT, '\n')
        output.insert(INSERT, ":ǀ ")
        output.insert(INSERT, tr)
        output.insert(INSERT, '\n')
        output.see("end")

# Bot Functions @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# starting
# *************************************************************
# This is where Chrome is opened and its instance created

# This is where Chrome is opened and its instance created


def start_writedom():
    try:
        print("Please Wait. Launching Chrome")
        global browser
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        prefs = {"profile.default_content_setting_values.notifications": 2,
                 "credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        # options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        browser = webdriver.Chrome(options=options,
                                   executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        time.sleep(2)
        browser.set_window_size(1225, 960)
        print("Browser launched successfully")
        launch()
    except Exception as e:
        print("This error122: ", e)

        start_writedom()


# *************************************************************
# Search the website and log in function
pp = [] # these variables are used to control immediate functions ...
# ...they are decalred globally because they are used to control state elsewhere
def launch():
    if __name__ == '__main__':
        try:
            browser.get('https://writedom.com/dashboard/')
            time.sleep(2)
            browser.find_element_by_name('email').send_keys(entry1.get())
            browser.find_element_by_name('password').send_keys(entry0.get())
            browser.find_element_by_class_name("signin-button").click()

            time.sleep(10)
        except TimeoutException:
            print("Connection Timeout")  # More needs to be done?????????
            is_connected()
            # what_is_happening()
            pass
        except NoSuchElementException:
            print("Logged in already")
            is_connected()
            # what_is_happening()
            pass
        except ElementClickInterceptedException:
            print("Clicking error")
            is_connected()
            # what_is_happening()
            pass
        except Exception as e:
            print("Failed to launch. Trying again", e)
            is_connected()
            # what_is_happening()
            # launch ()
        try:
            available_orders_header = browser.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/div[1]/div/main/div/div/h3').text
            if available_orders_header == 'Available Orders':  # checking for title of page
                print('\n'"Writedom Logged In successfully")
                all_orders_fn()
            else:
                print("Something happened!")
                pass
        except Exception as e:
            print("Access Error: ", e)
            ''''
            # this part checks whether the login was sucessful. Got a bug here, will be fixed
            time.sleep(18)
            try:
                b = browser.find_element_by_class_name('page-title').text
                if b == 'Sign In':
                    print("Login details are incorrect.\nCheck the details and try again")
                    browser.quit()
                    return
                else:
                    pass
            except Exception as e:
                print("Unkown error! Please restart the software")
                browser.quit()
                return
            '''

# This make sure that the chat box that sometimes pop up upon login is closed
# it also ensures that maximum number or orders are selected for display on screen
def all_orders_fn():
    print("Minimize the chat box")
    time.sleep(2)
    try:
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div').click()
    except NoSuchElementException:
        pass
    try:
        browser.execute_script("window.scrollTo(0, 1118)")
        browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[1]/div/main/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/button/div').click()
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[7]/span/div/div/div').click()
        print("All set!")

    except NoSuchElementException:
        print("Unable to load all")
        pass
    except ElementNotInteractableException:
        print("Unable to scroll, But its fine")
        pass
    except Exception:
        pass
    print("ALL SYSTEM GO") # 
    # order_listener()


# CHeck for anormalies.
# This is all the possible screens that a user can click while the user is under the bot control
# This bot can detect this and take back control and return to the orders page
what = [1, 2, 5]
freeze = []
away_from_orders_options_list = ['Help Needed', 'In Progress',
                                 'On Revision', 'Pending Clarification',
                                 'My Orders', 'Messages', 'Announcements',
                                 'Feedbacks', 'Financial overview',
                                 'Available Orders']

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Boolean check of internet connection and will only return when the internet is back. Recursion with variable timing
# The bot can only start if there is an internet connection
# This functions is also called during some lag senarios to check if internet is still available
net_timer = []
net_timer_delay = []
def is_connected():
    net = False
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))  # Checking for internet conn
        net_timer_delay.clear()
        net = True
        return net
    except OSError:
        pass
    if net is not True:
        net_timer.append(4)
        net_timer_delay.append(3)
        if len(net_timer) <= 1000:  # loop for 1000 times in a cumulative recursion of 20 seconds
            time.sleep(len(net_timer_delay))
            print("Checking internet again in:", len(net_timer_delay), "seconds")
            if len(net_timer_delay) > 20:  # resetting the timer when 20 seconds wait time are reached
                net_timer_delay.clear()

            is_connected()
        else:
            net_timer.clear()
            print("Internet gone completely")
            net = False
            return net
            # You can close the browser here after internet is gone for long.


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def what_is_happening():
    # Check for hearder in the page to ensure that it is on the right page at the right time
    try:
        available_orders_header = browser.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div/main/div/div/h3').text
    except NoSuchElementException:  # ic n case the program is not in any page on the list
        available_orders_header = ''
        print("What did you do! 1")
        try:  # click available orders
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass
    except Exception:
        available_orders_header = ''
        print("What did you do!")
        try:  # click available orders
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass
    if available_orders_header == 'Available Orders':
        print("is_happening. All good in orders")
        return True
    while available_orders_header in away_from_orders_options_list:
        print("Don't click on other", available_orders_header, "! I am in control: ")
        # what.append(3)
        time.sleep(len(what))
        try:  # click available orders
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()

        except Exception:
            freeze.append(3)
            is_connected()
            if len(freeze) > 3:
                print("Page frozen by ", available_orders_header)
            else:
                pass
        available_orders_header = ''
        what_is_happening()
    return


# __________________________________________
# this function checks the internet before the bot starts
# it is separate because it does not have recusrion as it only checks onece. 
ss = []
def first_is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))  # Checking for internet conn
        return True
    except OSError:
        time.sleep(2)
        ss.append(3)
        if len(ss) < 2:
            first_is_connected()
        else:
            print("No Internet!\n Please check your connection and Try again")
            pass
    except Exception:
        print("Did not start.Problem with internet")


er0 = []
er1 = []


# This function checks the order number and if it is available
# It cycles through untill available for a max of 100 times before returning force and removing the order from the bid list
# If the order is available it clicks to open it and return true
def dom_0(order_2):  # cliick on orders
    try:
        print("here 0")
        k_0 = 'PawaWritedomBot'
        # check if the order numbers match
        for _ in itertools.cycle(k_0):
            try:
                y = browser.find_element_by_partial_link_text(order_2).text
                if len(y) > 0:
                    browser.find_element_by_partial_link_text(order_2).click()  # click on an order
                    return True

                else:
                    pass
            except Exception as e:
                print("Error 0: ", e)
                er0.append(0)
                is_connected()
                what_is_happening()
                if len(er0) < 100:  # loop for 100 times looking for the order
                    continue
                else:
                    er0.clear()
                    what_is_happening()
                    print("Order ", order_2, " has a problem. Won't bid")
                    browser.refresh()

                break
                # Check if order is still available
            continue
    except Exception as e:
        print("Error 00: ", e)

    all_orders.append(order_2)
    return False


# This function Checks to see if the page is ready to start bidding
# Sometimes the pages don't load when clicked and that can cause problems - this is an inherent nature of the website
# it waits for 20 seconds two times before returning false. It does not discard the order because it is still available
ern = []
def dom_1(order_2):  # click apply
    print("here 1")
    try:  # look for the "Order info" tag on orders
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'section-title')))
        print("Page is ready!")
        return True
    except TimeoutException:
        print("Loading took too much time!")
        is_connected()  # if loading took much time check for internet
        ern.append(4)
        if len(ern) <= 2:  # loop 2 times checking for apply page
            print("Trying because of loading")
            browser.refresh()
            time.sleep(5)
            dom_1(order_2)
            return True
        else:
            ern.clear()
            pass
    except NoSuchElementException:
        print("Not in any order!")
        is_connected()
        what_is_happening()
    except Exception as e:
        print("Error 1: ", e)
        is_connected()
        what_is_happening()

    return False


# This functions checks if the order is on revision or normal.
# It helps in filtering of the orders that are on revision. They are kinda hard, haha. 
def status_check(order_2):
    status = ''
    try:
        status = browser.find_element_by_class_name('data-cell').text
    except Exception:
        pass
    if status == "In progress":
        print(status, "Go ahead")
        return True
    elif status == "Revision" and on_revision == 1:
        print(order_2, " -> Okay: Order is on Revision")
        return True
        #  all_orders.append(order_2)
    elif status == "Revision" and on_revision == 0:
        print(order_2, " -> OUT: Order is on Revision")
        all_orders.append(order_2)
    else:
        print(order_2, " -> Order is on Revision")
        all_orders.append(order_2)
    return False


# This is where the "Apply" button is clicked. It handles all the other scenarios 
# Return true only when the apply bid has been clicked. 
def dom_11(order_2):
    print("here 11")
    k_1 = 'PaulPawaWritedomBot'
    y = ''
    yy = ''
    for _ in itertools.cycle(k_1):
        try:
            y = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/main/div/div/div[1]/div[2]/div/div[4]/div').text
            yy = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/main/div/div/div[1]/div[2]/div/div[4]/div/div[1]/button/div').text
            time.sleep(1)
            break
        except Exception as e:
            print("Error 11: ", e)
            er1.append(0)
            is_connected()
            # what_is_happening()
            if len(er1) < 300:  # loop for 1000 times looking for the order apply button
                continue
            else:
                er1.clear()
                break
    # print("Checking apply")
    if y or yy == 'APPLY':  # if not yet applied
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/main/div/div/div[1]/div[2]/div/div[4]/div/div[1]/button/div/span').click()
        except Exception:
            pass
        time.sleep(1)
        all_orders.append(order_2)
        output.insert(INSERT, "\n Applied => {}\n".format(order_2))
        output.see('end')
        print("Applied -> ", order_2)
        # print(df[0:order_2])
        time.sleep(4)

        return True

    elif y or yy == 'Order is not available':  # if not available
        print(order_2, " -> Order is not available")
        all_orders.append(order_2)
        # unbid_new.remove(order_2)
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass

    elif y or yy == 'Assigned!':  # if You already has the order assigned to you
        print(order_2, " -> Assigned!")
        all_orders.append(order_2)
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass

    # check if order is already applied
    elif y or yy == 'Applied!':  # if applied already
        print(order_2, "-> Already Applied!")
        all_orders.append(order_2)
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass

    else:
        all_orders.append(order_2) # Sometimes this happens, I don't know why but I had to handle the exception
        print("Where are we? Haha!")
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass

    return False


# This is the function called to return to home to continue with the bidding.
# The website does not open other tabs when you click on orders. It stacks them, and this function ensures that we go back to home.
def dom_2():  # Click Available order and return to all orders
    # check if the window size is okay
    size = browser.get_window_size()
    if size["width"] < 1221:
        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        print("Window is small. Adjusting now")
        time.sleep(3)
        browser.set_window_size(1225, 960)
    else:
        pass

    print("here 2")
    try:
        browser.find_element_by_xpath('//*[@id="SideNavBar"]/div/a[6]/div/span/div/span').click()
        return True
    except Exception:
        is_connected()
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
            return True
        except Exception as e:
            print("Error 22: ", e)
            is_connected()
    return False


# This function is called when the page freezes due to messages from the support or unconfirmed assigned orders
# The page is not navigatable when in this state. To prevent recursion depth being reached, this function...
#... helps to make the program idle untill someone responds to the messages which unfreezes the site. Very crucial
def idling():
    print("Idling...")
    hed = ''
    while hed != 'Available orders':
        try:
            hed = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/main/div/div/h3').text
        except Exception:
            pass
        try:
            browser.find_element_by_xpath(
                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
        except Exception:
            pass
        browser.refresh()
        time.sleep(10)
    main()


# This function checks the level of education for the order.
# it is called for every order to check.
# IT helps in filtering complex, phD, etc orders out
def complexity(one_order, level):
    if level == 'H' and one_order not in all_orders:
        if Button_h.get() == 1:
            # this is the school levels for each order
            print(one_order, "->High school : Order Okay")
            original_order_id_list.append(one_order)
        else:
            all_orders.append(one_order)
        return
    else:
        pass

    if level == 'U' and one_order not in all_orders:
        if Button_u.get() == 1:
            # undergraduate(one_order, subject)
            print(one_order, "->Undergraduate : Order Okay")
            original_order_id_list.append(one_order)

        else:
            all_orders.append(one_order)
        return
    else:
        pass

    if level == 'M' and one_order not in all_orders:
        if Button_m.get() == 1:
            # undergraduate(one_order, subject)
            print(one_order, "->Masters : Order Okay")
            original_order_id_list.append(one_order)
        else:
            all_orders.append(one_order)
        return
    else:
        pass

    if level == 'P' and one_order not in all_orders:
        if Button_p.get() == 1:
            # undergraduate(one_order, subject)
            print(one_order, "->PhD : Order Okay")
            original_order_id_list.append(one_order)
        else:
            all_orders.append(one_order)
        return
    else:
        pass
    return


# pages of the order checking for filtering ***************************************************
# referenced in the GUI
# Also checks for slides, problems, and Questions
def with_pages(one_order, pg):
    # pg = int(pg)
    if min_pages.get() <= pg <= max_pages.get():
        if one_order not in original_order_id_list:
            original_order_id_list.append(one_order)
        print(one_order, "->Pages:", pg, ":Order okay")

    elif pg == 0:
        pass
        # original_order_id_list.append(one_order)
    else:
        if one_order not in all_orders:
            all_orders.append(one_order)
        print(one_order, "->Pages", pg, ":Out")
        pass
    return


def other_pages(one_order, slides, problems, questions):
    if slides > 0 and one_order not in all_orders:
        if slides_checked == 1:
            original_order_id_list.append(one_order)
            print(slides, "sides yes")
        else:
            all_orders.append(one_order)
    else:
        pass

    if problems > 0 and one_order not in all_orders:
        if problems_checked == 1:
            original_order_id_list.append(one_order)
            print(problems, "Problems yes")
        else:
            all_orders.append(one_order)
    else:
        pass

    if questions > 0 and one_order not in all_orders:
        if questions_checked == 1:
            original_order_id_list.append(one_order)
            print(questions, "Questions yes")
        else:
            all_orders.append(one_order)
    else:
        pass
    return



# Price check for filtering ***********************************************************
def cpp_calculator(one_order, prc):
    bid_price = 0
    price_1 = prc.split('$')
    price_2 = float(price_1[1])
    # print(Id, "->", price_2 )

    if min_budget.get() < price_2 < max_budget.get():
        if one_order not in original_order_id_list:
            original_order_id_list.append(one_order)
        print(one_order, "->Price", price_2, ":Order Okay")
    else:
        if one_order not in all_orders:
            all_orders.append(one_order)
        print(one_order, "->Price", price_2, ":Out")
    return bid_price


# Deadline Check for filtering *********************************************************
# Here I had to be creative and split the strings and map each corresponsing time to a known time correctly transformed
def time_calculator(one_order, ddline, time_min, time_max):
    bid_time = 0
    actual_time = 1
    # deadline = '1 day 22 hours'
    result_d = ddline.find('day')  # checking for days
    result_h = ddline.find('hour') # Checking for dours
    result_m = ddline.find('min') # Checking for minutes
    res = [int(i) for i in ddline.split() if i.isdigit()]
    # print(res)
    if result_d > 0:  # day present
        if result_h > 0:  # hour present
            # print(Id, "->", "Days:", res[0], " Hours:", res[1])
            actual_time = (res[0] * 24 * 60) + (res[1] * 60)
            # print(Id, "->", actual_time, "Mins")
        elif result_h < 0:
            # print(Id, "->", "Days:", res[0])
            actual_time = (res[0] * 24 * 60)
            # print(Id, "->", actual_time, "Mins")
        else:
            pass
    elif result_d < 0:
        if result_h > 0:
            if result_m > 0:
                # print(Id, "-> ", "Hours:", res[0], " Mins:", res[1])
                actual_time = (res[0] * 60) + res[1]
                # print(Id, "-> ", actual_time, "Mins")
            elif result_m < 0:
                # print(Id, "-> ", "Time Hours:", res[0])
                actual_time = (res[0] * 60)
            # print(Id, "-> ", actual_time, "Mins")
            else:
                pass
        elif result_h < 0:
            # print(Id, "-> ", "Time minutes:", res[0])
            actual_time = (res[0])
            # print(Id, "-> ", actual_time, "Mins")
        else:
            pass
    else:
        pass
    # Actual filtering using the range provided

    if time_min < actual_time < time_max:  # when order deadline is less than what is wanted
        if one_order not in original_order_id_list:
            original_order_id_list.append(one_order)
        print(one_order, "->Time", actual_time, "(hrs):Order Okay")
    else:
        if one_order not in all_orders:
            all_orders.append(one_order)
        print(one_order, "->Time", actual_time, "(hrs):Out")
    return bid_time


# Check the subjet for the order
def subject_check(one_order, subject, unwanted_list):
    subject = subject[1:]
    bid_sub = 0
    # subject = subject[1:].strip()
    # print(Id, "->", subject)
    if subject in unwanted_list:
        all_orders.append(one_order)
        print(one_order, "->Subject", subject, ":Out")
    else:
        original_order_id_list.append(one_order)
        print(one_order, "->Subject", subject, ":Order Okay")
    return bid_sub


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This section contains tha main controls of the program from where all the activities are controlled
# global df
qw = []

def main():
    global all_orders
    all_orders = []
    output = []
    y = []
    w = 0
    global original_order_id_list
    original_order_id_list = []
    size = browser.get_window_size()
    if size["width"] < 1221:
        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        print("Window is small. Adjusting now")
        time.sleep(3)
        browser.set_window_size(1225, 960)
    else:
        pass
    try:
        browser.find_element_by_xpath(
            '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
    except Exception:
        pass

    while w < 2 ** 20: # THis is the main while loop for the fucntion. Preffered over a function because of recurrsion limit and performance
        # ------------------------------------------------------
        output.clear()
        input_or = []
        try:
            orders_present = browser.find_elements_by_xpath('//table/tbody/tr/td')
            for orders in orders_present:
                input_or.append(orders.text)
        except Exception:
            pass

        num = int(len(input_or) / 9)
        # print("Total Orders found: ", num)
        # print(num)
        # list of length in which we have to split
        length_to_split = []
        for k in range(0, num):
            length_to_split.append(9)
        input_or_1 = iter(input_or)
        outp = [list(islice(input_or_1, elem))
                  for elem in length_to_split]
        # ----------------------
        d_ict = {}
        for orders in outp:
            d_ict[orders[0]] = orders[1:]

        df = pd.DataFrame.from_dict(d_ict,
                                    orient='index',
                                    columns=['Topic', 'Price',
                                             'Pages', 'Slides',
                                             'Problems', 'Questions',
                                          'Subject', 'Deadline'])
        pages = 0
        slides = 0
        problems = 0
        questions = 0
        price = ''
        subject = ''
        level = ''
        deadline = ''
            
        for one_order in df.index:
      
            try:
                # topic = df.loc[one_order, 'Topic']
                price = df.loc[one_order, 'Price']
                pages = int(df.loc[one_order, 'Pages'])
                slides = int(df.loc[one_order, 'Slides'])
                problems = int(df.loc[one_order, 'Problems'])
                questions = int(df.loc[one_order, 'Questions'])
                subject = df.loc[one_order, 'Subject']
                level = subject[0]
                deadline = df.loc[one_order, 'Deadline']
            except ValueError:
                pass
            
            # check for value error probably after order confirm page is present
            if pages and slides and problems and questions ==0 and price == '': 
                main()

            # THis is where all the functions calls that happens conditionaly and progressively.
            if one_order not in all_orders:
                subject_check(one_order, subject, unneeded_subject_list)

                if one_order not in all_orders:
                    time_calculator(one_order, deadline, min_deadline.get() * 60, max_deadline.get() * 60)

                    if one_order not in all_orders:
                        cpp_calculator(one_order, price)

                        if one_order not in all_orders:
                            with_pages(one_order, pages)

                            if one_order not in all_orders:
                                complexity(one_order, level)
                                # ----------------------------------------------------------
                                if one_order not in all_orders:
                                    other_pages(one_order, slides, problems, questions)
                                    print("---------------------------------------")
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                # what_is_happening()
                pass
            # When a false is returned at any point, the program will abort and pass every other stage to the deafult state

        original_order_id_list = list(set(sorted(original_order_id_list))) # This is the list of a sorted set that stores that orders that are to be bid are stored. 
        all_orders = list(set(sorted(all_orders)))
        # this compares two list original is the instantaneous and all orders is where all bid
        unbid_new = [x for x in original_order_id_list + all_orders if x not in all_orders] # Compare the list with the unwanted list, or bidded list

        # ------------------------
        # this compares two list original is the instantaneous and all orders is where all bid
        # unbid_new = [x for x in original_order_id_list + all_orders if x not in all_orders]
        if len(unbid_new) > 0:
            for order_1 in unbid_new:
                print("GO for: ->", order_1)
                # header = ''
                try:
                    header = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/main/div/div/h3').text
                except Exception:
                    continue
                time.sleep(2)
                if header == 'Available Orders':  # checking for title of page
                    if dom_0(order_1) is True:
                        if dom_1(order_1) is True:
                            status_check(order_1)
                            if dom_11(order_1) is True:
                                dom_2()
                                pass
                            else:
                                time.sleep(2)
                                break
                        else:
                            time.sleep(2)
                            break
                    else:
                        time.sleep(2)
                        break
                elif header == 'Messages':
                    # Looking for the confirm order page in first 4 rows
                    qw.append(4)
                    if len(qw) < 5:
                        confirm_first_row = ''
                        confirm_sec_row = ''
                        confirm_third_row = ''
                        confirm_four_row = ''
                        try:  # Look for
                            confirm_first_row = browser.find_element_by_xpath('//table/tbody/tr/td[5]')
                        except Exception:
                            pass
                        try:
                            confirm_sec_row = browser.find_element_by_xpath('//table/tbody/tr[2]/td[5]')
                        except Exception:
                            pass
                        try:
                            confirm_third_row = browser.find_element_by_xpath('//table/tbody/tr[3]/td[5]')
                        except Exception:
                            pass
                        try:
                            confirm_four_row = browser.find_element_by_xpath('//table/tbody/tr[3]/td[5]')
                        except Exception:
                            pass
                        # There is a bug here: ValueError: invalid literal for int() with base 10: 'CONFIRM\nREJECT'
                        pr1 = confirm_first_row.text.split('\n')
                        pr2 = confirm_sec_row.text.split('\n')
                        pr3 = confirm_third_row.text.split('\n')
                        pr4 = confirm_four_row.text.split('\n')
                        if pr1[0] or pr2[0] or pr3[0] or pr4[0] == 'CONFIRM':
                            print("Given Order")
                            idling()
                    else:
                        qw.clear()
                        print("Assigned Order")
                else:
                    try:  # click available orders
                        browser.find_element_by_xpath('//*[@id="SideNavBar"]/div/a[6]/div/span/div/span').click()
                        unbid_new.clear()
                    except Exception:
                        try:  # try click available orders again in case previous failed
                            browser.find_element_by_xpath(
                                '/html/body/div[3]/div/div/div/div[1]/div/nav/div/a[6]/div/span/div/div/div[2]').click()
                            unbid_new.clear()
                        except Exception as e:
                            print("Error a: ", e)
                    pass

        else:
            # this if statement is used to delay the refresh of the browser
            y.append(8)
            if len(y) > 14:
                time.sleep(2)
                try:
                    # check if for sure we are on the dashboard before refreshing
                    what_is_happening()
                    # __________________________________
                    # check if the window size is okay
                    size = browser.get_window_size()
                    if size["width"] < 1221:
                        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
                        print("Window is small. Adjusting now")
                        time.sleep(3)
                        browser.set_window_size(1225, 960)
                    else:
                        pass
                    # check for internet connection
                    is_connected()
                    browser.refresh()
                except WebDriverException:
                    pass
                y.clear()
            else:
                pass
            time.sleep(2)
        time.sleep(5)
        w += 1
        print(w)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# This part below ensures that internet is available for it to start the bot. loops untill internet is found
global min_price, max_price, \
    pages_min, pages_max,\
    high_checked, under_checked, master_checked, phd_checked, \
    passw, emal

f = 0

# THis is an color animator for the output screen that is only called when the bot is running
def output_animator():
    colors = ['#7FFFD4', '#454B1B', '#088F8F',
              '#AAFF00', '#5F9EA0', '#097969',
              '#50C878', '#5F8575', '#4F7942',
              '#228B22', '#7CFC00', '#008000',
              '#355E3B', '#00A36C', '#2AAA8A',
              '#4CBB17', '#90EE90', '#32CD32',
              '#478778', '#0BDA51']

    while f < 300000000:
        color = random.choice(colors)
        # output_entry.config(highlightcolor=random.choice(colors))
        output_entry.config(highlightbackground=color, highlightcolor=color)
        time.sleep(0.41)


# This is GUI point of entry to the program. Called when the start button is clicked
# It creates a thread that runs parallel to the GUI to prevent interference of the prgram by the looping GUI function
def start_clicked_0():

    threading.Thread(target=start_clicked).start()


# this is the condional check of the GUI and the program requirements
# Generally checks everything is in order logically
# example, minimum budget should not be more than maximum budget, etc
def start_clicked():

    selected_collector()
    # output.insert(INSERT, "Starting...\n")
    assert len(entry1.get()) and len(entry0.get()) > 0, output.insert(INSERT, "Email or Password cannot be empty\n")
    assert '@' in entry1.get(), output.insert(INSERT, "Please Enter a valid email address\n").see('end')
    # output.insert(INSERT, "Login Details.... Present\n")
    # output.insert(INSERT, "-----------------------------------\n")
    output.see('end')

    assert min_budget.get() < max_budget.get(), output.insert(INSERT, "Min Budget Cannot be more than Max Budget\n")
    output.insert(INSERT, "___________ORDERS TO BID___________ \n")
    output.insert(INSERT, "Budget: {}$ - {}$\n".format(int(min_budget.get()), int(max_budget.get())))
    # output.insert(INSERT, "\n-----------------------------------\n")
    output.see('end')

    assert min_pages.get() < max_pages.get(), output.insert(INSERT, "Min pages Cannot be more than Max pages\n")
    output.insert(INSERT, "Pages:  {} - {} pages\n".format(int(min_pages.get()), int(max_pages.get())))
    # output.insert(INSERT, "\n-----------------------------------\n")
    output.see("end")

    assert min_deadline.get() < max_deadline.get(), output.insert(INSERT, "Min deadline Cannot be more than Max deadline\n")
    output.insert(INSERT, "Time:   {}hrs - {}hrs\n".format(int(min_deadline.get()), int(max_deadline.get())))
    # output.insert(INSERT, "\n-----------------------------------\n")
    output.insert(INSERT, "___________________________________\n")

    assert Button_h.get() or Button_u.get() or Button_m.get() or Button_p.get() == 1, output.insert(INSERT, "Must select at least one level\n")

    first_is_connected()
    print("Internet connection available")
    output.insert(INSERT, "\nAll set")
    output.see("end")

    threading.Thread(target=output_animator).start()
    start_writedom()
    main()


# handle the "STOP" button function on the close. It alerts first before closing
def on_closing():
    if messagebox.askokcancel("Pawa Bidding Bot", "Do you want to quit \nand close the browser?"):
        window.destroy()
        try:
            browser.quit()
        except Exception:
            pass
        
        
# This is the Tkinter code below
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
window = Tk()
window.geometry("879x650")
window.configure(bg="#dce1ed")
# icon = PhotoImage(file = 'pawa icon.ico')
window.iconbitmap('pawa icon.ico')
window.title("PAWA Writedom Bidding Bot")
canvas = Canvas(
    window,
    bg="#dce1ed",
    height=650,
    width=879,
    bd=0,
    highlightthickness=0,
    relief="ridge")
# canvas.config(highlightbackground="#3c6fc7", highlightcolor="#3c6fc7")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    400.0, 333.5,
    image=background_img)

# Output Frame
output_entry = Frame(highlightthickness=10, background="#5b5c5e")
output_entry.config(highlightbackground="#3c6fc7", highlightcolor="#3c6fc7")
output_entry.place(x=40, y=360, height=250, width=345)

output = Text(output_entry, height=250, width=345, bg="#5b5c5e", fg="#fcffe8", wrap=WORD)
head = Label(output_entry, text="PAWA Writedom Bidding Bot", bg="#5b5c5e", fg="#2dcafa")
# counter = Text(head, bg="#5b5c5e", fg="#2dcafa")
# counter.pack(side=LEFT)
head.pack()

# budget_label = Label(other_settings, text="Budget", bg="#83c790", borderwidth=2, relief=SUNKEN)
# budget_label.place(x=15, y=12)
# output.insert(INSERT, "^^^^ Welcome to PAWA Writedom Bot! ^^^^ \n\nI will Help Apply for orders that you desire.\n")

output.insert(INSERT, "Please ensure the settings reflect you type of orders...\n")
output.insert(INSERT, ".....................................\n")

# output.config(foreground="white")


output.pack()

# Stop button
img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=on_closing,
    relief="flat")

b0.place(
    x=276, y=248,
    width=115,
    height=99)

# Start button
img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=start_clicked_0,
    relief="flat")

b1.place(
    x=46, y=248,
    width=116,
    height=104)

# Password entry box
entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    243.0, 223.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#f5f1f1",
    highlightthickness=0)

entry0.place(
    x=105.0, y=206,
    width=276.0,
    height=32)
entry0.config(show="*")

# Email entry box
entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    243.0, 158.5,
    image=entry1_img)
entry1 = Entry(
    bd=0,
    bg="#f5f1f1",
    highlightthickness=0)

entry1.place(
    x=105.0, y=141,
    width=276.0,
    height=33)

all_s = ['Accounting', 'Anthropology', 'Art & architecture', 'Astronomy', 'Biology', 'Business',
                'Chemistry', 'Classic English literature', 'Communication', 'Criminal Law', 'Culture',
                'Ecology', 'Economics', 'Education', 'Educations', 'Engineering', 'English',
                'Environmental studies', 'Accounting', 'Anthropology', 'Art & architecture', 'Astronomy', 'Biology', 'Business',
                'Chemistry', 'Classic English literature', 'Communication', 'Criminal Law', 'Culture',
                'Ecology', 'Economics', 'Education', 'Educations', 'Engineering', 'English',
                'Environmental studies', 'Accounting', 'Anthropology', 'Art & architecture', 'Astronomy', 'Biology', 'Business',
                'Chemistry', 'Classic English literature', 'Communication', 'Criminal Law', 'Culture',
                'Ecology', 'Economics', 'Education', 'Educations', 'Engineering', 'English',
                'Environmental studies']


# The right panel
r_panel = Frame(window, bg="#83c790", height=615, width=435)
r_panel.place(x=430, y=5)


# Creating the tabs, here is the main tab
# 3c6fc7 blueish
# 83c790 green wrtdm
# tab_parent.configure(bg="#83c790")
tab = ttk.Style()
tab.theme_use('default')
tab.configure('TNotebook.Tab', background="#83c790")
tab.map("TNotebook", background=[("selected", "#83c790")])
tab_parent = ttk.Notebook(r_panel)
tab_parent.pack(expand=1, fill=BOTH)

# Settings tab, default
tab_settings = Frame(tab_parent, bg="#808fbf", height=595, width=435)
tab_settings.place(x=430, y=5)
tab_parent.add(tab_settings, text="Settings")
# Label(tab_settings, text="Here is settings").pack()
# **********************************************
# subjects selections
selector = 1
# Checkbutton_select_all = IntVar(value=selector)
Checkbutton1 = IntVar(value=0)
Checkbutton2 = IntVar(value=selector)
Checkbutton3 = IntVar(value=selector)
Checkbutton4 = IntVar(value=selector)
Checkbutton5 = IntVar(value=selector)
Checkbutton6 = IntVar(value=selector)
Checkbutton7 = IntVar(value=0)
Checkbutton8 = IntVar(value=selector)
Checkbutton9 = IntVar(value=selector)
Checkbutton10 = IntVar(value=selector)
Checkbutton11 = IntVar(value=selector)
Checkbutton12 = IntVar(value=selector)
Checkbutton13 = IntVar(value=selector)
Checkbutton14 = IntVar(value=selector)
Checkbutton15 = IntVar(value=selector)
Checkbutton16 = IntVar(value=selector)
Checkbutton17 = IntVar(value=0)
Checkbutton18 = IntVar(value=selector)
Checkbutton19 = IntVar(value=selector)
Checkbutton20 = IntVar(value=selector)
Checkbutton21 = IntVar(value=selector)
Checkbutton22 = IntVar(value=0)
Checkbutton23 = IntVar(value=selector)
Checkbutton24 = IntVar(value=selector)
Checkbutton25 = IntVar(value=selector)
Checkbutton26 = IntVar(value=selector)
Checkbutton27 = IntVar(value=selector)
Checkbutton28 = IntVar(value=selector)
Checkbutton29 = IntVar(value=0)
Checkbutton30 = IntVar(value=selector)
Checkbutton31 = IntVar(value=selector)
Checkbutton32 = IntVar(value=selector)
Checkbutton33 = IntVar(value=0)
Checkbutton34 = IntVar(value=selector)
Checkbutton35 = IntVar(value=selector)
Checkbutton36 = IntVar(value=selector)
Checkbutton37 = IntVar(value=selector)
Checkbutton38 = IntVar(value=0)
Checkbutton39 = IntVar(value=selector)
Checkbutton40 = IntVar(value=selector)
Checkbutton41 = IntVar(value=selector)
Checkbutton42 = IntVar(value=selector)
Checkbutton43 = IntVar(value=selector)
Checkbutton44 = IntVar(value=selector)
Checkbutton45 = IntVar(value=selector)
Checkbutton46 = IntVar(value=0)
Checkbutton47 = IntVar(value=selector)
Checkbutton48 = IntVar(value=selector)
Checkbutton49 = IntVar(value=selector)
Checkbutton50 = IntVar(value=selector)
Checkbutton51 = IntVar(value=selector)
Checkbutton52 = IntVar(value=selector)

check_btn_lst = [Checkbutton1, Checkbutton2, Checkbutton3, Checkbutton4, Checkbutton5, Checkbutton6, Checkbutton7, Checkbutton8, Checkbutton9, Checkbutton10,
                 Checkbutton11, Checkbutton13, Checkbutton14, Checkbutton15, Checkbutton16, Checkbutton17,
                 Checkbutton18, Checkbutton19, Checkbutton20, Checkbutton21, Checkbutton22, Checkbutton23,
                 Checkbutton24, Checkbutton25, Checkbutton26, Checkbutton27, Checkbutton28, Checkbutton29,
                 Checkbutton30, Checkbutton31, Checkbutton32, Checkbutton33, Checkbutton34, Checkbutton35,
                 Checkbutton36, Checkbutton37, Checkbutton12, Checkbutton38, Checkbutton39, Checkbutton40, Checkbutton41,
                 Checkbutton42, Checkbutton43, Checkbutton44, Checkbutton45, Checkbutton46, Checkbutton47,
                 Checkbutton48, Checkbutton49, Checkbutton50, Checkbutton51, Checkbutton52]


all_subjects = ['Accounting', 'Anthropology', 'Art & architecture', 'Astronomy', 'Biology', 'Business',
                'Chemistry', 'Classic English literature', 'Communication', 'Criminal Law', 'Culture',
                'Ecology', 'Economics', 'Education', 'Educations', 'Engineering', 'English',
                'Environmental studies', 'Family and consumer science', 'Film studies', 'Finance',
                'Geography', 'Geology', 'History', 'Human Resource Management', 'Investments',
                'Journalism', 'Law', 'Literature', 'Management', 'Marketing', 'Mathematics',
                'Medicine', 'Music', 'Nursing', 'Other', 'Philosophy', 'Physics', 'Poetry',
                'Political science', 'Psychology', 'Religious studies', 'Shakespeare studies',
                'Sociology', 'Sports', 'Statistics', 'Technology', 'Theater studies', 'Tourism',
                'Women and gender studies', 'World affairs', 'World literature']


def select_all():
    for item in check_btn_lst:
        v = item
        if v.get() == 1:
            v.set(1)
        else:
            v.set(1)


def selected_collector():
    for n, sub in enumerate(check_btn_lst):
        if sub.get() == 0:
            unneeded_subject_list.append(all_subjects[n])
    print(unneeded_subject_list)


my_list = Listbox(tab_settings)
first_list = Listbox(my_list)
second_list = Listbox(my_list)
third_list = Listbox(my_list)

# tab_settings.place(x =430,y = 5,height=595, width=435)
my_list.place(x=0, y=0, width=435,  height=390)
first_list.place(x=0, y=0, width=145, height=385)
second_list.place(x=145, y=0, width=140, height=385)
third_list.place(x=285, y=0, width=145, height=385)
btn_bg = "white"
btn = Button(first_list, text="Select all", command=select_all, bg="#a9c0e8")
btn1 = Button(second_list, text="Get Selected", command=selected_collector, bg=btn_bg)

# first_list.insert(END,btn)
btn.pack(side=TOP)
# btn1.pack(side=BOTTOM)


# The time I made the bot, this is what I knew best. Proud of it but there are other ways to solve this now for me


# Button_select_all = Checkbutton(first_list, text="Select All", variable=Checkbutton_select_all, onvalue=1, offvalue=0, bg=btn_bg, command=select_all)
Button1 = Checkbutton(first_list, text="Accounting", variable=Checkbutton1, onvalue=1, offvalue=0, bg=btn_bg)
Button2 = Checkbutton(first_list, text="Anthropology", variable=Checkbutton2, onvalue=1, offvalue=0, bg=btn_bg)
Button3 = Checkbutton(first_list, text="Art & architecture", variable=Checkbutton3, onvalue=1, offvalue=0, bg=btn_bg)
Button4 = Checkbutton(first_list, text="Astronomy", variable=Checkbutton4, onvalue=1, offvalue=0, bg=btn_bg)
Button5 = Checkbutton(first_list, text="Biology", variable=Checkbutton5, onvalue=1, offvalue=0, bg=btn_bg)
Button6 = Checkbutton(first_list, text="Business", variable=Checkbutton6, onvalue=1, offvalue=0, bg=btn_bg)
Button7 = Checkbutton(first_list, text="Chemistry", variable=Checkbutton7, onvalue=1, offvalue=0, bg=btn_bg)
Button8 = Checkbutton(first_list, text="Cl Eng literature", variable=Checkbutton8, onvalue=1, offvalue=0, bg=btn_bg)
Button9 = Checkbutton(first_list, text="Communication", variable=Checkbutton9, onvalue=1, offvalue=0, bg=btn_bg)
Button10 = Checkbutton(first_list, text="Criminal Law", variable=Checkbutton10, onvalue=1, offvalue=0, bg=btn_bg)
Button11 = Checkbutton(first_list, text="Culture", variable=Checkbutton11, onvalue=1, offvalue=0, bg=btn_bg)
Button13 = Checkbutton(first_list, text="Ecology", variable=Checkbutton13, onvalue=1, offvalue=0, bg=btn_bg)
Button14 = Checkbutton(first_list, text="Economics", variable=Checkbutton14, onvalue=1, offvalue=0, bg=btn_bg)
Button15 = Checkbutton(first_list, text="Education", variable=Checkbutton15, onvalue=1, offvalue=0, bg=btn_bg)
Button16 = Checkbutton(first_list, text="Educations", variable=Checkbutton16, onvalue=1, offvalue=0, bg=btn_bg)
Button17 = Checkbutton(first_list, text="Engineering", variable=Checkbutton17, onvalue=1, offvalue=0, bg=btn_bg)
Button18 = Checkbutton(second_list, text="English", variable=Checkbutton18, onvalue=1, offvalue=0, bg=btn_bg)
Button19 = Checkbutton(second_list, text="Env studies", variable=Checkbutton19, onvalue=1, offvalue=0, bg=btn_bg)
Button20 = Checkbutton(second_list, text="Family/consumer", variable=Checkbutton20, onvalue=1, offvalue=0, bg=btn_bg)
Button21 = Checkbutton(second_list, text="Film studies", variable=Checkbutton21, onvalue=1, offvalue=0, bg=btn_bg)
Button22 = Checkbutton(second_list, text="Finance", variable=Checkbutton22, onvalue=1, offvalue=0, bg=btn_bg)
Button23 = Checkbutton(second_list, text="Geography", variable=Checkbutton23, onvalue=1, offvalue=0, bg=btn_bg)
Button24 = Checkbutton(second_list, text="Geology", variable=Checkbutton24, onvalue=1, offvalue=0, bg=btn_bg)
Button25 = Checkbutton(second_list, text="History", variable=Checkbutton25, onvalue=1, offvalue=0, bg=btn_bg)
Button26 = Checkbutton(second_list, text="H.R.M", variable=Checkbutton26, onvalue=1, offvalue=0, bg=btn_bg)
Button27 = Checkbutton(second_list, text="Investments", variable=Checkbutton27, onvalue=1, offvalue=0, bg=btn_bg)
Button28 = Checkbutton(second_list, text="Journalism", variable=Checkbutton28, onvalue=1, offvalue=0, bg=btn_bg)
Button29 = Checkbutton(second_list, text="Law", variable=Checkbutton29, onvalue=1, offvalue=0, bg=btn_bg)
Button30 = Checkbutton(second_list, text="Literature", variable=Checkbutton30, onvalue=1, bg=btn_bg)
Button31 = Checkbutton(second_list, text="Management", variable=Checkbutton31, onvalue=1, offvalue=0, bg=btn_bg)
Button32 = Checkbutton(second_list, text="Marketing", variable=Checkbutton32, onvalue=1, offvalue=0, bg=btn_bg)
Button33 = Checkbutton(second_list, text="Mathematics", variable=Checkbutton33, onvalue=1, offvalue=0, bg=btn_bg)
Button34 = Checkbutton(second_list, text="Medicine", variable=Checkbutton34, onvalue=1, offvalue=0, bg=btn_bg)
Button35 = Checkbutton(second_list, text="Music", variable=Checkbutton35, onvalue=1, offvalue=0, bg=btn_bg)
Button36 = Checkbutton(third_list, text="Nursing", variable=Checkbutton36, onvalue=1, offvalue=0, bg=btn_bg)
Button37 = Checkbutton(third_list, text="Other", variable=Checkbutton37, onvalue=1, offvalue=0, bg=btn_bg)
Button12 = Checkbutton(third_list, text="Philosophy", variable=Checkbutton12, onvalue=1, offvalue=0, bg=btn_bg)
Button38 = Checkbutton(third_list, text="Physics", variable=Checkbutton38, onvalue=1, offvalue=0, bg=btn_bg)
Button39 = Checkbutton(third_list, text="Poetry", variable=Checkbutton39, onvalue=1, offvalue=0, bg=btn_bg)
Button40 = Checkbutton(third_list, text="Political sci", variable=Checkbutton40, onvalue=1, offvalue=0, bg=btn_bg)
Button41 = Checkbutton(third_list, text="Psychology", variable=Checkbutton41, onvalue=1, offvalue=0, bg=btn_bg)
Button42 = Checkbutton(third_list, text="Religious studies", variable=Checkbutton42, onvalue=1, offvalue=0, bg=btn_bg)
Button43 = Checkbutton(third_list, text="Shakespeare studies", variable=Checkbutton43, onvalue=1, offvalue=0, bg=btn_bg)
Button44 = Checkbutton(third_list, text="Sociology", variable=Checkbutton44, onvalue=1, offvalue=0, bg=btn_bg)
Button45 = Checkbutton(third_list, text="Sports", variable=Checkbutton45, onvalue=1, offvalue=0, bg=btn_bg)
Button46 = Checkbutton(third_list, text="Statistics", variable=Checkbutton46, onvalue=1, offvalue=0, bg=btn_bg)
Button47 = Checkbutton(third_list, text="Technology", variable=Checkbutton47, onvalue=1, offvalue=0, bg=btn_bg)
Button48 = Checkbutton(third_list, text="Theater studies", variable=Checkbutton48, onvalue=1, offvalue=0, bg=btn_bg)
Button49 = Checkbutton(third_list, text="Tourism", variable=Checkbutton49, onvalue=1, offvalue=0, bg=btn_bg)
Button50 = Checkbutton(third_list, text="Women/gender", variable=Checkbutton50, onvalue=1, offvalue=0, bg=btn_bg)
Button51 = Checkbutton(third_list, text="World affairs", variable=Checkbutton51, onvalue=1, offvalue=0, bg=btn_bg)
Button52 = Checkbutton(third_list, text="World literature", variable=Checkbutton52, onvalue=1, offvalue=0, bg=btn_bg)

# my_list.insert(END, Button1)
# my_list.insert(END, Button2)

h1 = [Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9, Button10, Button11, Button13, Button14, Button15, Button16, Button17]
h2 = [Button18, Button19, Button20, Button21, Button22, Button23, Button24, Button25, Button26, Button27, Button28, Button29, Button30, Button31, Button32, Button33, Button34, Button35]
h3 = [Button36, Button37, Button12, Button38, Button39, Button40, Button41, Button42, Button43, Button44, Button45, Button46, Button47, Button48, Button49, Button50, Button51, Button52]
r = 27
jj = []
for things in h1:
    things.place(x=0, y=r)
    r += 21
r = 0
for things in h2:
    things.place(x=0, y=r)
    r += 21
r = 0
for things in h3:
    things.place(x=0, y=r)
    r += 21


# Help tab
tab_help = ttk.Frame(tab_parent)
tab_parent.add(tab_help, text="Help")
Label(tab_help, text="Here is help").pack()
# Activate tab
tab_activate = ttk.Frame(tab_parent)
tab_parent.add(tab_activate, text="Activate")
# Label(tab_activate, text="Here is Activate").pack()

# Spin boxes for pages and budget ,height=615, width=435

other_settings = Frame(tab_settings, bg="#dea249")
other_settings.place(x=0, y=390, width=450, height=205)


# Budget frame ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
budget_frame = Frame(other_settings, bg="white", borderwidth=2, relief=RIDGE)
budget_frame.place(x=10, y=20, width=130, height=80)

# Label for the frame
budget_label = Label(other_settings, text="Budget", bg="#83c790", borderwidth=2, relief=SUNKEN)
budget_label.place(x=15, y=12)
# Min budget
min_budget = DoubleVar(value=3)
budget_label_min = Label(budget_frame, text="Min $", bg="white", relief=FLAT)
budget_label_min.place(x=10, y=13)
s1 = Spinbox(budget_frame, from_=1, to=100, borderwidth=2, relief=RIDGE, textvariable=min_budget)
s1.place(x=10, y=30, width=40, height=30)

# Max budget
max_budget = DoubleVar(value=3000)
budget_label_max = Label(budget_frame, text="Max $", bg="white", relief=FLAT)
budget_label_max.place(x=80, y=13)
s2 = Spinbox(budget_frame, from_=1, to=3000, borderwidth=2, relief=RIDGE, textvariable=max_budget)
s2.place(x=80, y=30, width=40, height=30)


# Pages Frame ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pages_frame = Frame(other_settings, bg="white", borderwidth=2, relief=RIDGE)
pages_frame.place(x=155, y=20, width=130, height=180)

# Label for the frame
pages_label = Label(other_settings, text="Pages", bg="#83c790", borderwidth=2, relief=SUNKEN)
pages_label.place(x=160, y=12)
# Min pages
min_pages = DoubleVar(value=1)
pages_label_min = Label(pages_frame, text="Min", bg="white", relief=FLAT)
pages_label_min.place(x=10, y=13)
sp1 = Spinbox(pages_frame, from_=1, to=100, borderwidth=2, relief=RIDGE, textvariable=min_pages)
sp1.place(x=10, y=30, width=40, height=30)

# Max pages
max_pages = DoubleVar(value=300)
pages_label_max = Label(pages_frame, text="Max", bg="white", relief=FLAT)
pages_label_max.place(x=80, y=13)
sp2 = Spinbox(pages_frame, from_=1, to=300, borderwidth=2, relief=RIDGE, textvariable=max_pages)
sp2.place(x=80, y=30, width=40, height=30)

other_pages_f = Frame(pages_frame, bg="white", borderwidth=2, relief=RIDGE)
other_pages_f.place(x=1, y=96, width=124, height=80)


# Other pages label
other_label = Label(pages_frame, text="Bid orders with:", bg="#83c790", borderwidth=2, relief=SUNKEN)
other_label.place(x=6, y=88)

other_selector = 1
Button_s = IntVar(value=other_selector)
Button_p = IntVar(value=0)
Button_q = IntVar(value=0)

Button_slides = Checkbutton(other_pages_f, text="Slides", variable=Button_s, onvalue=1, offvalue=0, bg=btn_bg)
Button_problems = Checkbutton(other_pages_f, text="Problems", variable=Button_p, onvalue=1, offvalue=0, bg=btn_bg)
Button_questions = Checkbutton(other_pages_f, text="Questions", variable=Button_q, onvalue=1, offvalue=0, bg=btn_bg)

others_var = [Button_s, Button_p, Button_q]
others_btn = [Button_slides, Button_problems, Button_questions]
r = 10
for thin in others_btn:
    thin.place(x=0, y=r)
    r += 21


# Deadline Frame ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deadline_frame = Frame(other_settings, bg="white", borderwidth=2, relief=RIDGE)
deadline_frame.place(x=10, y=120, width=130, height=80)

# Label for the frame
deadline_label = Label(other_settings, text="Deadline", bg="#83c790", borderwidth=2, relief=SUNKEN)
deadline_label.place(x=15, y=112)
# Min deadline
min_deadline = DoubleVar(value=2)
deadline_label_min = Label(deadline_frame, text="Min (hr)", bg="white", relief=FLAT)
deadline_label_min.place(x=10, y=13)
sp1 = Spinbox(deadline_frame, from_=1, to=100, borderwidth=2, relief=RIDGE, textvariable=min_deadline)
sp1.place(x=10, y=30, width=40, height=30)

# Max deadline
max_deadline = DoubleVar(value=1000)
deadline_label_max = Label(deadline_frame, text="Max (hr)", bg="white", relief=FLAT)
deadline_label_max.place(x=80, y=13)
sp2 = Spinbox(deadline_frame, from_=1, to=1000, borderwidth=2, relief=RIDGE, textvariable=max_deadline)
sp2.place(x=80, y=30, width=40, height=30)

time_min = min_deadline.get() * 60
time_max = max_deadline.get() * 60


# **************************************************
complexity_f = Frame(other_settings, bg="white", borderwidth=2, relief=RIDGE)
complexity_f.place(x=300, y=20, width=130, height=100)

# Label for the frame
pages_label = Label(other_settings, text="Academic Level", bg="#83c790", borderwidth=2, relief=SUNKEN)
pages_label.place(x=305, y=12)

level_selector = 1
Button_h = IntVar(value=level_selector)
Button_u = IntVar(value=level_selector)
Button_m = IntVar(value=level_selector)
Button_p = IntVar(value=0)
Button_high = Checkbutton(complexity_f, text="High School", variable=Button_h, onvalue=1, offvalue=0, bg=btn_bg)
Button_Under = Checkbutton(complexity_f, text="Undergraduate", variable=Button_u, onvalue=1, offvalue=0, bg=btn_bg)
Button_Masters = Checkbutton(complexity_f, text="Masters", variable=Button_m, onvalue=1, offvalue=0, bg=btn_bg)
Button_phd = Checkbutton(complexity_f, text="PhD", variable=Button_p, onvalue=1, offvalue=0, bg=btn_bg)

sub_le_var = [Button_h, Button_u, Button_m, Button_p]
sub_le_btn = [Button_high, Button_Under, Button_Masters, Button_phd]
r = 10
for thin in sub_le_btn:
    thin.place(x=0, y=r)
    r += 19


# **************************************************
revision = Frame(other_settings, bg="white", borderwidth=2, relief=RIDGE)
revision.place(x=300, y=130, width=130, height=70)

# Label for the frame
pages_label = Label(other_settings, text="Orders on Revision", bg="#83c790", borderwidth=2, relief=SUNKEN)
pages_label.place(x=305, y=125)

rev_selctor = 0
Button_revision = IntVar(value=rev_selctor)

Button_p = IntVar(value=0)
check_button_rev = Checkbutton(revision, text="Apply them", variable=Button_revision, onvalue=1, offvalue=0, bg=btn_bg)
check_button_rev.place(x=0, y=20)

# Other variables
slides_checked = Button_s.get()
problems_checked = Button_p.get()
questions_checked = Button_q.get()
on_revision = Button_revision.get()

window.resizable(False, False)
window.mainloop()
