# the databaase schema descried

grocery_schema = """
Schema:


Schema:
1. Employee (
   employee_id [PK] — Unique identifier for each employee,
   name — Full name of the employee,
   email [unique] — Employee's email address (must be unique),
   phone — Contact number,
   role — Job role or title (e.g., cashier, manager),
   hire_date — Date when the employee joined,
   salary — Monthly salary,
   is_active — Boolean flag indicating if the employee is currently working
)

2. Customer (
   customer_id [PK] — Unique identifier for each customer,
   name — Full name of the customer,
   phone — Customer's phone number,
   registered_on — Date when the customer registered,
   total_visits — Number of times the customer has visited or purchased,
   total_spent — Total money spent by the customer across all bills
)

3. Category (
   category_id [PK] — Unique identifier for each item category,
   name [unique] — Name of the category (e.g., Dairy, Vegetables),
   aisle_number — Aisle in the store where this category is located,
   description — Brief description of the category
)

4. Supplier (
   supplier_id [PK] — Unique identifier for each supplier,
   name — Supplier's business name,
   phone — Contact number,
   email — Contact email,
   address — Physical address,
   gst_number — Supplier's tax identification number,
   active — Boolean indicating if supplier is actively supplying,
   created_on — Date the supplier was added to the system
)

5. Items (
   item_id [PK] — Unique identifier for each item,
   name — Item name (e.g., Milk, Rice),
   category_id [FK → Category.category_id] — Category this item belongs to,
   supplier_id [FK → Supplier.supplier_id] — Supplier who provides this item,
   price — Unit price of the item,
   stock — Available stock quantity,
   is_returnable — Indicates whether this item can be returned,
   is_available — Boolean flag to mark availability in store

   → Items are linked to `Category` and `Supplier` to classify and track source
)

6. Supplier_Billing (
   supply_id [PK] — Unique ID for each supply transaction,
   supplier_id [FK → Supplier.supplier_id] — Supplier who sent the items,
   item_id [FK → Items.item_id] — The item that was supplied,
   quantity_supplied — Number of units supplied,
   supply_price — Price per unit from supplier,
   supply_date — Date when the supply was made

   → Represents procurement records between suppliers and items
)

7. Billing (
   bill_id [PK] — Unique identifier for each customer bill,
   customer_id [FK → Customer.customer_id] — Customer who made the purchase,
   employee_id [FK → Employee.employee_id] — Employee who created the bill,
   bill_date — Timestamp of the billing,
   total_amount — Final total amount of the bill,
   discount_amount — Discount applied to this bill,
   coupon_code [FK → Coupon.code] — Coupon used, if any

   → Connects customers and employees for a transaction, optionally using a coupon
)

8. Bill_Item (
   bill_item_id [PK] — Unique ID for each item in a bill,
   bill_id [FK → Billing.bill_id] — The bill this item is part of,
   item_id [FK → Items.item_id] — The item that was purchased,
   quantity — Quantity purchased,
   unit_price — Price at time of purchase,
   total_price — unit_price × quantity

   → This is a line-item table connecting Bills and Items
)

9. Return_Items (
   return_id [PK] — Unique ID for each return record,
   bill_item_id [FK → Bill_Item.bill_item_id] — The specific bill item being returned,
   return_date — Timestamp of return,
   reason — Reason provided for return,
   quantity — Quantity returned,
   refund_amount — Amount refunded to customer,
   approved_by [FK → Employee.employee_id] — Employee who approved the return

   → Tracks returned items from bills and ensures returns are managed by employees
)

10. Coupon (
   code [PK] — Unique alphanumeric coupon code,
   discount_percent — Percentage discount offered,
   valid_from — Start date of coupon validity,
   valid_until — End date of coupon validity,
   is_active — Boolean flag indicating if coupon can be applied

   → Referenced in Billing to apply discounts
)

### Examples:

Q: Show all customers who have spent more than 3000.
A: SELECT name FROM Customer WHERE total_spent > 3000;

Q: Get names of employees who are currently active.
A: SELECT name FROM Employee WHERE is_active = TRUE;

Q: List items that are out of stock.
A: SELECT name FROM Items WHERE stock = 0;

Q: Find names of customers who used a coupon.
A: SELECT DISTINCT c.name FROM Customer c JOIN Billing b ON c.customer_id = b.customer_id WHERE b.coupon_code IS NOT NULL;

Q: Get the total quantity of a specific item sold.
A: SELECT i.name, SUM(bi.quantity) AS total_sold FROM Items i JOIN Bill_Item bi ON i.item_id = bi.item_id GROUP BY i.name;

"""
