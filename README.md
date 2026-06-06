# Store Management System (Kivy Desktop & Mobile)

A lightweight, cross-platform Store Management application built using Python and the Kivy framework. The system provides a real-time reactive user interface to track inventory details, compute stock levels, and query products instantly via a dynamic local database (`JSON`).

> 🚀 **Current Development Focus:** Successfully running as a desktop client. Currently being packaged using Buildozer for native Android deployment (.apk).

---

## ✨ Features
* **Dynamic Inventory Tracking:** Add items with specific data vectors (Product Name, Quantity, Cost Price, Selling Price, and Purchase Date).
* **Instant Query Engine:** Non-blocking, real-time search filtering as you type.
* **Persistent Local Storage:** Integrated flat-file JSON storage interface ensuring immediate data persistence on exit/crash.
* **Fluid UX Matrix:** Asynchronous UI rendering using Kivy’s `ScrollView` and dynamic layout binding for varying screen resolutions.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3
* **UI Framework:** Kivy (Cross-Platform GUI library)
* **Database:** Local JSON File I/O Serialization

---

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/store-management-kivy.git](https://github.com/YOUR_GITHUB_USERNAME/store-management-kivy.git)
   cd store-management-kivy
