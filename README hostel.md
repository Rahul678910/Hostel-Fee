<div align="center">

# 🏠 Roommate Expense Splitter

**Split rent, food, and electricity bills fairly, in one quick run.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20App-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

## 📖 About

Living in a hostel or shared flat means one thing: **monthly bill math**. This tiny Python CLI tool takes your room rent, food expenses, and electricity usage, then tells every roommate exactly how much they need to pay. No spreadsheets, no arguments.

## ✨ Features

- 🏢 Handles room / hostel / flat rent
- 🍕 Includes shared food expenses
- ⚡ Calculates electricity bill from **units consumed × rate per unit**
- 👥 Splits the grand total equally among all roommates
- 💰 Clean output in Indian Rupees (₹)

## 🧮 How It Works

```
electricity_bill  = units_used × unit_rate
combined_expense  = room_charge + food_expenses + electricity_bill
individual_share  = combined_expense ÷ number_of_people
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed ([download here](https://www.python.org/downloads/))

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git

# Move into the project folder
cd <your-repo-name>
```

### Run it

```bash
python "For Hostel or Room fee.py"
```

## 🎬 Example Run

```
Enter the monthly room/flat charge = 9000
Enter the total food expenses = 3000
Enter the electricity units consumed = 120
Enter cost per electricity unit = 8
How many people are sharing the space? = 3

Each roommate needs to contribute ₹ 4320
```

**Breakdown:** electricity = 120 × 8 = ₹960 → total = 9000 + 3000 + 960 = ₹12,960 → ₹12,960 ÷ 3 = **₹4,320 each**

## 📁 Project Structure

```
.
├── For Hostel or Room fee.py   # Main script
└── README.md                   # You are here
```

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts used:** user input, type conversion, arithmetic operators, integer division

## 🔮 Future Improvements

- [ ] Support decimal values (currently whole numbers only)
- [ ] Input validation (no zero or negative roommates)
- [ ] Unequal splits (e.g. per-person food or electricity usage)
- [ ] Save monthly history to a CSV file
- [ ] GUI or web version with Flask / Streamlit

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and open a pull request.

## 📄 License

Distributed under the MIT License.

## 👤 Author

**Ramdas Murmu**
Computer Science student • Web Developer • AI/ML enthusiast

⭐ If this saved you from a roommate argument, drop a star!
