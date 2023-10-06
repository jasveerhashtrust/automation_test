import time
import subprocess
import pytest
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import tempfile
import os
import socket
import psutil


def terminate_process_by_port(port):
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            connections = proc.connections()
            for conn in connections:
                if conn.laddr.port == port:
                    print(f"Terminating process {proc.pid} using port {port}")
                    process = psutil.Process(proc.pid)
                    process.terminate()
                    process.wait()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


@pytest.mark.usefixtures("setup")
class TestFetchAgents:
    def test_creating_yeour_first_uAgent(self):
        print("copy")
        copy_button = self.driver.find_elements(
            By.XPATH, "//button[@title='Copy code']"
        )
        for i in range(len(copy_button)):
            if i == 2:
                copy_button[i].click()
        time.sleep(3)
        # fist_uagent = pyperclip.paste()
        fist_uagent = 'print("jasveer")'
        print(fist_uagent, "pppppppppppppppppppppppp")
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = os.path.join(temp_dir, "temp_script.py")
            with open(temp_file_path, "w") as temp_file:
                print("write")
                temp_file.write(fist_uagent)
            result = subprocess.Popen(
                ["python", temp_file_path, "--port", "8000"])
            print("Python script output:")
            print(result.stdout)
            time.sleep(6)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            results = sock.connect_ex(("localhost", 8000))
            if results == 0:
                assert True
                terminate_process_by_port(8000)
            else:
                assert False
                print("Port 8000 is not in use.")

    #
    #
    #
    # def test_Creating_an_interval_task(self):
    #     self.driver.find_element(By.XPATH,"//a[text()='Creating an interval task'][1]").click()
    #     copy_button=self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 2:
    #             copy_button[i].click()
    #     time.sleep(3)
    #     interval_task= pyperclip.paste()
    #
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(interval_task)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    #
    #
    # def test_Getting_uAgent_addresses(self):
    #     self.driver.find_element(By.XPATH,"//a[text()='Getting uAgent addresses 🤖📫'][1]").click()
    #     copy_button=self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 4:
    #             copy_button[i].click()
    #     time.sleep(3)
    #     address = pyperclip.paste()
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(address)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    # def test_using_uAgents_storage_function(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='Using uAgents storage function'][1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@title='Copy code']").click()
    #     time.sleep(3)
    #     storage_function= pyperclip.paste()
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(storage_function)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    # def test_registering_in_the_Almanac_Contract(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='Registering in the Almanac Contract'][1]").click()
    #     self.driver.find_element(By.XPATH, "//button[@title='Copy code']").click()
    #     time.sleep(3)
    #     contract = pyperclip.paste()
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(contract)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #
    # def test_communicating_with_other_uAgents1(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='Communicating with other uAgents 📱🤖️'][1]").click()
    #     time.sleep(2)
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 5:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     agents_communication = pyperclip.paste()
    #
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(agents_communication)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(9)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    # def test_communicating_with_other_uAgents2(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='Communicating with other uAgents 📱🤖️'][1]").click()
    #     time.sleep(2)
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 10:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     remote_agents_alice = pyperclip.paste()
    #
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(remote_agents_alice)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(9)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    #
    # def test_communicating_with_other_uAgents3(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='Communicating with other uAgents 📱🤖️'][1]").click()
    #     time.sleep(2)
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 13:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     remote_agents_bob = pyperclip.paste()
    #
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(remote_agents_bob)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8001"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(9)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8001))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8001)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8001 is not in use.")

    # def test_book_a_table_at_a_restaurant_using_uAgents(self):
    #     self.driver.find_element(
    #         By.XPATH,
    #         "//a[text()='How to book a table at a restaurant using uAgents'][1]",
    #     ).click()
    #     time.sleep(2)
    #     # self.driver.execute_script("window.scrollTo(0,5000)")
    #     copy_button = self.driver.find_elements(
    #         By.XPATH, "//button[@title='Copy code']"
    #     )
    #     for i in range(len(copy_button)):
    #         if i == 2:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     book_table = pyperclip.paste()
    #     print(book_table)
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(book_table)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")

    #
    # def test_use_uAgents_to_verify_messages(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='How to use uAgents to verify messages 📬🔐'][1]").click()
    #     self.driver.execute_script("window.scrollTo(0,1000)")
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 7:
    #             copy_button[i].click()
    #     time.sleep(3)
    #     verify_message= pyperclip.paste()
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(verify_message)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    #
    # def test_use_uAgents_to_send_tokens(self):
    #     self.driver.find_element(By.XPATH, "//a[text()='How to use uAgents to send tokens 📊💸'][1]").click()
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 6:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     send_tokens= pyperclip.paste()
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(send_tokens)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
    #
    # def test_use_the_uAgents_to_simulate_a_cleaning_scenario(self):
    #     self.driver.execute_script("window.scrollTo(0,60000)")
    #     self.driver.find_element(By.XPATH, "//a[text()='How to use the uAgents to simulate a cleaning scenario'][1]").click()
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0,5000)")
    #     copy_button = self.driver.find_elements(By.XPATH, "//button[@title='Copy code']")
    #     for i in range(len(copy_button)):
    #         if i == 14:
    #             copy_button[i].click()
    #     time.sleep(4)
    #     cleaning_scenario= pyperclip.paste()
    #
    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         temp_file_path = os.path.join(temp_dir, "temp_script.py")
    #         with open(temp_file_path, "w") as temp_file:
    #             temp_file.write(cleaning_scenario)
    #         result = subprocess.Popen(["python", temp_file_path, "--port", "8000"])
    #         print("Python script output:")
    #         print(result.stdout)
    #         time.sleep(6)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         results = sock.connect_ex(("localhost", 8000))
    #         if results == 0:
    #             assert True
    #             terminate_process_by_port(8000)
    #             time.sleep(3)
    #         else:
    #             assert False
    #             print("Port 8000 is not in use.")
