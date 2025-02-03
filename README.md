# 📦 Amazon Playwright Test Automation

This repository contains a Playwright test script to automate login, search for an iPhone, add an item to the cart, and log out from [Amazon India](https://www.amazon.in/).

---

## 🚀 **Setup Instructions**

### 1️⃣ **Prerequisites**
Ensure you have the following installed:
- Python (>= 3.8)
- pip (Python package manager)
- Playwright and pytest

---

### 2️⃣ **Installation**
Clone this repository and install dependencies.

# Clone the repository
git clone https://github.com/your-username/amazon-playwright-test.git
cd amazon-playwright-test

# Create a virtual environment (Optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install required packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install

3️⃣ Update Credentials
Modify the test script (test_amazon.py) and replace:
email = "your-email@example.com"
password = "your-password"
with your actual Amazon credentials.

4️⃣ Run the Test
Execute the Playwright test script using pytest:
test_amazon_login.py::test_amazon 

✅ Test Steps : 
1.Open Amazon India (https://www.amazon.in/).
2.Login using your email and password.
3.Search for iPhone.
4.Select the 4th item from search results.
5.Add the selected item to the cart.
6.Navigate to the cart.
7.Log out of Amazon.

☠️ issue: OTP Required for Login
Amazon asks for OTP verification.
The script will pause for 60 seconds after entering credentials.
Manually enter the OTP in the browser before the test proceeds.

Thank you 😊 



