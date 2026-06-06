import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

FILE_NAME = "inventory.json"

class StoreManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 15
        
        # Load data instantly
        self.inventory = self.load_data()

        # --- Header ---
        self.add_widget(Label(
            text="STORE MANAGEMENT SYSTEM", 
            font_size='22sp', 
            bold=True,
            size_hint_y=None, 
            height=50
        ))

        # --- Input Section ---
        form_container = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        form_container.bind(minimum_height=form_container.setter('height'))

        def create_field(label_text, hint):
            field_block = BoxLayout(orientation='vertical', size_hint_y=None, height=65, spacing=3)
            lbl = Label(text=label_text, halign='left', valign='bottom', size_hint_y=None, height=25)
            lbl.bind(size=lbl.setter('text_size'))
            txt_input = TextInput(multiline=False, hint_text=hint, size_hint_y=None, height=35)
            field_block.add_widget(lbl)
            field_block.add_widget(txt_input)
            return field_block, txt_input

        f_name, self.name_input = create_field("Product Name:", "e.g., Laptop")
        f_qty, self.qty_input = create_field("Quantity:", "e.g., 50 or Fifty")
        f_cp, self.cp_input = create_field("Cost Price:", "e.g., 40000")
        f_sp, self.sp_input = create_field("Selling Price:", "e.g., 45000")
        f_date, self.date_input = create_field("Purchase Date:", "e.g., 2026-05-25")

        form_container.add_widget(f_name)
        form_container.add_widget(f_qty)
        form_container.add_widget(f_cp)
        form_container.add_widget(f_sp)
        form_container.add_widget(f_date)

        self.add_widget(form_container)

        # --- Action Buttons ---
        btn_layout = BoxLayout(size_hint_y=None, height=50)
        add_btn = Button(text="Add Product", background_color=(0.1, 0.7, 0.3, 1), font_size='16sp', bold=True)
        add_btn.bind(on_press=self.add_product)
        btn_layout.add_widget(add_btn)
        self.add_widget(btn_layout)

        # --- Search Section ---
        search_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=65, spacing=3)
        search_lbl = Label(text="Search Product by Name:", halign='left', valign='bottom', size_hint_y=None, height=25)
        search_lbl.bind(size=search_lbl.setter('text_size'))
        
        self.search_input = TextInput(multiline=False, hint_text="Type a name to search...")
        self.search_input.bind(text=self.search_product)
        
        search_layout.add_widget(search_lbl)
        search_layout.add_widget(self.search_input)
        self.add_widget(search_layout)

        # --- Results / Display Area ---
        self.scroll_view = ScrollView()
        self.results_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        
        # FIXED THE BUG HERE:
        self.scroll_view.add_widget(self.results_layout)
        self.add_widget(self.scroll_view)
        
        # Initial view showing all items stored in file
        self.display_products(self.inventory)

    def load_data(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, 'r') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_data(self):
        with open(FILE_NAME, 'w') as f:
            json.dump(self.inventory, f, indent=4)

    def add_product(self, instance):
        name = self.name_input.text.strip()
        qty = self.qty_input.text.strip()
        cp = self.cp_input.text.strip()
        sp = self.sp_input.text.strip()
        date = self.date_input.text.strip()

        if not name:
            return 

        new_product = {
            "name": name,
            "quantity": qty,
            "cost_price": cp,
            "selling_price": sp,
            "purchase_date": date
        }

        self.inventory.append(new_product)
        self.save_data()
        
        # Clear fields
        self.name_input.text = ""
        self.qty_input.text = ""
        self.cp_input.text = ""
        self.sp_input.text = ""
        self.date_input.text = ""
        
        self.display_products(self.inventory)

    def display_products(self, data_list):
        self.results_layout.clear_widgets()
        
        if not data_list:
            lbl = Label(text="No matching products found.", size_hint_y=None, height=40, halign="center")
            self.results_layout.add_widget(lbl)
            return

        for prod in reversed(data_list):
            text_display = (
                f"📦 PRODUCT: {prod['name'].upper()}\n"
                f"   🔹 Qty: {prod['quantity']}  |  💵 CP: {prod['cost_price']}  |  📈 SP: {prod['selling_price']}  |  📅 Date: {prod['purchase_date']}"
            )
            
            lbl = Label(
                text=text_display, 
                size_hint_y=None, 
                height=55, 
                halign="left", 
                valign="middle", 
                line_height=1.2
            )
            lbl.bind(size=lbl.setter('text_size'))
            self.results_layout.add_widget(lbl)

    def search_product(self, instance, value):
        query = value.strip().lower()
        
        if not query:
            self.display_products(self.inventory)
            return

        filtered_items = [p for p in self.inventory if query in p['name'].lower()]
        self.display_products(filtered_items)


class StoreApp(App):
    def build(self):
        return StoreManager()

if __name__ == '__main__':
    StoreApp().run()