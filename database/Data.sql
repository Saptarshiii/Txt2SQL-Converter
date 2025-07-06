INSERT INTO Employee (name, email, phone, role, hire_date, salary, is_active) VALUES
('Ravi Sharma', 'ravi@store.com', '9990001111', 'Cashier', '2023-01-12', 25000.00, TRUE),
('Priya Das', 'priya@store.com', '9990002222', 'Manager', '2022-05-01', 40000.00, TRUE),
('Anjali Mehta', 'anjali@store.com', '9990003333', 'Cashier', '2024-02-10', 26000.00, TRUE),
('Sourav Ghosh', 'sourav@store.com', '9990004444', 'Inventory Clerk', '2023-07-15', 28000.00, TRUE),
('Deepak Yadav', 'deepak@store.com', '9990005555', 'Security', '2022-09-01', 22000.00, TRUE),
('Nikita Verma', 'nikita@store.com', '9990006666', 'Assistant Manager', '2023-03-22', 35000.00, TRUE),
('Raj Patel', 'raj@store.com', '9990007777', 'Warehouse Staff', '2023-04-05', 24000.00, TRUE),
('Ayesha Khan', 'ayesha@store.com', '9990008888', 'Cashier', '2024-01-20', 25500.00, TRUE),
('Manoj Sinha', 'manoj@store.com', '9990009999', 'Supervisor', '2022-11-13', 36000.00, TRUE),
('Pooja Iyer', 'pooja@store.com', '9990001010', 'Cleaner', '2023-05-30', 20000.00, TRUE);


INSERT INTO Customer (name, phone, registered_on, total_visits, total_spent) VALUES
('Amit Kumar', '8881112233', '2024-01-05', 5, 2450.00),
('Neha Singh', '8881113344', '2024-03-12', 2, 780.00),
('Rajesh Roy', '8881114455', '2023-12-10', 8, 5520.00),
('Megha Joshi', '8881115566', '2024-04-21', 3, 1290.00),
('Alok Ranjan', '8881116677', '2023-11-03', 6, 3410.00),
('Sonal Tiwari', '8881117788', '2024-01-25', 4, 2120.00),
('Vikas Bansal', '8881118899', '2024-02-18', 7, 4780.00),
('Ritu Kapoor', '8881119900', '2024-03-07', 5, 2560.00),
('Harshita Jain', '8881120011', '2023-09-15', 9, 6190.00),
('Devansh Malhotra', '8881121122', '2024-04-01', 2, 690.00);

INSERT INTO Category (name, aisle_number, description) VALUES
('Snacks', 1, 'Chips, biscuits, munchies other similar items'),
('Dairy', 2, 'Milk, cheese, butter and other milk products'),
('Beverages', 3, 'Tea, coffee, juices'),
('Bakery', 4, 'Bread, cakes, pastries'),
('Vegetables', 5, 'Fresh greens and roots'),
('Fruits', 6, 'Seasonal and imported fruits'),
('Personal Care', 7, 'Shampoo, soap, etc.'),
('Household', 8, 'Cleaners, brooms, kitchen tools'),
('Baby Products', 9, 'Diapers, baby food'),
('Frozen Foods', 10, 'Ice cream, frozen meals');


INSERT INTO Supplier (name, phone, email, address, gst_number, active, created_on) VALUES
('GoodFoods Ltd.', '7770011223', 'contact@goodfoods.com', 'Kolkata, WB', 'GSTIN1234GF', TRUE, '2023-11-01'),
('BeverageCo', '7770011333', 'sales@beverageco.com', 'Delhi, DL', 'GSTIN5678BC', TRUE, '2023-09-15'),
('FreshFarms Pvt.', '7770011444', 'support@freshfarms.com', 'Ranchi, JH', 'GSTIN8888FF', TRUE, '2023-10-20'),
('HouseWise India', '7770011555', 'admin@housewise.com', 'Mumbai, MH', 'GSTIN9999HW', TRUE, '2024-01-05'),
('BabyCare Inc.', '7770011666', 'care@babycare.com', 'Bangalore, KA', 'GSTIN7777BC', TRUE, '2024-02-10');


INSERT INTO Items (name, category_id, supplier_id, price, stock, is_returnable, is_available) VALUES
('Lays Chips', 1, 1, 20.00, 200, TRUE, TRUE),
('Kurkure Masala', 1, 1, 15.00, 150, TRUE, TRUE),
('Oreo Biscuits', 1, 1, 30.00, 100, TRUE, TRUE),
('Amul Milk 1L', 2, 1, 55.00, 180, TRUE, TRUE),
('Amul Butter 100g', 2, 1, 50.00, 90, TRUE, TRUE),
('Mother Dairy Curd 500g', 2, 1, 45.00, 120, TRUE, TRUE),
('Tropicana Orange Juice', 3, 2, 80.00, 70, TRUE, TRUE),
('Pepsi 500ml', 3, 2, 35.00, 130, TRUE, TRUE),
('Red Label Tea 250g', 3, 2, 90.00, 50, TRUE, TRUE),
('Modern Bread', 4, 1, 25.00, 60, TRUE, TRUE),
('Britannia Cake', 4, 1, 20.00, 50, TRUE, TRUE),
('Potato 1kg', 5, 3, 25.00, 250, FALSE, TRUE),
('Tomato 1kg', 5, 3, 30.00, 220, FALSE, TRUE),
('Onion 1kg', 5, 3, 28.00, 230, FALSE, TRUE),
('Banana Dozen', 6, 3, 45.00, 60, FALSE, TRUE),
('Apple 1kg', 6, 3, 120.00, 70, FALSE, TRUE),
('Dove Soap', 7, 4, 55.00, 100, TRUE, TRUE),
('Colgate Toothpaste', 7, 4, 60.00, 90, TRUE, TRUE),
('Harpic Toilet Cleaner', 8, 4, 75.00, 80, TRUE, TRUE),
('Lizol Floor Cleaner', 8, 4, 110.00, 85, TRUE, TRUE),
('Pampers Diapers S', 9, 5, 399.00, 40, TRUE, TRUE),
('Cerelac Wheat', 9, 5, 250.00, 45, TRUE, TRUE), 
('Amul Ice Cream Cup', 10, 1, 30.00, 100, TRUE, TRUE),
('Yummiez Nuggets', 10, 1, 120.00, 60, TRUE, TRUE);


INSERT INTO Coupon (code, discount_percent, valid_from, valid_until, is_active) VALUES
('NEWYEAR10', 10, '2025-01-01', '2025-01-31', TRUE),
('SUMMER5', 5, '2025-05-01', '2025-07-31', TRUE),
('FESTIVE15', 15, '2025-10-01', '2025-11-15', TRUE),
('WELCOME20', 20, '2025-01-01', '2025-12-31', TRUE),
('FLAT50', 50, '2025-04-01', '2025-04-30', FALSE); -- inactive


INSERT INTO Supplier_Billing (supplier_id, item_id, quantity_supplied, supply_price, supply_date) VALUES
(1, 1, 300, 15.00, '2025-06-01'),
(1, 4, 200, 45.00, '2025-06-03'),
(2, 7, 150, 65.00, '2025-06-05'),
(3, 12, 500, 20.00, '2025-06-06'),
(4, 17, 120, 40.00, '2025-06-07'),
(5, 21, 70, 310.00, '2025-06-08');


-- Bills
INSERT INTO Billing (customer_id, employee_id, bill_date, total_amount, discount_amount, coupon_code) VALUES
(1, 1, '2025-07-01 14:30:00', 180.00, 18.00, 'NEWYEAR10'),
(3, 2, '2025-07-02 16:15:00', 320.00, 16.00, 'SUMMER5'),
(5, 3, '2025-07-03 18:00:00', 560.00, 56.00, 'FESTIVE15');

-- Items per bill
INSERT INTO Bill_Item (bill_id, item_id, quantity, unit_price, total_price) VALUES
(1, 1, 2, 20.00, 40.00),
(1, 2, 2, 15.00, 30.00),
(2, 3, 3, 30.00, 90.00),
(2, 4, 2, 55.00, 110.00),
(3, 21, 1, 399.00, 399.00),
(3, 20, 1, 110.00, 110.00);


INSERT INTO Return_Items (bill_item_id, return_date, reason, quantity, refund_amount, approved_by) VALUES
(1, '2025-07-02 10:00:00', 'Broken seal', 1, 20.00, 2),
(6, '2025-07-04 09:00:00', 'Wrong product', 1, 110.00, 3);
